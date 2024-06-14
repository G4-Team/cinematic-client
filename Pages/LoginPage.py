from prompt_toolkit.shortcuts import input_dialog, message_dialog
import requests
import os


from .PageMaker import PageMaker
from .ProfilePage import ProfilePage
from .AdminProfilePage import AdminProfilePage

class LoginPage(PageMaker):
    def __init__(self):
        super().__init__()
        # Initializing page length
        self.pageLength = 40

        # Initializing variables
        self.username = ""
        self.password = ""

        # Drawing Ui 
        self.drawUi()

        # Handle commands
        while(1):
            command = input("Enter the number representing your command:\n")
            if command == "1":
                self.username = input_dialog(title = "Username", text = "Enter your username:",
                                             style = self.dialogStyles).run() 
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "2":
                self.password = input_dialog(title = "Password", 
                                             text = "Enter your Password:", 
                                             password = True,
                                             style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "3":
                request = requests.post("http://127.0.0.1:8000/users/login/", json = {
                    "username": self.username,
                    "password": self.password})
                if request.status_code == 200:
                    self.save_cookies(request.cookies)
                    message_dialog(title = "Success",
                                   text = request.json()['message'],
                                   style = self.dialogStyles).run()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if request.json()['is_admin']:
                        adminProfilePage = AdminProfilePage(request.json()['user_id'])
                    else:
                        profilePage = ProfilePage(request.json()['user_id'])
                    break
                else:
                    message_dialog(title = "Error",
                                   text = request.json()['message'],
                                   style = self.dialogStyles).run()
            elif command == "4":
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()


    def drawUi(self):
        self.pageLength = max([self.pageLength, 
                                len(self.username) + 27, 
                                len(self.password) + 27])
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        # drawing username
        if self.username != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username', ':', 
                                                     self.username)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username') 

        # drawing password
        if self.password != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Password', ':', 
                                                     len(self.password) * "*")
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Password') 

        self.drawEndedLine(self.pageLength)
        self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - Confirm')
        self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - Back')
        self.drawEndedLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
