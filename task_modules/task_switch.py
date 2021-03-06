from .restaurant import FoodHandler
from .activity import ActivityHandler
from .weather import WeatherHandler
from .none import NoneHandler
from .greeting import GreetingHandler
from .speech import SpeechHandler


class TaskSwitcher(object):

    def __init__(self):

        self.none_handler = NoneHandler()
        self.food_handler = FoodHandler()
        self.weather_handler = WeatherHandler()
        self.activity_handler = ActivityHandler()
        self.greeting_handler = GreetingHandler()
        self.speech_handler = SpeechHandler()

        self.initialize_handlers()

    def initialize_handlers(self):

        print("[TaskSwitcher] Initializer all handlers......")

        self.food_handler.load_data('data/Food.json')
        self.activity_handler.load_data('data/Activity.json')
        self.speech_handler.load_data('data/Speech.json')

        print("[TaskSwitcher] Initialization succeeded.")

    def get_task_handler(self, intent):

        '''
        :param intent: a string, LUIS's intent.name with best score 
        :return: the task_handler 
        '''

        if intent == "Food":
            return self.food_handler

        if intent == "Activity":
            return self.activity_handler

        if intent == "Greeting":
            return self.greeting_handler

        if intent == "Weather":
            return self.weather_handler

        if intent == "Speech":
            return self.speech_handler

        if intent == "None":
            return self.none_handler