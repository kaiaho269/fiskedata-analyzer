import duckdb

CSV_PATH = "/home/kaiaho/Downloads/fangstdata_2025.csv"


def connect():
    return duckdb.connect()


def base_query():
    return f"""
        FROM read_csv_auto(
            '{CSV_PATH}',
            delim=';'
        )
    """
def rank_vessels_by_value(
    start_date=None,
    end_date=None,
    vessel_size=None,
    areas=None,
    species=None,
    gear=None
):
    conn = connect()

    filters = ['"Fartøy ID" IS NOT NULL']

    if start_date:
        filters.append(f'"Siste fangstdato" >= DATE \'{start_date}\'')

    if end_date:
        filters.append(f'"Siste fangstdato" <= DATE \'{end_date}\'')

    size_codes = {
        "Under 11 m": 1,
        "11-14,99 m": 2,
        "15-20,99 m": 3,
        "21-27,99 m": 4,
        "28 m og over": 5,
    }

    if vessel_size and vessel_size != "All vessels":
        code = size_codes[vessel_size]
        filters.append(f'"Lengdegruppe (kode)" = {code}')

    if areas:
        area_conditions = [
            f'("Hovedområde (kode)" = \'{main}\' '
            f'AND "Lokasjon (kode)" = \'{location}\')'
            for main, location in areas
        ]

        filters.append("(" + " OR ".join(area_conditions) + ")")

    if species:
        if isinstance(species, str):
            species = [species]

        species_list = ", ".join(
            f"'{s}'" for s in species
        )

        filters.append(f'"Art - gruppe" IN ({species_list})')

    if gear and gear != "All gears":
        if isinstance(gear, str):
            gear = [gear]

        gear_list = ", ".join(
            f"'{g}'" for g in gear
        )

        filters.append(f'"Redskap" IN ({gear_list})')    
    where_clause = " AND ".join(filters)

    query = f"""
        SELECT
            "Fartøy ID" AS vessel_id,
            MAX("Fartøynavn") AS vessel_name,
            MAX("Registreringsmerke (seddel)") AS registration,
            SUM(TRY_CAST("Fangstverdi" AS DOUBLE)) AS catch_value_nok
        {base_query()}
        WHERE {where_clause}
        GROUP BY "Fartøy ID"
        ORDER BY catch_value_nok DESC
    """
    
    
    return conn.execute(query).fetchdf()
def follow_vessels(vessel_ids):
    conn = connect()

    ids = ", ".join(f"'{v}'" for v in vessel_ids)

    query = f"""
        SELECT
            "Fartøy ID" AS vessel_id,
            MAX("Fartøynavn") AS vessel_name,
            MAX("Registreringsmerke (seddel)") AS registration,
            "Hovedområde (kode)" AS main_area,
            "Lokasjon (kode)" AS location,
            "Art - gruppe" AS species,
            SUM(TRY_CAST("Fangstverdi" AS DOUBLE)) AS catch_value_nok
        {base_query()}
        WHERE "Fartøy ID" IN ({ids})
        GROUP BY
            "Fartøy ID",
            "Hovedområde (kode)",
            "Lokasjon (kode)",
            "Art - gruppe"
        ORDER BY catch_value_nok DESC
    """

    return conn.execute(query).fetchdf()

def get_summary(length=None, gear=None):
    conn = connect()

    filters = []

    if length and length != "All vessels":
        if length == "Under 11 m":
            filters.append(
                'TRY_CAST(REPLACE("Største lengde", \',\', \'.\') AS DOUBLE) < 11'
            )

    if gear and gear != "All gears":
        filters.append(f'"Redskap" = \'{gear}\'')

    where_clause = ""

    if filters:
        where_clause = "WHERE " + " AND ".join(filters)

    query = f"""
    SELECT
        COUNT(*) AS records,
        COUNT(DISTINCT "Fartøy ID") AS vessels
    {base_query()}
    {where_clause}
    """

    return conn.execute(query).fetchone()
