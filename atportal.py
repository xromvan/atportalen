#from kivy.app import App
from kivy.lang.builder import Builder

appView = Builder.load_string("""
<AtPortal>
GridLayout:
  cols: 1
  rows: 1
  Button:
    id: f_but
    text: "Test"
""")

appView.run()
