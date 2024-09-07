from datetime import datetime
from typing import Optional
from typing_extensions import Annotated

from rich.console import Console
from rich.table import Table
from typer import Argument, echo, Typer 

from task_tracker.database import DatabaseClient
from task_tracker.schemas import TaskStatus, UserTask
from task_tracker.utils import show_data

app = Typer()
client = DatabaseClient()
console = Console()


@app.command(name='add', help='Add a new item to Task List')
def cread(task_description: str):
    new_task = UserTask(
        description=task_description,
        status=TaskStatus.TODO,
        created_at=datetime.now(),
        updated_at=None,
    )

    response = client.insert_data(task=new_task)
    if response.success:
        echo(f'Task added successfully with ID: {response.data}')
    else:
        echo(f'Error adding task: {response.message}')


@app.command(name='list', help='List user Tasks')
def read(status: Annotated[Optional[str], Argument()] = None):
    table = Table(title='Tasks List')
    table.add_column('ID', justify='center', style='cyan', no_wrap=True)
    table.add_column(
        'Description', justify='center', style='magenta', no_wrap=True
    )
    table.add_column('Status', justify='center', style='green', no_wrap=True)
    if status is None:
        response = client.get()
        if response.success:    
            show_data(data=response.data, table=table, console=console)
 
        else:
            echo(f'Error listing tasks: {response.message}')
    else:
        if status in TaskStatus:
            response = client.get(status=status)
            if response.success:
                data = response.data
                if data:
                    show_data(data=data, table=table, console=console)
                else:
                    echo('Empty list')
        else:
            part_one = 'Error listing tasks:'
            part_two = 'Invalid input. Please use this options:'
            part_three = '"todo", "in-progress" or "done"' 
            echo(part_one + ' ' + part_two + '' + part_three)

@app.command(name='update', help='Update Task description')
def update_description(id: int, new_description: str):
    response = client.update_data(
        id=id, 
        description=new_description, 
        updated_at=datetime.now().isoformat()
    )
    if response.success:
        echo('Task updated successfully!')
    else:
        echo('Error: Task not updated. ID not found!')

@app.command(
        name='mark-in-progress', help='Update Task status to In-Progress')
def update_to_in_progress(id: int):
    response = client.update_data(
        id=id, 
        status='in-progress', 
        updated_at=datetime.now().isoformat()
    )
    if response.success:
        echo('Task updated successfully!')
    else:
        echo('Error: Task not updated. ID not found!')

@app.command(name='mark-done', help='Update Task status to Done')
def update_to_done(id: int):
    response = client.update_data(
        id=id, status='done', updated_at=datetime.now().isoformat())
    if response.success:
        echo('Task updated successfully!')
    else:
        echo('Error: Task not updated. ID not found!')

@app.command(name='delete', help='Delete Task')
def delete_task(id: int):
    response  = client.delete_data(id=id)

