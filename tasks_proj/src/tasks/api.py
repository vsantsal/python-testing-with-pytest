from collections import namedtuple

# Task element types : [summary: str, owner: str, done: bool, id: int]
Task = namedtuple('Task', 'summary owner done id')
# You can use __new__.__defaults__ to create Task objects without having to spcify all fields.
Task.__new__.__defaults__ = (None, None, False, None)


def add(task: Task) -> int:
    """Add a task (a Task object) to the tasks database."""
    if not isinstance(task, Task):
        raise TypeError('task must be Task object')
    if not isinstance(task.summary, str):
        raise ValueError('task.summary must be string')
    if not ((task.owner is None) or
            isinstance(task.owner, str)):
        raise ValueError('task.owner must be string or None)')
    # We test for this in ch5, so keep this commented out to let
    # the ch5 test fail.
    #
    # if not isinstance(task.done, bool):
    #     raise ValueError('task.done must be True or False')
    if task.id is not None:
        raise ValueError('task.id must None')
    if _tasksdb is None:
        raise UninitializedDatabase()
    task_id = _tasksdb.add(task._asdict())
    return task_id


def start_tasks_db(db_path, db_type):  # type: (str, str) -> None
    """Connect API functions to a db."""
    if not isinstance(db_path, str):
        raise TypeError('db_path must be a string')
    global _tasksdb
    if db_type == 'tiny':
        import tasks.tasksdb_tinydb
        _tasksdb = tasks.tasksdb_tinydb.start_tasks_db(db_path)
    elif db_type == 'mongo':
        import tasks.tasksdb_pymongo
        _tasksdb = tasks.tasksdb_pymongo.start_tasks_db(db_path)
    else:
        raise ValueError("db_type must be a 'tiny' or 'mongo'")