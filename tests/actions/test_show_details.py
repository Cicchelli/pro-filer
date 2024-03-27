from unittest.mock import patch
import pytest
from pro_filer.actions.main_actions import show_details


@pytest.fixture
def file_context_fake():
    return {"base_path": "/home/test/!!!!"}


@pytest.fixture
def found_file_context():
    return {"base_path": "/home/test/Downloads/Trybe_logo.png"}


@pytest.fixture
def found_directory_context():
    return {"base_path": "/home/test/Downloads"}


def test_show_details_file_error(capsys, file_context_fake):
    with patch("os.path.exists", return_value=False):
        show_details(file_context_fake)
        captured = capsys.readouterr()
        assert captured.out == "File '!!!!' does not exist\n"


def test_show_details_found_file(capsys, found_file_context):
    with patch("os.path.exists", return_value=True), patch(
        "os.path.getsize", return_value=100
    ), patch("os.path.isdir", return_value=False), patch(
        "os.path.splitext", return_value=("Trybe_logo", ".png")
    ), patch(
        "os.path.getmtime", return_value=1558447897.0442736
    ):

        show_details(found_file_context)
        captured = capsys.readouterr()

        assert "File name: Trybe_logo.png\n" in captured.out
        assert "File size in bytes: 100\n" in captured.out
        assert "File type: file\n" in captured.out
        assert "File extension: .png\n" in captured.out
        assert "Last modified date: 2019-05-21\n" in captured.out


def test_show_details_found_directory(capsys, found_directory_context):
    with patch("os.path.exists", return_value=True), patch(
        "os.path.getsize", return_value=500
    ), patch("os.path.isdir", return_value=True), patch(
        "os.path.splitext", return_value=("Downloads", "")
    ), patch(
        "os.path.getmtime", return_value=1558447897.0442736
    ):

        show_details(found_directory_context)
        captured = capsys.readouterr()

        assert "File name: Downloads\n" in captured.out
        assert "File size in bytes: 500\n" in captured.out
        assert "File type: directory\n" in captured.out
        assert "File extension: [no extension]\n" in captured.out
        assert "Last modified date: 2019-05-21\n" in captured.out
