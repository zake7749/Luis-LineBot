from .task import TaskHandler


class ActivityHandler(TaskHandler):

    def __init__(self):
        super(ActivityHandler, self).__init__()

    def get_response(self, entity=None):
        return self.get_random_response()