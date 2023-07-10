import pyautogui
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from popup import open_popup

count = 0
run = True
streaming = ''

pyautogui.useImageNotFoundException()

class Screen(GridLayout):
    btn = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        Window.size = (500,500)
        self.cols = 1
        self.startButton = Button(
            text = 'START'
        )
        self.startButton.bind(on_press=self.autoplay)
        self.add_widget(self.startButton)

        self.netflixButton = Button(
            text = 'netflix'
        )
        self.netflixButton.bind(on_press=self.streaming)
        self.add_widget(self.netflixButton)

        self.primeButton = Button(
            text = 'primevideo'
        )
        self.primeButton.bind(on_press=self.streaming)
        self.add_widget(self.primeButton)

        self.hboButton = Button(
            text = 'hbo'
        )
        self.hboButton.bind(on_press=self.streaming)
        self.add_widget(self.hboButton)

        self.disneystar = Button(
            text = 'disneystar'
        )
        self.disneystar.bind(on_press=self.streaming)
        self.add_widget(self.disneystar)


    def streaming(self, instance):
        global streaming
        streaming = instance.text

    def autoplay(self, instance):
        global run
        global streaming

        if not streaming:
            open_popup()
            return

        while run:
            global count 
            count = count+1
            print("autoplay", count)
            try:
                play = pyautogui.locateOnScreen('streaming/'+ streaming +'.png')
                pyautogui.click(play)
                time.sleep(5)
                self.autoplay(self)
            except pyautogui.ImageNotFoundException:
                print('ImageNotFoundException: image not found')


class MeuApp(App):
    def build(self):
        return Screen()
    
    
MeuApp().run()