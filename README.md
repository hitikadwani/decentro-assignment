# Task Tracker CLI

A simple command-line based to-do list application that allows you to track your tasks efficiently.

## Features

- Add tasks with title, optional description, an,status d  due date
- List all tasks with their status
- Mark tasks as completed
- Delete tasks
- Data persistence using a local JSON file
- Sort tasks by due date

## Project Structure

```
task_tracker/
│
├── main.py                 # CLI entry point
├── complete/
│   └── task_manager.py     # Functions to add, delete, mark complete
├── file/
│   └── storage.py          # Functions to read/write JSON file
├── tasks.json              # Stores task data
└── README.md               # Instructions & how to run
```

## Installation

1. Clone the repository or download the files
2. Ensure you have Python 3.6+ installed

## Usage

### Running the application

Run the application in interactive mode:

```bash
python main.py
```

### Available Commands

- **Add a task**:
  ```
  add <title> [--desc <description>] [--due <YYYY-MM-DD>]
  ```
  Example: `add "Buy groceries" --desc "Milk, eggs, bread" --due 2025-05-10`

- **List all tasks**:
  ```
  list
  ```

- **Mark a task as completed**:
  ```
  complete <id>
  ```
  Example: `complete 1`

- **Delete a task**:
  ```
  delete <id>
  ```
  Example: `delete 2`

- **Show help**:
  ```
  help
  ```

- **Exit the application**:
  ```
  exit
  ```

### Non-interactive Mode

You can also run commands directly without entering interactive mode:

```bash
python main.py add "Buy groceries" --desc "Milk, eggs, bread"
python main.py list
python main.py complete 1
```

## Data Storage

Tasks are stored in a `tasks.json` file in the same directory as the application. The file is created automatically when you add your first task.

## Challenges Faced

Refactoring the project structure required careful handling of imports and file paths to avoid errors. Ensuring robust data storage and cross-platform compatibility also posed challenges, especially when dynamically locating and managing the `tasks.json` file.