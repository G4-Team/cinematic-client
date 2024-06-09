from prompt_toolkit.shortcuts import input_dialog, message_dialog
import os

from .PageMaker import PageMaker

class EditAdminProfilePage(PageMaker):
    def __init__(self):
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
                self.newPassword = input_dialog(title = "New Password", 
                                             text = "Enter your new Password:", 
                                             password = True,
                                             style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "5":
                self.confirmNewPassword = input_dialog(title = "Confirm New Password", 
                                                    text = "Enter your New Password again:",
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
            elif command == "7": 
                self.password = input_dialog(title = "Password", 
                                             text = "Enter your Current Password:", 
                                             password = True,
                                             style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "8":
                message_dialog(title = "Info", text = "Profile Updated successfully!",
                               style = self.dialogStyles).run()
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()


    def loadDb(self):
        self.username = ""
        self.email = ""
        self.phoneNumber = ""
        self.birthdate = ""
        self.newPassword = ""
        self.confirmNewPassword = ""
        self.password = ""

    def drawUi(self):
        # makeing sure page can contain all content
        self.pageLenght = max([self.pageLength, len(self.username) + 20,
                              len(self.email) + 20,
                              len(self.phoneNumber) + 20,
                              len(self.birthdate) + 20,
                              len(self.password) + 20,
                              len(self.confirmNewPassword) + 20,
                              len(self.newPassword) + 20])
        self.drawLine(self.pageLenght)
        self.drawEndedLine(self.pageLength)
        # drawing username
        if self.username != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username', ':', 
                                                     self.username)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username') 

        # drawing email
        if self.email != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Email', ':', 
                                                     self.email)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Email') 
        
        # drawing phone number
        if self.phoneNumber != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - Phone number', ':', 
                                                     self.phoneNumber)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - Phone number') 

        # drawing new password
        if self.newPassword != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - New Password', ':', 
                                                     len(self.newPassword) * "*")
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - New Password') 

        # drawing confirm new password
        if self.confirmNewPassword != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '5 - Confirm New Password', ':',
                                                     len(self.confirmNewPassword) * "*")
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '5 - Confirm New password')

        # drawing birthdate
        if self.birthdate != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '6 - Birthdate', ':', 
                                                     self.birthdate)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '6 - Birthdate')

        self.drawEndedLine(self.pageLength)
        # drawing password
        if self.password != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '7 - Password', ':', 
                                                     len(self.password) * "*")
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '7 - Password') 

        self.drawLineWithParametersStartAt(self.pageLength, 2, '8 - Confirm')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
