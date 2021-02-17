from kivy.lang.builder import Builder
from page_controller import PageController
from kivy.app import App


page_controller = PageController()

class WaterMarkerApp(App):
    def build(self):
        return page_controller

        
if __name__ == "__main__":
    WaterMarkerApp().run()