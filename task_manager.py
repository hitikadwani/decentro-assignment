from typing import List, Dict, Any, Optional
from complete import storage
from datetime import datetime

def add_task(title: str, description: str = "", due_date: Optional[str] = None) -> None:
    tasks = storage.load_tasks()
    task_id = 1
    if tasks:
        task_id = max(task["id"] for task in tasks) + 1
    new_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "status": "Pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    if due_date:
        new_task["due_date"] = due_date
    tasks.append(new_task)
    storage.save_tasks(tasks)
    print(f"Task '{title}' added with ID: {task_id}")

def list_tasks() -> None:
    tasks = storage.load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    tasks_with_due_date = [task for task in tasks if "due_date" in task]
    tasks_without_due_date = [task for task in tasks if "due_date" not in task]
    if tasks_with_due_date:
        tasks_with_due_date.sort(key=lambda x: x["due_date"])
    sorted_tasks = tasks_with_due_date + tasks_without_due_date
    print("\n===== TASK LIST =====")
    for task in sorted_tasks:
        status_display = "✓" if task["status"] == "Completed" else "⬚"
        due_date_display = f" (Due: {task['due_date']})" if "due_date" in task else ""
        print(f"{task['id']}. [{status_display}] {task['title']}{due_date_display}")
        if task["description"]:
            print(f"   Description: {task['description']}")
        print(f"   Status: {task['status']}")
        print("-------------------")
    print("====================\n")

def complete_task(task_id: int) -> None:
    tasks = storage.load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            storage.save_tasks(tasks)
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task with ID {task_id} not found.")

def delete_task(task_id: int) -> None:
    tasks = storage.load_tasks()
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted_task = tasks.pop(i)
            storage.save_tasks(tasks)
            print(f"Task '{deleted_task['title']}' with ID {task_id} deleted.")
            return
    print(f"Task with ID {task_id} not found.")