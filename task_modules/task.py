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

    def filter_responses_by_tags(self, tag_name, random_select=False):

        valid_responses = []

        for response_col in self.data:
            if tag_name in response_col['tags']:
                valid_responses.append(response_col['defaultResponse'])

        if random_select:
            idx = random.randint(0, len(valid_responses)-1)
            return valid_responses[idx]
        else:
            return valid_responses

    def has_entity(self, entities, entity_type, threshold):

        '''
        :param entities: the result from LUIS.
        :param entity_type: the type of entity we want to search for.
        :param threshold: in range [0,1], to block the entity with low score.
        :return: return true if we found a such entity, else False.
        '''

        for entity in entities:
            if entity_type == entity.get_type() and entity.get_score() > threshold:
                return True
        return False