import kivy.app
from kivy.uix.button import Button
class NewApp(kivy.app.App):
    def build(self):
        return Button(text='Hello Berlin')
app = NewApp(title="Hello")
app.run()
