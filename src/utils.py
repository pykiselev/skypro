from typing import List, Dict
import json
import os

def get_operations(path: str)-> List[Dict]:
    operations = []
    if os.path.isfile(path) and os.path.getsize(path) > 0:
        try:
            with open(path, encoding='utf-8') as f:
                operations = json.load(f)
        except json.JSONDecodeError:
            operations = []
        finally:
            return operations

print(get_operations("../data/operations.json"))