import streamlit as st
import duckdb
from analysis import rank_vessels_by_value, get_summary

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

area_filter = st.sidebar.selectbox(
    "Area",
    [
        "Romsdalsfjorden 07-31",
        "Romsdalsfjorden 07-32"
    ]
)

# Build filters


result = get_summary(
    length=length_filter,
    gear=gear_filter
)

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


st.subheader("Fleet Investigation")

areas = None

if area_filter == "Romsdalsfjorden 07-31":
    areas = [("07", "31")]

elif area_filter == "Romsdalsfjorden 07-32":
    areas = [("07", "32")]

fleet = rank_vessels_by_value(
    areas=areas,
    species=["Torsk", "Sei"],
    vessel_size=length_filter,
    gear=gear_filter
)

st.caption(f"Total vessels: {len(fleet):,}")

st.dataframe(
    fleet,
    use_container_width=True,
    hide_index=True
)
