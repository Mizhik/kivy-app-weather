import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import requests
import json

API="aab1fb0cd6f961b2d87c23ae2c01ab64"

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout,self).__init__(**kwargs)

        self.cols = 1

        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        self.top_grid.add_widget(Label(text="City: "))
        self.city = TextInput(multiline=False)
        self.top_grid.add_widget(self.city)

        self.add_widget(self.top_grid)

        self.submit = Button(text = "Ok", font_size = 32)
        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        city = self.city.text
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')

        if res:
            data = json.loads(res.text)
            temp = data['main']['temp']
            result = Label(text=f'Weather in {city} is {temp}')
        else:
            result = Label(text="Erorr city")

        self.add_widget(result)
        self.city.text = ''


class MyApp(App):
    def build(self):
       return MyGridLayout()
       
    def on_start(self):
        self.icon = './logo-weather.png'
        self.title = "Weather"

if __name__ == "__main__":
    MyApp().run()