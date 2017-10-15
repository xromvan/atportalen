# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang.builder import Builder

appView = Builder.load_string("""
<AtPortal>
GridLayout:
  cols: 1
  Button:
    id: f_but
    text: "Anställning - Ledighet"
  Button:
    id: f_buta
    text: "Tjänstgöring - Schema - Legitimation"
  Button:
    id: f_butb
    text: "Utbildning - Kurser"
  Button:
    id: f_butc
    text: "Forskning - Förbättring"
  Button:
    id: f_butd
    text: "Handledning"
  Button:
    id: f_bute
    text: "AT-råd - AT-rum"
  Button:
    id: f_bute
    text: "Kontakt"
  Button:
    id: f_bute
    text: "Regionkalendern"
""")

class ATApp(App):
    def build(self):
        return appView

ATApp().run()
