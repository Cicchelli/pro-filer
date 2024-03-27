import pytest
from pro_filer.actions.main_actions import find_duplicate_files


@pytest.fixture
def example_files(tmp_path):
    path_one_output = tmp_path / "test1"
    path_two_output = tmp_path / "test2"
    path_three_output = tmp_path / "air.txt"
    path_one_output.mkdir()
    path_two_output.mkdir()
    path_three_output.touch()
    path_three_output.write_text("test1")
    example_text_one = path_one_output / "water.txt"
    example_text_two = path_two_output / "water.txt"
    example_text_one.touch()
    example_text_two.touch()

    return [
        str(example_text_one),
        str(example_text_two),
        str(path_three_output),
    ]


def test_find_duplicate_exception_files():
    except_context = {"all_files": ["test1.py", "test2.py", "test3.py"]}

    with pytest.raises(ValueError):
        find_duplicate_files(except_context)


def test_find_duplicate_duplicates_files(example_files):
    duplicated_context = {"all_files": example_files}

    resulted = find_duplicate_files(duplicated_context)
    assert len(resulted) == 1
    assert "water.txt" in resulted[0][0]
    assert "water.txt" in resulted[0][1]
