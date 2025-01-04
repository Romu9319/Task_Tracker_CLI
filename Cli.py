import json_manager
import click
import datetime


@click.group()
def cli():
    pass

# Add new tasks
@cli.command()
@click.option('--description', required=True, help="Write task description")
@click.option('--status', default="todo", help="Task creation date")
@click.option('--date', default=datetime.date.today(), help="Task creation date")
@click.pass_context
def add(ctx, description, status, date):
    if not description:
        ctx.fail("Task description required")
    else:
        data = json_manager.list_task()
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
@cli.command()
@click.argument("status", required=False, type=str)
def list(status):
    data = json_manager.list_task()

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
@click.argument("id", type=int)
def delete(id):
    data = json_manager.list_task()
    task = next((task for task in data if task["id"] == id), None)

    if task is None:
        print(f"Task with id {id} not found")
    else: 
        data.remove(task)
        json_manager.add_task(data)
        print(f"Task with id {id} has been deleted")


@cli.command()
@click.argument("id", type=int)
@click.argument("description", type=str)
def update(id, description):
    data = json_manager.list_task()
    for task in data:
        if task["id"] == id:
            if description is not None:
                task["description"] = description
                task["updatedAt"] = str(datetime.date.today())
                json_manager.add_task(data)
                print(f"Task with id {id} has been updated")
            break
    


@cli.command()
@click.argument("id", type=int)
def mark_in_progress(id):
    data = json_manager.list_task()
    for task in data:
        if task["id"] == id:
            if task["status"] != "in-progress":
                task["status"] = "in-progress"
                task["updatedAt"] = str(datetime.date.today())
                json_manager.add_task(data)
                print(f"Task {id} marked as 'in-progress'")
            break
    print(f"Task with id {id} not found")


@cli.command()
@click.argument("id", type=int)
def mark_done(id):
    data = json_manager.list_task()
    for task in data:
        if task["id"] == id:
            if task["status"] != "done":
                task["status"] = "done"
                task["updatedAt"] = str(datetime.date.today())
                json_manager.add_task(data)
                print(f"Task {id} marked as 'done'")
            break
    print(f"Task with id {id} not found")


if __name__ == '__main__':
    cli()

