import csv
from pathlib import Path


def test_sample_fixture_has_expected_shape():
    path = Path("tests/fixtures/fiskedata_sample.csv")
    assert path.exists(), f"Missing sample file: {path}"

    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file, delimiter=";")
        header = next(reader)
        rows = list(reader)

    assert len(header) == 133
    assert len(rows) == 10_000
