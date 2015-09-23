from datetime import datetime, timedelta


class Node:
    def __init__(self, parent = None, name = '', 
            begin = None, spent = None):
        self.name = name
        self.children = []
        self.level = 0
        self.parent = parent
        self.begin = begin or datetime.now().replace(microsecond=0)
        self.spent = spent or timedelta()
        if parent:
            self.level = parent.level + 1
            parent.children.append(self)

    def __repr__(self):
        return "{0}: {1}".format(self.level, self.name)
