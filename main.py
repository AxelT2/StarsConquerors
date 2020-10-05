
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.layout import Layout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from sphinx.addnodes import only
from kivy.uix.boxlayout import BoxLayout

Builder.load_string(""" 
<PantallaEstrellas>    
    GridLayout:
        cols: 1
        Button:
            text:"Galaxias"
        Button:
            text: "Sistema Solar"
        Button:
            text: "Constelaciones"            
    
<PantallaGalaxias>
    BoxLayout:
        Button:
            text: "Galaxia1"
            on_press: root.manager.current = 'Galaxy1'
        Button:
            text: "Galaxia2"
            on_press: root.manager.current = 'Galaxy2'
        Button:
            text: "Galaxia3"    
            on_press: root.manager.current = 'Galaxy3'    
    
<PantallaSistema>    
    GridLayout:
        Label:
            text: "Imagen del sistema"
        Label:
            text: "Info del planeta seleccionado"
            
<PantallaConstela>
    BoxLayout:
        Label:
            text: "Imagen de la constelación"
        Label:
            text: "Info de la constelacion"
            
<PantallaEspacio>
    BoxLayout:
        Label
            text: "Hi there, conqueror!"
        Label
            text: "What are you looking for today?"    
        Label.
            text: "Tierra desde el espacio"    
                    
<PantallaMisiones>
    
<PantallaSatelites>
""")

class PantallaGalaxias(Screen):

    pass

class PantallaEstrellas(Screen):

    pass

class PantallaSistema(Screen):

    pass

class PantallaConstela(Screen):

    pass

class PantallaEspacio(Screen):

    pass
class PantallaMisiones(Screen):

    pass

class PantallaSatelites(Screen):

    pass

class Search(TextInput):
    def __init__(self, **kwargs):
        self.add_widget(Label(text="Search"))
        self.search = TextInput(multiline=False)
        self.add_widget(self.search)

class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols = 1

        self.botones = GridLayout()
        self.botones.cols = 3


        self.sate = Button(text="Satélites", font_size = 30)
        self.botones.add_widget(self.sate)
        self.mis = Button(text="Misiones", font_size=30)
        self.botones.add_widget(self.mis)
        self.espacio = Button(text="Desde el espacio", font_size=30)
        self.botones.add_widget(self.espacio)
        self.add_widget(self.botones)


        self.BotonTierra = Button(text="Tierra", font_size=30)
        self.BotonTierra.bind(on_press = self.Presionado)
        self.add_widget(self.BotonTierra)

    def Presionado(self, instance):
        sm.switch_to(PantallaEstrellas)

    def PresionadoEspace(self, instance):
        sm.switch_to(PantallaEspacio)

    def PresionadoMision(self, instance):
        sm.switch_to(PantallaMisiones)
    def PresionadoSateli(self, instance):
        sm.switch_to(PantallaSatelites)

sm = ScreenManager()


class Stars(App):
        def build(self):
            sm.add_widget(PantallaEstrellas(name='Estrellas'))
            sm.add_widget(PantallaGalaxias(name='Galaxias'))
            sm.add_widget(PantallaSistema(name='Sistema'))
            sm.add_widget(PantallaEspacio(name='Espacio'))
            return Grid()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   Stars().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
