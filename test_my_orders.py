import os
import pytest
from test_consol import save_directory_contents

def test_save_directory_contents(tmpdir):
    # Create temporary directory and files for testing
    tmpdir.mkdir("test_dir1")
    tmpdir.mkdir("test_dir2")
    tmpdir.join("test_file1.txt").write("Test file 1")
    tmpdir.join("test_file2.txt").write("Test file 2")

    # Change to the temporary director
    os.chdir(str(tmpdir))

    # Call the function to save the contents of the working directory
    save_directory_contents()

    # Check the results
    file_path = os.path.join(str(tmpdir), "listdir.txt")
    assert os.path.isfile(file_path)

    with open(file_path, "r") as f:
        content = f.read()

    expected_content = "files: test_file1.txt, test_file2.txt\n" \
                       "dirs: test_dir1, test_dir2\n"
    assert content == expected_content

# Run the test
if __name__ == "__main__":
    pytest.main(["-q", __file__])

def test_show_history(capsys):
    # Initialize history with some test data
    global history
    history = [(100.0, 'пополнение счета'), (50.0, 'покупка - "книга"')]

    # Call the show_history() function
    show_history()

    # Capture the printed output
    captured = capsys.readouterr()

    # Assert the expected output
    expected_output = "История покупок:\n" \
                      "(100.0, 'пополнение счета')\n" \
                      "(50.0, 'покупка - \"книга\"')\n"
    assert captured.out == expected_output

    print("Проверка функции show_history() успешно пройдена.")

# Run the test
if __name__ == "__main__":
    pytest.main(["-q", __file__])






