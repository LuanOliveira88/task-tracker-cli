from datetime import datetime

from task_tracker.schemas import TaskStatus, UserTask


def test_serialize_copy_method_inside_serialize_task():
    user_task_test = UserTask(
        description='Complete the project report by end of the week',
        status=TaskStatus.TODO,
        created_at=datetime.now(),
    )
    assert hasattr(user_task_test, 'copy')


# def test_serialize_task():
#     user_task_test = UserTask()
