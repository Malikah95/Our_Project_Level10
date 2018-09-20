import kivy
from kivy import Config
from kivy.lang import Builder

kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

Config.set('graphics', 'width',  350)
Config.set('graphics', 'height', 600)

Builder.load_file("symkivy.kv")

class Manager(ScreenManager):
    pass

class LoginWindow(Screen):
    pass

class Register(Screen):
    pass

class Personal_Info(Screen):
    pass

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

class ScreensApp(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    ScreensApp().run()