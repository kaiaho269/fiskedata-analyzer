from analysis import base_query


def test_base_query_reads_semicolon_delimited_csv():
    query = base_query()

    assert "read_csv_auto" in query
    assert "delim=';'" in query
