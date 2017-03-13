class NewList(list):

    def __init__(self, s=[]):
        self.s = s

    def range(self):
        return max(self.s) - min(self.s)