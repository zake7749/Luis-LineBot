from .task import TaskHandler

class GreetingHandler(TaskHandler):

    def __init__(self):
        super(GreetingHandler, self).__init__()

    def get_response(self, entity=None):
        return "你好 :)"