from .task import TaskHandler


class FoodHandler(TaskHandler):

    def __init__(self):
        super(FoodHandler, self).__init__()

    def get_response(self, entity=None):

        if entity is None:
            return self.get_random_response()
        else:
            if self.has_entity(entity, "飯", 0.8):
                return self.filter_responses_by_tags("飯", random_select=True)
            elif self.has_entity(entity, "麵", 0.6):
                return self.filter_responses_by_tags("麵", random_select=True)
            elif self.has_entity(entity, "甜點", 0.6):
                return self.filter_responses_by_tags("甜點", random_select=True)
            else:
                return self.get_random_response()