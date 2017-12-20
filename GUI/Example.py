import remi.gui as gui
from remi import start, App


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        b1 = gui.Button('Timer Config', width=210, height=25)

        tb = gui.TabBox(width='100%', height='100%')
        tb.add_tab(b1, 'Timer Config', None)

        b2 = gui.Button('Timer Status', width=210, height=25)
        tb.add_tab(b2, 'Timer Status', None)

        b3 = gui.Button('Show first tab', width=210, height=25)
        tb.add_tab(b3, 'Third', None)

        b1.set_on_click_listener(self.on_bt1_pressed, tb, b2)
        b2.set_on_click_listener(self.on_bt2_pressed, tb, 'Third')
        b3.set_on_click_listener(self.on_bt3_pressed, tb, 0)

        return tb

    def on_bt1_pressed(self, widget, tabbox, refWidgetTab):
        tabbox.select_by_widget(refWidgetTab)

    def on_bt2_pressed(self, widget, tabbox, refWidgetTabName):
        tabbox.select_by_name(refWidgetTabName)

    def on_bt3_pressed(self, widget, tabbox, tabIndex):
        tabbox.select_by_index(tabIndex)


if __name__ == "__main__":
    start(MyApp, address='192.168.7.224', port=8081, multiple_instance=False, enable_file_cache=True, update_interval=0.1, start_browser=True, title="Tab Demo", standalone=False)