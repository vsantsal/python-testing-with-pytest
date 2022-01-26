from collections import namedtuple

Task = namedtuple('Task', 'summary owner done id')
# You can use __new__.__defaults__ to create Task objects without having to spcify all fields.
Task.__new__.__defaults__ = (None, None, False, None)
