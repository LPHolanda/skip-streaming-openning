from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button 
from kivy.uix.floatlayout import FloatLayout

def open_popup():
  box = FloatLayout()

  label = (Label(text="choose a player before start.",font_size=15,
    size_hint=(None,None),pos_hint={'x':.25,'y':.6}))
  box.add_widget(label)
  
  button = (Button(text="close",size_hint=(None,None),
    width=400,height=50,pos_hint={'x':0,'y':0}))
    
  box.add_widget(button)
  
  popup = Popup(title="Choose a player",content=box,
    size_hint=(None,None),size=(450,300),auto_dismiss=False,title_size=15)
    
  button.bind(on_press=popup.dismiss)
  
  popup.open()