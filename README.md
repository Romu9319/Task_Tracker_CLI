# Task Manager CLI
A command line application (CLI) to manage tasks. Allows you to easily add, list, update, delete and change the task status from the terminal.

# Installation 
1. Clone the repository 
    https://github.com/Romu9319/Task_Tracker_CLI.git
2. Install dependencies
    pip install -r requirements.txt
3. Run the CLI
    python cli.py --help

# Available Commands
1. Add new task
    ```bash
      python cli.py add [description] [status] [date]
    ```
    - description: Description of the task (Required)
    - status: Default value: everything. Task states (all, in-progress, done).
    - date: Default value current date. YYYY-MM-DD date format.
    
