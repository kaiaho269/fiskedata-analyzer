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
    species=None
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

    if vessel_size:
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
