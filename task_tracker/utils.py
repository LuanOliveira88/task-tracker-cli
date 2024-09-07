from rich.console import Console
from rich.table import Table

def show_data(data: list, table: Table, console:Console) -> None:
    for item in data:
        _id = item.doc_id
        _description = item['description']
        _status = item['status']
        table.add_row(str(_id), _description, _status)
    console.print(table)