# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang.builder import Builder

appView = Builder.load_string("""
<AtPortal>
GridLayout:
  spacing: [ 2, 2 ]
  cols: 1
  Button:
    id: f_but
    text: "[color=000000][b]Anställning - Ledighet[/b][/color]"
    background_color: [ 255, 255, 255, 255 ]
    markup: True
  Button:
    id: f_buta
    text: "[color=000000][b]Tjänstgöring - Schema - Legitimation[/b][/color]"
    background_color: [ 255, 255, 255, 255 ]
    markup: True
  Button:
    id: f_butb
    text: "[color=000000][b]Utbildning - Kurser[/b][/color]"
    background_color: [ 255, 255, 255, 255 ]
    markup: True
  Button:
    id: f_butc
    text: "[color=000000][b]Forskning - Förbättring[/b][/color]"
    background_color: [ 255, 255, 255, 255 ]
    markup: True
  Button:
    id: f_butd
    text: "[color=000000][b]Handledning[/b][/color]"
    background_color: [ 255, 255, 255, 255 ]
    markup: True
  Button:
    id: f_bute
    text: "[color=000000][b]AT-råd - AT-rum[/b][/color]"
    background_color: [ 255, 255, 255, 255 ]
    markup: True
  Button:
    id: f_bute
    text: "[color=000000][b]Kontakt[/b][/color]"
    background_color: [ 255, 255, 255, 255 ]
    markup: True
  Button:
    id: f_bute
    text: "[color=000000][b]Regionkalendern[/b][/color]"
    background_color: [ 255, 255, 255, 255 ]
    markup: True
  Button:
    id: f_bute
    text: "[color=000000][b]Aktuellt[/b][/color]"
    background_color: [ 255, 255, 255, 255 ]
    markup: True
""")

class ATApp(App):
    def build(self):
        return appView

ATApp().run()
