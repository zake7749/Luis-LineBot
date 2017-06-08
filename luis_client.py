from luis_sdk import LUISClient
from utils.env_setting import get_env_variable

def LuisProcessor():

    APPID = get_env_variable('APPID')
    APPKEY = get_env_variable('APPKEY')
    client = LUISClient(APPID, APPKEY, verbose=True)
    return client

def process_res(res):
    '''
    A function that processes the luis_response object and prints info from it.
    :param res: A LUISResponse object containing the response data.
    :return: None
    '''
    print('---------------------------------------------')
    print('LUIS Response: ')
    print('Query: ' + res.get_query())
    print('Top Scoring Intent: ' + res.get_top_intent().get_name())
    if res.get_dialog() is not None:
        if res.get_dialog().get_prompt() is None:
            print('Dialog Prompt: None')
        else:
            print('Dialog Prompt: ' + res.get_dialog().get_prompt())
        if res.get_dialog().get_parameter_name() is None:
            print('Dialog Parameter: None')
        else:
            print('Dialog Parameter Name: ' + res.get_dialog().get_parameter_name())
        print('Dialog Status: ' + res.get_dialog().get_status())
    print('Entities:')
    for entity in res.get_entities():
        print('"%s":' % entity.get_name())
        print('Type: %s, Score: %s' % (entity.get_type(), entity.get_score()))

def main():

    processor = LuisProcessor()
    res = processor.predict("明天中午要吃什麼")
    process_res(res)

if __name__ == "__main__":
    main()