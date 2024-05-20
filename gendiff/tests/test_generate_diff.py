from gendiff.scripts.gendiff import generate_diff
import json
from pathlib import Path


def test_generate_diff():
    script_dir = Path(__file__).parent
    file_path1 = script_dir / 'fixtures' / 'file1.json'
    file_path2 = script_dir / 'fixtures' / 'file2.json'
    correct_result_path = script_dir / 'fixtures' / 'right_test_gendiff.txt'
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    f = open(correct_result_path)
    text = f.read()
    f.close
    assert generate_diff(file1, file2) == text
