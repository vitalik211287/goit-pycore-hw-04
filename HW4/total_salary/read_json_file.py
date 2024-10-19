from pathlib import Path
import json


def read_json_file(path):
    with open(f'{path}', 'r') as f:
        file_content = f.read()  
    return json.loads(file_content)
    
    
# read_json_file()