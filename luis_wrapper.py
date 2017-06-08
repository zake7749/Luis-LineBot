from luis_sdk import LUISClient

class LuisWrapper(object):

    def __init__(self, APPID, APPKEY):

        self.luis_processer = LUISClient(APPID, APPKEY, verbose=True)

        self.query_history = ''
        self._top_intent_history = ''
        self._entities_history = []

    def predict(self, query):

        '''
        :param query: the end user's query
        :return: (top_intent, entities)
        '''

        res = self.luis_processer.predict(query)
        return self.process_res(res)

    def process_res(self, res):
        '''
        A function that processes the luis_response object and prints info from it.
        :param res: A LUISResponse object containing the response data.
        :return: None
        '''
        self.query_history = res.get_query()

        top_intent = res.get_top_intent().get_name()
        self._top_intent_history = top_intent

        entities = res.get_entities()
        self._entities_history = entities

        return top_intent,entities