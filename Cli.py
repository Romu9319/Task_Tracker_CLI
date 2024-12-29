import tasks_manager
import click


@click.group()
def cli():
    pass

@cli.command()
def list():
    data = tasks_manager.list_task()
    for task in data:
       print(f"{task["id"]} - {task["description"]} | {task["status"]} | {task["createdAt"]} | {task["updatedAt"]}")

if __name__ == '__main__':
    cli()

