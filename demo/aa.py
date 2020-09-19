from kivy.app import App
from kivy.lang import Builder


root = Builder.load_string('''
BoxLayout:
    id: bl
    orientation: 'vertical'
    padding: 10, 10
    row_default_height: '48dp'
    row_force_default: True
    spacing: 10, 10

    GridLayout:
        id: layout_content
        cols: 1
        row_default_height: '20dp'
        row_force_default: True
        spacing: 0, 0
        padding: 0, 0

        Label:
            text: 'You don''t have any downloads. Please add new download from Home screen'
''')

class MainApp(App):

    def build(self):
        return root

if __name__ == '__main__':
    MainApp().run()