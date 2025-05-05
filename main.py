#!/usr/bin/env python3
import sys
from complete import task_manager

def print_help():
    """
    Print the help message showing available commands.
    """
    print("\nTask Tracker CLI - Available Commands:")
    print("  add <title> [--desc <description>] [--due <YYYY-MM-DD>]")
    print("      Add a new task with the specified title and optional description and due date")
    print("  list")
    print("      List all tasks")
    print("  complete <id>")
    print("      Mark a task as completed")
    print("  delete <id>")
    print("      Delete a task")
    print("  help")
    print("      Show this help message")
    print("  exit")
    print("      Exit the application\n")

def parse_command():
    """
    Parse command line arguments or get input from the user.
    """
    if len(sys.argv) > 1:
        # If arguments were provided when running the script, use them
        args = sys.argv[1:]
        process_command(args)
        return
    
    # Otherwise, run in interactive mode
    print("Welcome to Task Tracker CLI!")
    print_help()
    
    while True:
        try:
            command = input("\nEnter a command (or 'help' for available commands): ").strip()
            
            if not command:
                continue
                
            if command.lower() == "exit":
                print("Goodbye!")
                break
                
            args = command.split()
            process_command(args)
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

def process_command(args):
    """
    Process a command with its arguments.
    
    Args:
        args: List of command arguments
    """
    command = args[0].lower()
    
    if command == "help":
        print_help()
        
    elif command == "add":
        if len(args) < 2:
            print("Error: Missing task title")
            return
            
        title = args[1]
        description = ""
        due_date = None
        
        i = 2
        while i < len(args):
            if args[i] == "--desc" and i + 1 < len(args):
                description = args[i + 1]
                i += 2
            elif args[i] == "--due" and i + 1 < len(args):
                due_date = args[i + 1]
                i += 2
            else:
                i += 1
                
        task_manager.add_task(title, description, due_date)
        
    elif command == "list":
        task_manager.list_tasks()
        
    elif command == "complete":
        if len(args) < 2:
            print("Error: Missing task ID")
            return
            
        try:
            task_id = int(args[1])
            task_manager.complete_task(task_id)
        except ValueError:
            print("Error: Task ID must be a number")
            
    elif command == "delete":
        if len(args) < 2:
            print("Error: Missing task ID")
            return
            
        try:
            task_id = int(args[1])
            task_manager.delete_task(task_id)
        except ValueError:
            print("Error: Task ID must be a number")
            
    else:
        print(f"Unknown command: {command}")
        print_help()

if __name__ == "__main__":
    parse_command()