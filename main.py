from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Load UI from .kv file
Builder.load_file("ui/main_screen.kv")

class MainScreen(Screen):
    pass

class PetQuestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        return sm

if __name__ == "__main__":
    PetQuestApp().run()
