from kivy.uix.screenmanager import Screen, SlideTransition


class Register(Screen):
    def do_register(self, usernameText, passwordText):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()
