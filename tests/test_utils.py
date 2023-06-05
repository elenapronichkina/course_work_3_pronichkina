from src.utils import read_json, sort_data


def test_read_json(path_to_test_json, expected_result_read_json_test):
    assert read_json(path_to_test_json) == expected_result_read_json_test


def test_sort_data(data_for_sort, expected_result_for_sort):
    assert sort_data (data_for_sort) == expected_result_for_sort