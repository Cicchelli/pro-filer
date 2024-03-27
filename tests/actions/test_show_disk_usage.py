from pro_filer.actions.main_actions import show_disk_usage
from pro_filer.cli_helpers import _get_printable_file_path
import pytest


@pytest.fixture
def empty_context_file():
    return {"all_files": []}


@pytest.fixture
def example_files(tmp_path):

    content_one = "Bem vindo ao mundo do pythonista!!!"
    content_two = "Hello"

    output_file_one = tmp_path / "example_one.txt"
    output_path_two = tmp_path / "example_two.txt"

    output_file_one.touch()
    output_file_one.write_text(content_one)

    output_path_two.touch()
    output_path_two.write_text(content_two)

    return [str(output_file_one), str(output_path_two)]


def test_show_disk_usage_files_without(capsys, empty_context_file):
    show_disk_usage(empty_context_file)
    captured = capsys.readouterr()
    assert captured.out == "Total size: 0\n"


def test_show_disk_files_usages(capsys, example_files):
    context = {"all_files": example_files}

    output_one = f"'{_get_printable_file_path(example_files[0])}':".ljust(70)
    output_two = f"'{_get_printable_file_path(example_files[1])}':".ljust(70)

    show_disk_usage(context)
    captured = capsys.readouterr()

    assert captured.out == (
        f"{output_one} 35 (87%)\n"
        + f"{output_two} 5 (12%)\n"
        + "Total size: 40\n"
    )
