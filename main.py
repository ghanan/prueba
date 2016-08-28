import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Win(BoxLayout):
    pass

class AplicApp(App):
    def build(self):
        pan = Win()
        return pan


if __name__=="__main__":
    mapp = AplicApp()
    mapp.run()
