import os
from prompt_toolkit.shortcuts import input_dialog, message_dialog
import requests

from .PageMaker import PageMaker
from .LoginPage import LoginPage


class RegisterPage(PageMaker):
    def __init__(self):
        super().__init__()
        # Initializing page length
        self.pageLength = 40

        # Initializing variables
        self.username = None
        self.email = None
        self.phoneNumber = None
        self.password = None
        self.confirmPassword = None
        self.birthdate = None

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
                self.email = input_dialog(title = "Email", text = "Enter your Email:", 
                                          style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "3":
                self.phoneNumber = input_dialog(title = "Phone number", 
                                                text = "Enter your Phone number:",
                                                style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "4":
                self.password = input_dialog(title = "Password", 
                                             text = "Enter your Password:", 
                                             password = True,
                                             style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "5":
                self.confirmPassword = input_dialog(title = "Confirm Password", 
                                                    text = "Enter your Password again:",
                                                    password = True,
                                                    style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "6":
                self.birthdate = input_dialog(title = "Birthdate", 
                                              text = "Enter your Birthdate:\n(ex. yyyy/mm/dd)",
                                              style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "8":
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            elif command == "7":
                try:
                    payload = {}
                    if self.username is not None:
                        payload['username'] = self.username
                    if self.email is not None:
                        payload['email'] = self.email
                    if self.phoneNumber is not None:
                        payload['phone'] = self.phoneNumber
                    if self.password is not None:
                        payload['password'] = self.password
                    if self.confirmPassword is not None:
                        payload['confirm_password'] = self.confirmPassword
                    if self.birthdate is not None:
                        payload['birthday'] = self.birthdate
                    request = requests.post("http://127.0.0.1:8000/users/register/", json = payload)
                    out = request.json()
                except:
                    message_dialog(title = "Error",
                                   text = "Server Not Responding",
                                   style = self.dialogStyle).run()
                if request.status_code == 201:
                    message_dialog(title = "Success",
                                   text = out['message'],
                                   style = self.dialogStyles).run()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    loginPage = LoginPage()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    message_dialog(title = "Error",
                                   text = out['message'],
                                   style = self.dialogStyles).run()

            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()



    def drawUi(self):
        self.pageLength = max([self.pageLength, 
                                len(str(self.username)) + 27, 
                                len(str(self.email)) + 20,
                                len(str(self.password)) + 27,
                                len(str(self.phoneNumber)) + 35,
                                len(str(self.confirmPassword)) + 45,
                                len(str(self.birthdate)) + 28])
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        # drawing username
        if self.username is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username*', ':', 
                                                     self.username)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username*') 

        # drawing email
        if self.email is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Email*', ':', 
                                                     self.email)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Email*') 
        
        # drawing phone number
        if self.phoneNumber is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - Phone number', ':', 
                                                     self.phoneNumber)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - Phone number') 

        # drawing password
        if self.password is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - Password*', ':', 
                                                     len(self.password) * "*")
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - Password*') 

        # drawing confirm password
        if self.confirmPassword is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '5 - Confirm Password*', ':', 
                                                     len(self.confirmPassword) * "*")
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '5 - Confirm password*')

        # drawing birthdate
        if self.birthdate is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '6 - Birthdate*', ':', 
                                                     self.birthdate)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '6 - Birthdate*')

        self.drawEndedLine(self.pageLength)
        self.drawLineWithParametersStartAt(self.pageLength, 2, '7 - Confirm')
        self.drawLineWithParametersStartAt(self.pageLength, 2, '8 - Back')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
