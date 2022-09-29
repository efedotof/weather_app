from cgitb import text
from distutils.command.build import build
import requests
from bs4 import BeautifulSoup
from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.relativelayout import RelativeLayout
import lxml

from kivy.core.window import Window
Window.size = (500, 400)
class Main_Pogoda(Screen):
    def session(self):

            city = self.ids.sity_input.text
            response = requests.get(f"https://www.google.ru/search?q={city}+погода")
            soup = BeautifulSoup(response.text, "html.parser")
            grad = soup.find('div', class_='BNeawe iBp4i AP7Wnd')
            grad1 = soup.find('div', class_='BNeawe tAd8D AP7Wnd')
            mm = grad.text
            self.ids.name_button_starting.text = '[color=#00ffcc]Обновить[/color]'
            self.ids.pogoda.text = grad1.text
            self.ids.gradus.text = grad.text

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"
        Builder.load_file('style.kv')
        sm = ScreenManager()
        sm.add_widget(Main_Pogoda(name='menu'))
        return sm

def main():
    global grad
    app = MainApp()
    app.run()


if __name__ == '__main__':
    main()