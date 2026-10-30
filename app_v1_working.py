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

query = f"""
SELECT
    COUNT(*) AS records,
    COUNT(DISTINCT "Fartøy ID") AS vessels
FROM read_csv_auto('{CSV_PATH}', delim=';')
"""

result = conn.execute(query).fetchone()

col1, col2 = st.columns(2)

with col1:
    st.metric("Catch records", f"{result[0]:,}")

with col2:
    st.metric("Unique vessels", f"{result[1]:,}")

st.success("🐟 Dataset connected successfully.")
