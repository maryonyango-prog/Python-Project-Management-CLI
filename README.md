# Project Management CLI

A command-line tool to manage users, projects, and tasks with an interactive menu interface.

## Requirements

- Python 3.8 or higher
- See `requirements.txt` for dependencies

## Installation

1. Clone or download the project
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Simply run the program and follow the interactive menu:

```bash
python main.py
```

You'll see a menu with these options:

```
1. Add User
2. List Users
3. Add Project
4. List Projects
5. Add Task
6. List Tasks
7. Complete Task
8. Exit
```

Just select a number and follow the prompts!

### Example Workflow

1. Run `python main.py`
2. Press `1` to add a user
3. Enter name: `John Doe`
4. Enter email: `john@example.com`
5. Press `2` to list all users (shows in a formatted table)
6. Press `3` to add a project
7. Enter project title: `Website Redesign`
8. Enter owner email: `john@example.com`
9. And so on...

## Features

- 👤 **User Management** - Create and track users
- 📁 **Project Organization** - Organize tasks by project
- ✅ **Task Tracking** - Manage and complete tasks
- 💾 **Data Persistence** - All data saved to JSON
- 🎨 **Beautiful Output** - Color-coded, formatted interactive tables

## Project Structure

```
├── main.py              # CLI entry point (interactive menu)
├── models/              # Data models
│   ├── user.py         # User and Person classes
│   ├── project.py      # Project class
│   └── task.py         # Task class
├── utils/              # Utilities
│   └── storage.py      # JSON storage handling
└── data/
    └── storage.json    # Data file (auto-created)
```

## License

See LICENSE file
