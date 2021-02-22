import sys
sys.path.append('../')

from datetime import datetime as dt

class Program:
    """A coding educational program"""
    id = -1
    name = ''
    # date_added = null

    def __init__(self, id, name, date_added):
        self.id = id
        self.name = name
        self.date_added = dt.strptime(date_added, '%m/%d/%Y')

    def f(self):
        return 'hello world'
