from datetime import datetime
from typing import Any, Dict

from task_tracker.schemas import TaskStatus, UserTask


def serialize_task(task: UserTask) -> Dict[str, Any]:
    """Convert complex types to serializable formats."""

    serialized_task = task.copy()
    serialized_task.status = serialized_task.status.value
    serialized_task.created_at = serialized_task.created_at.isoformat()
    if serialized_task.updated_at is not None:
        serialized_task.updated_at = serialized_task.updated_at.isoformat()
    serialized_task = serialized_task.as_dict()
    return serialized_task


def deserialize_task(task: dict[str, Any]) -> UserTask:
    """Convert serialized data back into complex types."""

    if 'status' in task:
        task['status'] = TaskStatus(task['status'])
    if 'created_at' in task:
        task['created_at'] = datetime.fromisoformat(task['created_at'])
    if 'update_at' in task and task['update_at']:
        task['update_at'] = datetime.fromisoformat(task['update_at'])
    return UserTask(**task)
