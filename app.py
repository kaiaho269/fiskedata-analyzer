import streamlit as st
import duckdb

CSV_PATH = "/home/kaiaho/Downloads/fangstdata_2025.csv"

st.set_page_config(
    page_title="Fiskedata Analyzer",
    page_icon="🐟",
    layout="wide"
)

st.title("🐟 Fiskedata Analyzer")
st.caption("Fiskeridirektoratet 2025 — vessel and catch analysis")

conn = duckdb.connect()

# Sidebar filters
st.sidebar.header("Filters")

length_filter = st.sidebar.selectbox(
    "Vessel length",
    [
        "All vessels",
        "Under 11 m"
    ]
)

gear_filter = st.sidebar.selectbox(
    "Gear",
    [
        "All gears",
        "Juksa/pilk"
    ]
)

# Build filters
filters = []

if length_filter == "Under 11 m":
    filters.append("""
        TRY_CAST(
            REPLACE("Største lengde", ',', '.')
            AS DOUBLE
        ) < 11
    """)

if gear_filter == "Juksa/pilk":
    filters.append('"Redskap" = \'Juksa/pilk\'')

where_clause = ""

if filters:
    where_clause = "WHERE " + " AND ".join(filters)

# Query
query = f"""
SELECT
    COUNT(*) AS records,
    COUNT(DISTINCT "Fartøy ID") AS vessels
FROM read_csv_auto(
    '{CSV_PATH}',
    delim=';'
)
{where_clause}
"""

result = conn.execute(query).fetchone()

# KPIs
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Catch records",
        f"{result[0]:,}"
    )

with col2:
    st.metric(
        "Unique vessels",
        f"{result[1]:,}"
    )

st.success("🐟 Dataset connected successfully.")
