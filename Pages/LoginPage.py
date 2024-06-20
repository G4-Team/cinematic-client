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
        self.username = None
        self.password = None

        # Drawing Ui 
        self.drawUi()

        # Handle commands
        while(1):
            command = input("Enter the number representing your command:\n")
            if command == "1":
                self.username = input_dialog(title = "Username", text = "Enter your username:",
                                             style = self.dialogStyles).run() 
                if self.username == "":
                    self.username = None
            elif command == "2":
                self.password = input_dialog(title = "Password", 
                                             text = "Enter your Password:", 
                                             password = True,
                                             style = self.dialogStyles).run()
                if self.password == "":
                    self.password = None
            elif command == "3":
                try:
                    payload = {}
                    if self.username is not None:
                        payload['username'] = self.username
                    if self.password is not None:
                        payload['password'] = self.password
                    request = requests.post(self.url + "/users/login/", json = payload)
                    out = request.json()
                except:
                    message_dialog(title = "Error",
                                   text = "Server not responding ",
                                   style = self.dialogStyles).run()

                if request.status_code == 200:
                    self.save_cookies(request.cookies)
                    message_dialog(title = "Success",
                                   text = request.json()['message'],
                                   style = self.dialogStyles).run()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if out['is_admin']:
                        adminProfilePage = AdminProfilePage(out['user_id'])
                    else:
                        profilePage = ProfilePage(out['user_id'])
                    break
                else:
                    message_dialog(title = "Error",
                                   text = out['message'],
                                   style = self.dialogStyles).run()
            elif command == "4":
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()


    def drawUi(self):
        self.pageLength = max([self.pageLength, 
                                len(str(self.username)) + 27, 
                                len(str(self.password)) + 27])
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        # drawing username
        if self.username is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username', ':', 
                                                     self.username)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username') 

        # drawing password
        if self.password is not None:
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
