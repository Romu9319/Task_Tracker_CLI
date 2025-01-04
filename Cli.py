import json_manager
import click
import datetime


@click.group()
def cli():
    pass

# Add new tasks
VALID_STATUSES = ["todo", "in-progress", "done"]
@cli.command()
@click.argument('description', required=True)
@click.argument('status', default="todo", type=str)
@click.argument('date', default=datetime.date.today())
@click.pass_context
def add(ctx, description, status, date):
    if description.strip() == "":
        ctx.fail("Task description is required")
    
    if status and status not in VALID_STATUSES:
        print(f"Invalid status {status}. The valid status are: {', '.join(VALID_STATUSES)}")
    
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        ctx.fail("Invalid date format!. Please use YYYY-MM-DD.")
    
    data = json_manager.read_task()
    task_id = max((task["id"] for task in data), default=0) + 1
    new_task = {
        "id": task_id,
        "description": description,
        "status":status,
        "createdAt": str(date),
        "updatedAt": str(datetime.date.today())
    } 
    data.append(new_task)
    json_manager.add_task(data)
    print(f"New task with id {task_id} has been created")

# List all tasks or list by status
VALID_STATUSES = ["todo", "in-progress", "done"]
@cli.command()
@click.argument("status", required=False, type=str)
def list(status):
    data = json_manager.read_task()

    if status and status not in VALID_STATUSES:
        print(f"Invalid status {status}. The valid status are: {', '.join(VALID_STATUSES)}")

    if not status:
        for task in data:
            print(f"{task["id"]} - {task["description"]} | {task["status"]} | {task["createdAt"]} | {task["updatedAt"]}")
    else:
        tasks = [task for task in data if task["status"] == status]
        if not tasks:
            print(f"Tasks with status {status} not found ")
        else:
            for task in tasks:
                print(f"{task["id"]} - {task["description"]} | {task["status"]} | {task["createdAt"]} | {task["updatedAt"]}")

# Delete task by id
@cli.command()
@click.argument("id", type=str)
def delete(id):
    try:
        task_id = int(id)
    except ValueError:
        print("A numeric ID is required, try again")
        return
    
    data = json_manager.read_task()
    task = next((task for task in data if task["id"] == task_id), None)

    if task is None:
        print(f"Task with id {id} not found")
    else: 
        data.remove(task)
        json_manager.add_task(data)
        print(f"Task with id {id} has been deleted")

# Update task by id
@cli.command()
@click.argument("id", type=str)
@click.argument("description", type=str)
@click.pass_context
def update(ctx, id, description):
    if description.strip() == "":
        ctx.fail("Task description is required")
    try:
        task_id = int(id)
    except ValueError:
        print("A numeric ID is required, try again")
        return

    data = json_manager.read_task()
    for task in data:
        if task["id"] == task_id:
            if description is not None:
                task["description"] = description
                task["updatedAt"] = str(datetime.date.today())
                json_manager.add_task(data)
                print(f"Task with id {task_id} has been updated")
            break

# Change status to in-progress   
@cli.command()
@click.argument("id", type=str)
def mark_in_progress(id):
    try:
        task_id = int(id)
    except ValueError:
        print("A numeric ID is required, try again")
        return
    
    data = json_manager.read_task()
    for task in data:
        if task["id"] == task_id:
            if task["status"] != "in-progress":
                task["status"] = "in-progress"
                task["updatedAt"] = str(datetime.date.today())
                json_manager.add_task(data)
                print(f"Task {task_id} marked as 'in-progress'")
            break
    print(f"Task with id {task_id} not found")


@cli.command()
@click.argument("id", type=int)
def mark_done(id):
    try:
        task_id = int(id)
    except ValueError:
        print("A numeric ID is required, try again")
        return
    
    data = json_manager.read_task()
    for task in data:
        if task["id"] == task_id:
            if task["status"] != "done":
                task["status"] = "done"
                task["updatedAt"] = str(datetime.date.today())
                json_manager.add_task(data)
                print(f"Task {task_id} marked as 'done'")
            break
    print(f"Task with id {task_id} not found")


if __name__ == '__main__':
    cli()

