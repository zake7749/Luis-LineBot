from luis_wrapper import LuisWrapper
from utils.env_setting import get_env_variable
from task_modules.task import TaskHandler
from task_modules.task_switch import task_switch

LUIS_APPID = get_env_variable('APPID')
LUIS_APPKEY = get_env_variable('APPKEY')

class Chatbot(object):

    '''
    A Chatbot using LUIS for NLU part.
    '''

    def __init__(self):

        self.task_handler = TaskHandler()
        self.luis_wrapper = LuisWrapper(LUIS_APPID, LUIS_APPKEY)
        self.task_handler.load_data('data/Food.json')

    def get_response(self, query):

        #top_intent, entities = self.luis_wrapper.predict(query)
        #handler = task_switch(top_intent)
        #response = handler.get_response(entities)

        return self.task_handler.get_random_response()

def main():

    c = Chatbot()
    print(c.get_response('今天要吃什麼'))

if __name__ == "__main__":
    main()