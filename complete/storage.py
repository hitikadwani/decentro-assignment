import json
import os
from typing import List, Dict, Any

TASKS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'file', 'tasks.json')

def load_tasks() -> List[Dict[str, Any]]:
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)