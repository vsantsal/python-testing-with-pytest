from typing import Dict

from tasks import Task


def test_task_equality():
    """Different tasks should not be equal."""
    t1: Task = Task('sit there', 'brian')
    t2: Task = Task('do something', 'okken')
    assert t1 != t2


def test_dict_equality():
    """Different tasks compared as dicts should not be equal."""
    t1_dict: Dict = Task('make sandwich', 'okken')._asdict()
    t2_dict: Dict = Task('make sandwich', 'okken')._asdict()
    assert t1_dict == t2_dict
