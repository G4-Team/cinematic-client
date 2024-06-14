import os
from http import cookiejar

from .LoginPage import LoginPage
from .PageMaker import PageMaker
from .ProfilePage import ProfilePage
from .RegisterPage import RegisterPage


class WelcomePage(PageMaker):
    def __init__(self):
        # Initializing page length
        self.pageLen = 30

        # Initializing ui
        self.drawUi()

        # Handle Commands
        while 1:
            command = input(
                    """Enter the number representing your comand:\n(ex. 1 - register -->> your input: 1)\n"""
            )
            if command == "1":
                os.system("cls" if os.name == "nt" else "clear")
                registerPage = RegisterPage()

            elif command == "2":
                os.system("cls" if os.name == "nt" else "clear")
                loginPage = LoginPage()

            os.system("cls" if os.name == "nt" else "clear")
            self.drawUi()

    def drawUi(self):
        self.drawLine(self.pageLen)
        for i in range(3):
            self.drawEndedLine(self.pageLen)
        self.drawLineWithParameters(self.pageLen, "1 - register")
        self.drawEndedLine(self.pageLen)
        self.drawLineWithParameters(self.pageLen, "2 - login")
        for i in range(3):
            self.drawEndedLine(self.pageLen)
        self.drawLine(self.pageLen)
