from pydantic import BaseModel,Field
from rich.console import Console
from rich.table import Table
import json

TASKS_FILE = "tasks.json"

class Task(BaseModel):
    id: int 
    title: str =Field(..., min_length=1, max_length=100)
    description: str | None = None
    completed: bool = False

def display_menu():
    console = Console()
    console.print("\nTask Manager", style="bold blue")
    console.print("1. View Tasks")
    console.print("2. Add Task")
    console.print("3. Delete Task")
    console.print("4. Mark Task as Completed")
    console.print("5. Exit")    

def display_tasks(tasks):
    if not tasks:
       console = Console()
       console.print("No tasks available.", style="bold red") 
    else:
        console = Console()
        table = Table(title="Task List")
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Title", style="magenta")
        table.add_column("Description", style="green")
        table.add_column("Completed", justify="center", style="red")
    
        for task in tasks:
            completed_status = "Yes" if task.completed else "Pending"
            table.add_row(str(task.id), task.title, task.description or "", completed_status)
    
        console.print(table)

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            data = json.load(f)
        return [Task(**task) for task in data]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump([task.dict() for task in tasks], f)


def get_next_task_id(tasks):
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1       


def create_task(tasks, title, description=None):
    console = Console()
    try:
        new_task = Task(id=get_next_task_id(tasks), title=title, description=description)
        tasks.append(new_task)
        save_tasks(tasks)
      
        console.print("Task added successfully.", style="bold green")
        return new_task
    
    except Exception as e:
        console.print(f"Error creating task: {e}", style="bold red")
        return None


def get_task_by_id(tasks, task_id):
    for task in tasks:
        if task.id == task_id:
            return task
    return None


def update_task(tasks, task_id, title=None, description=None, completed=None):
    task = get_task_by_id(tasks, task_id)
    if task:
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if completed is not None:
            task.completed = completed
        save_tasks(tasks)
        return task
    return None

def delete_task(tasks, task_id):
    task = get_task_by_id(tasks, task_id)
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        return True
    return False


def main():
    console = Console() 
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Choose an option: ")
        

        if choice == "1":
                display_tasks(tasks)

        elif choice == "2":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            new_task = create_task(tasks, title, description)

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to delete: "))
                if delete_task(tasks, task_id):
                    console.print("Task deleted successfully.", style="bold green")
                else:
                    console.print("Task not found.", style="bold red")
            except ValueError:
                console.print("Invalid task ID.", style="bold red")


        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                task = get_task_by_id(tasks, task_id)
                if task:
                    task.completed = True
                    save_tasks(tasks)
                    console.print("Task marked as completed.", style="bold green")
                else:
                    console.print("Task not found.", style="bold red")
            except ValueError:
                console.print("Invalid task ID.", style="bold red")

        elif choice == "4":
            break
        
        elif choice == "5":
            console.print("Exiting the Task Manager. Goodbye!", style="bold green")
            break

        else:
            console = Console()
            console.print("Invalid option. Please try again.", style="bold red")

if __name__ == "__main__":
    main()
