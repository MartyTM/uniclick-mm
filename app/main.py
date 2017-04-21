from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

from connected import Connected
from register import Register


class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        print(app.username)

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'

    def resetForm(self):
        self.ids['username'].text = ""
        self.ids['password'].text = ""

    def go_to_register(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'register'


class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        manager.add_widget(Register(name='register'))

        return manager


if __name__ == '__main__':
    LoginApp().run()
