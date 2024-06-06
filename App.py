from Pages.WelcomePage import WelcomePage
import os

class App:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        welcomePage = WelcomePage()
