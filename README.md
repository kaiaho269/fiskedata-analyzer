# Fiskedata Analyzer

![GitHub Actions Workflow Status](https://github.com/kaiaho269/fiskedata-analyzer/actions/workflows/check_sample.yml/badge.svg)

Analysis tool for Norwegian fishing vessel and catch data.
Analysis tool for Norwegian fishing vessel and catch data.

## About

Fiskedata Analyzer is a Python/Streamlit application for exploring
Norwegian commercial fishing vessel and catch data.

The project uses official catch data from the Norwegian Directorate
of Fisheries (Fiskeridirektoratet) to investigate vessel-level
economics, fishing activity, gear, species, fishing areas and
landing patterns.

The project is also a practical learning project for developing
data analysis, Python, DuckDB, Streamlit, Git and GitHub skills.

> **New to development?** Start with [FOR_BEGINNERS.md](FOR_BEGINNERS.md).

## Current status

🚧 Active development

The current version provides a basic dashboard for exploring the
2025 dataset by:

- Vessel length
- Fishing gear
- Vessel count
- Catch records

More detailed vessel-level economic analysis is being developed.

## Data

Source:

Norwegian Directorate of Fisheries (Fiskeridirektoratet)

Dataset:

**Fangstdata (seddel) koblet med fartøydata – 2025**

The raw dataset is not included in this repository because of its
size. It is downloaded separately and excluded through `.gitignore`.

## Technology

- Python
- DuckDB
- Streamlit
- Pandas
- Git / GitHub

## Project goals

The long-term goal is to build an interactive analysis tool that can
help investigate questions such as:

- What does a typical small fishing vessel earn?
- How much variation exists between vessels?
- Which fishing methods and species generate the highest catch value?
- Where are the most economically successful small vessels operating?
- How does catch value relate to fishing days, vessel characteristics
  and crew?
- What might a realistic economic model for a small commercial fishing
  vessel look like?

**Important:** Catch value is not the same as profit or personal income.
Operating costs, financing, maintenance, fuel, gear, insurance, crew
costs and taxes must be considered separately.

## License

This project is currently intended primarily as a personal research
and learning project.
