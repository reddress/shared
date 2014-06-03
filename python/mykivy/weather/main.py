import json

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.network.urlrequest import UrlRequest

class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()
    search_results = ObjectProperty()
    
    def search_location(self):
        search_template = "http://api.openweathermap.org/data/2.5/find?q={}&type=like"
        search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location)

        print("called search location for '{}'".format(self.search_input.text))
        
    def my_function(self, param):
        print(param)

    def found_location(self, request, data):
        data = json.loads(data.decode()) if not isinstance(data, dict) else data # p. 29 needed because of bug
        
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                  for d in data['list']]
        self.search_results.item_strings = cities
        print("\n".join(cities))

class WeatherRoot(BoxLayout):
    pass
        
class WeatherApp(App):
    my_data = "this is Weather app data"
    pass

if __name__ == '__main__':
    WeatherApp().run()
