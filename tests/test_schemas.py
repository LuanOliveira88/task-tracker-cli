from datetime import datetime

from task_tracker.schemas import TaskStatus, UserTask


def test_instance_creation():
    """Test if UserTask class is being instanciated correctly"""

    description = 'Implement new feature'
    status = TaskStatus.TODO
    created_at = datetime.now()
    user_task_test = UserTask(
        description=description, status=status, created_at=created_at
    )

    assert isinstance(user_task_test, UserTask)
    assert user_task_test.description == description
    assert user_task_test.status == status
    assert user_task_test.created_at == created_at
    assert hasattr(user_task_test, 'updated_at')


def test_instance_creation_with_optional_arguments():
    """Test if UserTask is instanciated correctly with all params."""

    description = 'Refactor code'
    status = TaskStatus.IN_PROGRESS
    created_at = datetime.now()
    updated_at = datetime.now()

    user_task_test = UserTask(
        description=description,
        status=status,
        created_at=created_at,
        updated_at=updated_at,
    )
    assert isinstance(user_task_test, UserTask)


def test_as_dict_method():
    user_task_test = UserTask(
        description='Submit the quarterly financial report by Friday',
        status=TaskStatus.TODO,
        created_at=datetime.now(),
    )
    expected_dict = {
        'description': 'Submit the quarterly financial report by Friday',
        'status': TaskStatus.TODO,
        'created_at': datetime.now(),
        'updated_at': None,
    }

    assert isinstance(user_task_test.as_dict(), dict)
    assert user_task_test.as_dict() == expected_dict
