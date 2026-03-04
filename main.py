#!/usr/bin/env python3
from models import User, Project, Task
from utils import Storage
from rich.console import Console
from rich.table import Table
from rich.panel import Panel


def show_menu():
    """Display the main menu"""
    menu = """
    [bold cyan]PROJECT MANAGEMENT SYSTEM[/bold cyan]
    
    [bold]1.[/bold]  Add User
    [bold]2.[/bold]  List Users
    [bold]3.[/bold]  Add Project
    [bold]4.[/bold]  List Projects
    [bold]5.[/bold]  Add Task
    [bold]6.[/bold]  List Tasks
    [bold]7.[/bold]  Complete Task
    [bold]8.[/bold]  Exit
    """
    return menu


def show_users_table(users, console):
    """Display users in a table"""
    if users:
        table = Table(title=" USERS", title_style="bold blue")
        table.add_column("Name", style="cyan")
        table.add_column("Email", style="magenta")
        for u in users:
            table.add_row(u['name'], u['email'])
        console.print(table)
    else:
        console.print("[dim]  No users found[/dim]")


def show_projects_table(projects, console):
    """Display projects in a table"""
    if projects:
        table = Table(title="PROJECTS", title_style="bold blue")
        table.add_column("Title", style="cyan")
        table.add_column("Owner", style="magenta")
        for p in projects:
            table.add_row(p['title'], p['user_email'])
        console.print(table)
    else:
        console.print("[dim]  No projects found[/dim]")


def show_tasks_table(tasks, console):
    """Display tasks in a table"""
    if tasks:
        table = Table(title="TASKS", title_style="bold blue")
        table.add_column("Status", style="yellow")
        table.add_column("Title", style="cyan")
        table.add_column("Project", style="magenta")
        table.add_column("Assigned To", style="green")
        for t in tasks:
            mark = "" if t['status'] == 'completed' else "⏳"
            table.add_row(mark, t['title'], t['project_title'], t['assigned_to'])
        console.print(table)
    else:
        console.print("[dim]  No tasks found[/dim]")


def add_user(db, console):
    """Add a new user"""
    name = console.input("[cyan]Enter user name: [/cyan]").strip()
    email = console.input("[cyan]Enter user email: [/cyan]").strip()
    
    if not name or not email:
        console.print(" Name and email cannot be empty", style="bold red")
        return
    
    if db.find_user(email):
        console.print(" User already exists", style="bold red")
    else:
        user = User(name, email)
        db.add_user(user.to_dict())
        console.print(f"Added: {user}", style="bold green")


def add_project(db, console):
    """Add a new project"""
    title = console.input("[cyan]Enter project title: [/cyan]").strip()
    owner_email = console.input("[cyan]Enter owner email: [/cyan]").strip()
    
    if not title or not owner_email:
        console.print(" Title and email cannot be empty", style="bold red")
        return
    
    if not db.find_user(owner_email):
        console.print("User not found", style="bold red")
    else:
        project = Project(title, owner_email)
        db.add_project(project.to_dict())
        console.print(f" Added project: {project}", style="bold green")


def add_task(db, console):
    """Add a new task"""
    title = console.input("[cyan]Enter task title: [/cyan]").strip()
    project_title = console.input("[cyan]Enter project name: [/cyan]").strip()
    assigned_email = console.input("[cyan]Enter assignee email: [/cyan]").strip()
    
    if not title or not project_title or not assigned_email:
        console.print(" All fields are required", style="bold red")
        return
    
    if not db.find_project(project_title):
        console.print(" Project not found", style="bold red")
    elif not db.find_user(assigned_email):
        console.print("User not found", style="bold red")
    else:
        task = Task(title, project_title, assigned_email)
        db.add_task(task.to_dict())
        console.print(f" Added task: {task}", style="bold green")


def complete_task(db, console):
    """Mark a task as complete"""
    title = console.input("[cyan]Enter task title to complete: [/cyan]").strip()
    
    if not title:
        console.print(" Task title cannot be empty", style="bold red")
        return
    
    if db.complete_task(title):
        console.print(f" Task '{title}' completed!", style="bold green")
    else:
        console.print(" Task not found", style="bold red")


def main():
    """Main function - Menu-driven interface"""
    console = Console()
    db = Storage()
    
    console.print(Panel("[bold cyan]Welcome to Project Management System[/bold cyan]", 
                        style="bold blue", expand=False))
    
    while True:
        console.print(show_menu())
        choice = console.input("[bold yellow]Select an option (1-8): [/bold yellow]").strip()
        console.print()  # Blank line for readability
        
        if choice == '1':
            add_user(db, console)
        elif choice == '2':
            show_users_table(db.get_users(), console)
        elif choice == '3':
            add_project(db, console)
        elif choice == '4':
            show_projects_table(db.get_projects(), console)
        elif choice == '5':
            add_task(db, console)
        elif choice == '6':
            show_tasks_table(db.get_tasks(), console)
        elif choice == '7':
            complete_task(db, console)
        elif choice == '8':
            console.print("[bold green]Goodbye![/bold green]")
            break
        else:
            console.print("[bold red]Invalid option. Please try again.[/bold red]")
        
        console.input("[dim]Press Enter to continue...[/dim]")
        console.clear()


if __name__ == '__main__':
    main()