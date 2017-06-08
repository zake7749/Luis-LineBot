from .task import TaskHandler

class FoodHandler(TaskHandler):

    def __init__(self):
        super(FoodHandler, self).__init__()

    def get_response(self, entity='None'):
        return self.get_random_response()