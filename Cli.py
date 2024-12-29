import json_manager
import click
import datetime


@click.group()
def cli():
    pass

@cli.command()
def list():
    data = json_manager.list_task()
    for task in data:
       print(task)
       #print(f"{task["id"]} - {task["description"]} | {task["status"]} | {task["createdAt"]} | {task["updatedAt"]}")


@cli.command()
@click.option('--description', required=True, help="Write task description")
@click.option('--status', default="in-progress", help="Task creation date")  # done, todo, in-progress
@click.option('--date', default=datetime.date.today(), help="Task creation date")
### investigar como puedo hacer para que se rellenen los datos del 
### resto de propiedades de la tarea ("status","createdAt", "updatedAt")
@click.pass_context
def add(ctx, description, status, date):
    if not description:
        ctx.fail("Task description required")
    else:
        data = json_manager.list_task()
        task_id = len(data) + 1 
        new_task = {
            "id": task_id,
            "description": description,
            "status":"in-progress",
            "createdAt": str(date),
            "updatedAt": str(datetime.date.today())

        } 
        data.append(new_task)
        json_manager.add_task(data)

if __name__ == '__main__':
    cli()

