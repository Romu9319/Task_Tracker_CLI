import json_manager
import click


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
### investigar como puedo hacer para que se rellenen los datos del 
### resto de propiedades de la tarea ("status","createdAt", "updatedAt")
@click.pass_context
def add(ctx, description):
    if not description:
        ctx.fail("Task description required")
    else:
        data = json_manager.list_task()
        task_id = len(data) + 1 
        new_task = {
            "id": task_id,
            "description": description,
        } 
        data.append(new_task)
        json_manager.add_task(data)


if __name__ == '__main__':
    cli()

