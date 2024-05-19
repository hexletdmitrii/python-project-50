from gendiff.scripts.gendiff import generate_diff
import json


def test_generate_diff():
    file1 = json.load(open('/home/dmitrii/hexlet/python-project-50/gendiff/tests/fixtures/file1.json'))
    file2 = json.load(open('/home/dmitrii/hexlet/python-project-50/gendiff/tests/fixtures/file2.json'))
    f = open('/home/dmitrii/hexlet/python-project-50/gendiff/tests/fixtures/right_test_gendiff.txt')
    text = f.read()
    f.close
    assert generate_diff(file1, file2) == text
    
 
test_generate_diff()