import pytest
from pro_filer.actions.main_actions import show_preview


# Test data for different contexts
test_data = [
    ({"all_files": [], "all_dirs": []}, "Found 0 files and 0 directories\n"),
    (
        {
            "all_files": [
                "src/qwe.py",
                "src/utils/rty.py",
                "src/trybe/uio.py",
                "src/actions/asd.py",
                "src/imgs/fgh.py",
                "src/mods/jkl.py",
            ],
            "all_dirs": [
                "src",
                "src/utils",
                "src/trybe",
                "src/actions",
                "src/imgs",
                "src/mods",
            ],
        },
        "Found 6 files and 6 directories\n"
        "First 5 files: ['src/qwe.py', 'src/utils/rty.py', 'src/trybe/uio.py', "
        "'src/actions/asd.py', 'src/imgs/fgh.py']\n"
        "First 5 directories: ['src', 'src/utils', 'src/trybe', 'src/actions', 'src/imgs']\n",
    ),
    (
        {
            "all_files": ["src/__init__.py", "src/utils/__init__.py"],
            "all_dirs": ["src", "src/utils"],
        },
        "Found 2 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', 'src/utils/__init__.py']\n"
        "First 5 directories: ['src', 'src/utils']\n",
    ),
]


@pytest.mark.parametrize("context, expected_output", test_data)
def test_show_preview(capsys, context, expected_output):
    """
    Test function for show_preview.

    Args:
    - capsys: pytest fixture to capture stdout.
    - context (dict): The context containing files and directories.
    - expected_output (str): The expected output.
    """
    show_preview(context)
    captured = capsys.readouterr()
    assert captured.out == expected_output
