# Task Manager CLI
A command line application (CLI) to manage tasks. Allows you to easily add, list, update, delete and change the task status from the terminal.

# Roadmap project URL
https://roadmap.sh/projects/task-tracker

# Installation 
1. Clone the repository 
    https://github.com/Romu9319/Task_Tracker_CLI.git
2. Install dependencies
    ```bash
      pip install -r requirements.txt
    ```   
4. Run the CLI
    ```bash
      python cli.py --help
    ```
    
# Available Commands
1. Add new task
    ```bash
      python cli.py add [description] [status] [date]
    ```
    - description: Description of the task (Required)
    - status: Default value (todo). Task states (all, in-progress, done).
    - date: Default value current date. YYYY-MM-DD date format.
    - Example:
       ```bash
          python cli.py add "Review documentation" in-progress 2024-06-05
       ```
       or
       ```bash
          python cli.py add "Review documentation"
       ```
       - In this case, status and date will take the default values
    
2. List tasks
   - List all tasks
    ```bash
      python cli.py list
    ```
   - List by status
    ```bash
      python cli.py list [status]
    ```
3. Delete task
    ```bash
      python cli.py delete [id]
    ```
4. Update description
    ```bash
      python cli.py update [id] "New description"
    ```
5. Change status
   - Change to in-progress
   ```bash
      python cli.py mark-in-progress [id]
   ```
   - Change to done
   ```bash
      python cli.py mark-done [id]
   ```
   - Remember that todo is the default state of the tasks, unless it is manually indicated when creating them
    
