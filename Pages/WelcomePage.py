from .LoginPage import LoginPage
from .PageMaker import PageMaker
from .RegisterPage import RegisterPage

import os


class WelcomePage(PageMaker):
    def __init__(self):
        # Initializing page length
        self.pageLen = 30

        # Initializing ui
        self.ui = self.drawUi()
        print(self.ui)

        # Handle Commands
        command = input('''Enter the number representing your comand:\n(ex. 1 - register -->> your input: 1)\n''')
        if command == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            registerPage = RegisterPage()
        elif command == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            loginPage = LoginPage()

    def drawUi(self):
        ui = ""
        ui += self.drawLine(self.pageLen)
        for i in range(3):
            ui += self.drawEndedLine(self.pageLen)
        ui += self.drawLineWithParameters(self.pageLen, "1 - register")
        ui += self.drawEndedLine(self.pageLen)
        ui += self.drawLineWithParameters(self.pageLen, "2 - login")
        for i in range(3):
            ui += self.drawEndedLine(self.pageLen)
        ui += self.drawLine(self.pageLen)
        return ui
