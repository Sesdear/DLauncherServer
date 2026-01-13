import json

def get_json(file: str) -> dict:
    with open(f"app/jsons/{file}.json", 'r') as f:
        _data: dict = json.load(f)
    return _data