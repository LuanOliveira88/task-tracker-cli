from typing import Any, Optional

from tinydb import Query, TinyDB

from task_tracker.config import get_logger
from task_tracker.schemas import UserTask, TaskStatus
from task_tracker.serializers import serialize_task

logger = get_logger(name=__name__)


class DatabaseResponse:
    def __init__(
        self,
        success: bool,
        data: Optional[Any] = None,
        message: Optional[str] = None,
    ) -> None:
        self.success = success
        self.data = data
        self.message = message

    def __repr__(self) -> str:
        success_part = f'success={self.success}'
        data_part = f'data={self.data}'
        message_part = f'message={self.message}'
        return f'DatabaseResponse({success_part}, {data_part}, {message_part})'


class DatabaseClient:
    def __init__(self) -> None:
        self.__path = 'test_db.json'
        self.client = TinyDB(path=self.__path, indent=4)
        self.table = self.client.table('tests')
        self.query = Query()

    def insert_data(self, task: UserTask) -> DatabaseResponse:
        try:
            serialized_task = serialize_task(task)
            doc_id = self.table.insert(document=serialized_task)
            logger.info(f'Task inserted successfully with ID: {doc_id}')
            return DatabaseResponse(success=True, data=doc_id, message='OK')

        except Exception as error:
            logger.error(
                f'Failed to insert task. Error: {error}', exc_info=True
            )
            return DatabaseResponse(
                success=False,
                message='Error: Task could not be saved to the database.',
            )

    def get(self, status: Optional[str] = None) -> DatabaseResponse:
        if status is None:
            try:
                data = self.table.all()
                return DatabaseResponse(success=True, data=data, message='OK')
            except Exception:
                return DatabaseResponse(
                    success=True, data=data, message='DB retrieving error'
                )
        else:
            data = self.table.search(self.query.status == status)
            return DatabaseResponse(success=True, data=data, message='OK')


    def update_data(self, id: int, **kwargs) -> DatabaseResponse:
        try:
            data = self.table.update({**kwargs}, doc_ids=[id])
            return DatabaseResponse(success=True, data=data, message='OK')
        except Exception as error:
            return DatabaseResponse(success=False, message=f'Error: {error}')
        
    def delete_data(id: int) -> DatabaseResponse:
        pass