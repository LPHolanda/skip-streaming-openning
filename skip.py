import pyautogui
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
import kivy.utils
from popup import open_popup

count = 0
run = True
streaming = ''

pyautogui.useImageNotFoundException()

class Screen(GridLayout):
    btn = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        Window.size = (300,500)
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
        # self.netflixButton.background_normal = 'icons/netflix.png'
        # self.netflixButton.size_hint = (4,4)
        self.netflixButton.background_normal = ''
        self.netflixButton.background_color = kivy.utils.get_color_from_hex('#DE0913')
        self.add_widget(self.netflixButton)

        self.primeButton = Button(
            text = 'primevideo'
        )
        self.primeButton.bind(on_press=self.streaming)
        # self.primeButton.background_normal = 'icons/primevideo.png'
        # self.primeButton.size_hint = (5,5)
        self.primeButton.background_normal = ''
        self.primeButton.background_color = kivy.utils.get_color_from_hex('#1993f7')
        self.add_widget(self.primeButton)

        self.hboButton = Button(
            text = 'hbo'
        )
        self.hboButton.bind(on_press=self.streaming)
        # self.hboButton.background_normal = 'icons/hbomax.jpg'
        # self.hboButton.size_hint = (5,5)
        self.hboButton.background_normal = ''
        self.hboButton.background_color = kivy.utils.get_color_from_hex('#6A1CD1')
        self.add_widget(self.hboButton)

        self.disneystar = Button(
            text = 'disneystar'
        )
        self.disneystar.bind(on_press=self.streaming)
        # self.disneystar.background_normal = 'icons/disneystar.jpg'
        # self.disneystar.size_hint = (5,5)
        self.disneystar.background_normal = ''
        self.disneystar.background_color = kivy.utils.get_color_from_hex('#261E42')
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
        self.title = 'Skip Openning'
        return Screen()
    
    
MeuApp().run()