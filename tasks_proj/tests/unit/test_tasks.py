from typing import Dict

from tasks import Task


def test_task_has_default_instantiation():
    """Using no parameters should invoke defaults."""
    task_1: Task = Task()
    task_2: Task = Task(None, None, False, None)

    assert task_1 == task_2


def test_task_member_access():
    """Check .field functionality of namedtuple."""
    test_task: Task = Task('buy milk', 'brian')
    assert test_task.summary == 'buy milk'
    assert test_task.owner == 'brian'
    assert (test_task.done, test_task.id) == (False, None)


def test_task_as_dict():
    """_asdict should return a dictionary."""
    test_task: Task = Task('do something', 'okken', True, 21)
    t_dict_obtained: Dict = test_task._asdict()
    expected: Dict = {'summary': 'do something',
                      'owner': 'okken',
                      'done': True,
                      'id': 21}
    assert t_dict_obtained == expected


def test_task_replace():
    """replace() should change passed in fields."""
    test_task_before: Task = Task('finish book', 'brian', False)
    test_task_after: Task = test_task_before._replace(id=10, done=True)
    expected_task: Task = Task('finish book', 'brian', True, 10)
    assert test_task_after == expected_task
