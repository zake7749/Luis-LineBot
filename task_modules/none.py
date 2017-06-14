from .task import TaskHandler


class NoneHandler(TaskHandler):

    def __init__(self):
        super(NoneHandler, self).__init__()

    def get_response(self, entity=None):
        return "這部分仍在施工中"