import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file("style.kv")

class MyGridLayout(Widget):
    name = ObjectProperty(None)
    surname = ObjectProperty(None)
    age = ObjectProperty(None)

    def press(self):
        name = self.name.text
        surname = self.surname.text
        age = self.age.text

        #self.add_widget(Label(text=f'Hello {surname} {name}, your age is {age}'))
        print(f'Hello {surname} {name}, your age is {age}')
        self.name.text = ''
        self.surname.text = ''
        self.age.text = ''

class MyApp(App):
    def build(self):
       return MyGridLayout()
       
    def on_start(self):
        self.icon = './logo-weather.png'
        self.title = "Weather"

if __name__ == "__main__":
    MyApp().run()