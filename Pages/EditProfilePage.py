from prompt_toolkit.shortcuts import input_dialog, message_dialog
import os
import requests

from .PageMaker import PageMaker

class EditProfilePage(PageMaker):
    def __init__(self, user_id):
        super().__init__()
        # Initializing page lenght
        self.pageLength = 40

        # Initializing variables
        self.loadDb()

        # draw ui 
        self.drawUi()

        # Handle command
        while(1):
            command = input("Enter the number representing your command:\n")
            if command == "1":
                self.username = input_dialog(title = "Username", text = "Enter your username:",
                                             style = self.dialogStyles).run() 
                if self.username == "":
                    self.username = None

            elif command == "2":
                self.email = input_dialog(title = "Email", text = "Enter your Email:", 
                                          style = self.dialogStyles).run()
                if self.email == "":
                    self.email = None

            elif command == "3":
                self.phoneNumber = input_dialog(title = "Phone number", 
                                                text = "Enter your Phone number:",
                                                style = self.dialogStyles).run()
                if self.phoneNumber == "":
                    self.phoneNumber = None

            elif command == "5":
                self.newPassword = input_dialog(title = "New Password", 
                                             text = "Enter your new Password:", 
                                             password = True,
                                             style = self.dialogStyles).run()
                if self.newPassword == "":
                    self.newPassword = None

            elif command == "6":
                self.confirmNewPassword = input_dialog(title = "Confirm New Password", 
                                                    text = "Enter your New Password again:",
                                                    password = True,
                                                    style = self.dialogStyles).run()
                if self.confirmNewPassword == "":
                    self.confirmNewPassword = None
            elif command == "4":
                self.birthdate = input_dialog(title = "Birthdate", 
                                              text = "Enter your Birthdate:\n(ex. yyyy-mm-dd)",
                                              style = self.dialogStyles).run()
                if self.birthdate == "":
                    self.birthdate = None

            elif command == "7": 
                self.password = input_dialog(title = "Password", 
                                             text = "Enter your Current Password:", 
                                             password = True,
                                             style = self.dialogStyles).run()
                if self.password == "":
                    self.password = None
            elif command == '9':
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            elif command == "8":
                payloadProfile = {}
                payloadPassword = {}
                if self.username is not None:
                    payloadProfile['username'] = self.username
                if self.email is not None:
                    payloadProfile['email'] = self.email
                if self.phoneNumber is not None:
                    payloadProfile['phone'] = self.phoneNumber
                if self.birthdate is not None:
                    payloadProfile['birthday'] = self.birthdate
                if self.password is not None:
                    payloadPassword['old_password'] = self.password
                if self.confirmNewPassword is not None:
                    payloadPassword['confirm_password'] = self.confirmNewPassword
                if self.newPassword is not None:
                    payloadPassword['password'] = self.newPassword
                if payloadProfile:
                    try:
                        requestProfile = requests.put(self.url + 'users/change-profile/' + str(user_id) + '/', json = payloadProfile,
                                                  cookies = self.get_cookies())
                        if requestProfile.status_code == 200:
                            message_dialog(title = "Success", text = requestProfile.json()['message'],
                               style = self.dialogStyles).run()
                        else:
                            message_dialog(title = "Error", text = requestProfile.json()['message'],
                               style = self.dialogStyles).run()
                    except:
                        message_dialog(title = "Error",
                                       text = "Server not responding",
                                       style = self.dialogStyles).run()

                if payloadPassword:
                    try:
                        requestPassword = requests.put(self.url + 'users/change-password/' + str(user_id) + '/',
                                                   json = payloadPassword,
                                                   cookies = self.get_cookies())
                        if requestPassword.status_code == 200:
                            message_dialog(title = "Success", text = requestPassword.json()['message'],
                               style = self.dialogStyles).run()
                        else:
                            message_dialog(title = "Error", text = requestPassword.json()['message'],
                               style = self.dialogStyles).run()
                    except:
                        message_dialog(title = "Error",
                                       text = "Server not responding",
                                       style = self.dialogStyles).run()

                break
            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()


    def loadDb(self):
        self.username = None
        self.email = None
        self.phoneNumber = None
        self.birthdate = None
        self.newPassword = None
        self.confirmNewPassword = None
        self.password = None

    def drawUi(self):
        # makeing sure page can contain all content
        self.pageLength = max([self.pageLength, len(str(self.username)) + 25,
                              len(str(self.email)) + 30,
                              len(str(self.phoneNumber)) + 30,
                              len(str(self.birthdate)) + 30,
                              len(str(self.password)) + 30,
                              len(str(self.confirmNewPassword)) + 35,
                              len(str(self.newPassword)) + 30])
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        # drawing username
        if self.username is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username', ':', 
                                                     self.username)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username') 

        # drawing email
        if self.email is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Email', ':', 
                                                     self.email)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Email') 
        
        # drawing phone number
        if self.phoneNumber is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - Phone number', ':', 
                                                     self.phoneNumber)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - Phone number') 


        # drawing birthdate
        if self.birthdate is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - Birthdate', ':', 
                                                     self.birthdate)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - Birthdate')

        self.drawEndedLine(self.pageLength)

        # drawing new password
        if self.newPassword is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '5 - New Password', ':', 
                                                     len(self.newPassword) * "*")
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '5 - New Password') 

        # drawing confirm new password
        if self.confirmNewPassword is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '6 - Confirm New Password', ':',
                                                     len(self.confirmNewPassword) * "*")
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '6 - Confirm New password')
        # drawing password
        if self.password is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '7 - Password', ':', 
                                                     len(self.password) * "*")
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '7 - Password') 

        self.drawEndedLine(self.pageLength)
        self.drawLineWithParametersStartAt(self.pageLength, 2, '8 - Confirm')
        self.drawLineWithParametersStartAt(self.pageLength, 2, '9 - Back')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
