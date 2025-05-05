import json
import os
from typing import List, Dict, Any

# Define the path to the JSON file
TASKS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'file', 'tasks.json')

def load_tasks() -> List[Dict[str, Any]]:
    """
    Load tasks from the JSON file.
    If the file doesn't exist, return an empty list.
    """
    if not os.path.exists(TASKS_FILE):
        return []
    
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        # If the file is empty or not valid JSON, return an empty list
        return []

def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    """
    Save tasks to the JSON file.
    """
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)