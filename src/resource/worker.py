class Worker:  # 工人类
    def __init__(self, index, name):
        self.index = index
        self.name = name
        self.start = 0
        self.end = None
        self.index_list = []

    def clear(self):  # 解码用：清除工人的工作信息
        self.start = 0
        self.end = None
        self.index_list = []
