from .task import TaskHandler


class SpeechHandler(TaskHandler):

    def __init__(self):
        super(SpeechHandler, self).__init__()

    def get_response(self, entity=None):
        return self.get_random_response()