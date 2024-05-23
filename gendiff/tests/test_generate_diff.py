from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.gendiff import parser_file


def test_generate_diff1():
    file1 = parser_file('file1.json')
    file2 = parser_file('file2.json')
    correct_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(file1, file2) == correct_result


def test_generate_diff2():
    file1 = parser_file('file1.yml')
    file2 = parser_file('file2.yml')
    correct_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(file1, file2) == correct_result


def test_generate_diff3():
    file1 = parser_file('file4.json')
    file2 = parser_file('file5.json')
    correct_result = parser_file('right_test_gendiff.txt')
    assert generate_diff(file1, file2) == correct_result


def test_generate_diff4():
    file1 = parser_file('file4.yml')
    file2 = parser_file('file5.yaml')
    correct_result = parser_file('right_test_gendiff.txt')
    assert generate_diff(file1, file2) == correct_result


def test_generate_diff5():
    file1 = parser_file('file4.yml')
    file2 = parser_file('file5.json')
    correct_result = parser_file('right_test_gendiff.txt')
    assert generate_diff(file1, file2) == correct_result


def test_generate_diff6():
    file1 = parser_file('file4.yml')
    file2 = parser_file('file5.json')
    correct_result = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''
    print(generate_diff(file1, file2, 'plain'))
    assert generate_diff(file1, file2, 'plain') == correct_result
