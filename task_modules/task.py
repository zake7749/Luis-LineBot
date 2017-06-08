import random
import json

class TaskHandler(object):

    def __init__(self):

        self.data = None

    def load_data(self, path):

        with open(path, 'r', encoding='utf-8') as input:
            self.data = json.load(input)

    def get_response(self, entity='None'):
        raise NotImplementedError

    def get_random_response(self):

        idx = random.randint(0, len(self.data)-1)
        return self.data[idx]['defaultResponse']