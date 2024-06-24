from pathlib import Path
import yaml
import json


def parser_file(file_name):
    if '/' in file_name:
        file_path = file_name
    else:
        script_dir = Path(__file__).parent.parent
        file_path = script_dir / 'gendiff' / 'tests' / 'fixtures' / file_name
    file_check = Path(file_path)
    if not file_check.exists():
        return 'Error'
    if file_name.endswith('json'):
        with open(file_path) as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return 'Error'
            # return json.load(f)
    elif file_name.endswith('yml') or file_name.endswith('yaml'):
        with open(file_path) as f:
            return yaml.safe_load(f)
    elif file_name.endswith('txt'):
        with open(file_path) as f:
            return f.read()
