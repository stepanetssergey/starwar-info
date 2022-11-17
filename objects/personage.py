import requests
from settings.config import Config


class Personage:

    api_all = 'people'
    api_search = 'people/?search='

    def __init__(self, personage_name):
        self.name = personage_name

    def api_get(self, request_text):
        result = requests.get(Config.API_PATH + request_text)
        current_personages = result.json()
        return current_personages['results']

    def get_all(self):
        list_of_names = []
        current_personages = self.api_get(self.api_all)
        for item in current_personages:
            list_of_names.append(item['name'])
        return list_of_names

    def get_one(self):
        current_personages = self.api_get(self.api_search+self.name)
        return current_personages[0]

    def show_personage(self, item):
        #{'name':'joe', 'age': 20}
        # [name, age]
        for parameter in item.keys():
            try:
                print(parameter+':'+item[parameter])
            except:
                pass

