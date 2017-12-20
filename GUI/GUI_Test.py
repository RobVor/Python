import remi.gui as gui
from remi import start, App

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width = 120, height = 120)
        self.lbl = gui.Label('Hello world!')
        self.bt = gui.Button('Press me!')
        self.btb = gui.Button('Back one...')

        # setting the listener for the onclick event of the button
        self.bt.set_on_click_listener(self.on_button_pressed)

        # appending a widget to another, the first argument is a string key
        container.append(self.lbl)
        container.append(self.bt)
        container.append(self.btb)

        # returning the root widget
        return container

    # listener function
    def on_button_pressed(self, widget):
        self.lbl.set_text('Button pressed!')
        self.bt.set_text('Hi!')
        self.btb.set_on_click_listener()

# starts the webserver
start(MyApp, address='192.168.7.224', port=8081, multiple_instance=False, enable_file_cache=True, update_interval=0.1, start_browser=False)