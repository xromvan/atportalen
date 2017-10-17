import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.graphics import *
from kivy.graphics import Color, Rectangle
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage

class CustomLayout(FloatLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(CustomLayout, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0, 1, 0, 1)  # color should be chnaged to bluem, will be bettger
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
	
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="Välkommen AT läkare"))
        self.add_widget(Label(text="Skriv in dina initialer"))
				
        #Define Username widget
        self.add_widget(Label(text='Användarnamn'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
		
        #Define password widget
        self.add_widget(Label(text='Lösenord'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
		
		#define a login button
        self.add_widget(Button(text='Logga in'))
		# Binding should be added to respond to the press down event


class AtPortal(App):

    def build(self):
	    #Adding our main layout
        login_screen = LoginScreen()
        login_layout = CustomLayout()
		
        login_screen.add_widget(login_layout)
        login_layout.add_widget(
            AsyncImage(
                source="https://www.sahlgrenska.se/Areas/SU/Static/images/vgregion-wave.png",
                size_hint= (1, .8),
                pos_hint={'center_x':.5, 'center_y':.5}))
			
        return login_screen


if __name__ == '__main__':
    AtPortal().run()
