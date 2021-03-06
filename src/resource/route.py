from .task import Task


class Route:
    def __init__(self, name=None, index=None):
        self.name = name
        self.index = index
        self.task = {}

    def clear(self):
        for i in self.task.keys():
            self.task[i].clear()

    @property
    def nop(self):  # 工序数量
        return len(self.task)

    def add_task(self, machine, duration, name=None, limited_wait=None, resumable=None, worker=None, index=None):
        if index is None:
            index = self.nop
        self.task[index] = Task(index, machine, duration, name, limited_wait, resumable, worker)
