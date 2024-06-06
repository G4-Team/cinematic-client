import os
from prompt_toolkit.shortcuts import input_dialog

from .PageMaker import PageMaker
from .LoginPage import LoginPage


class RegisterPage(PageMaker):
    def __init__(self):
        super().__init__()
        # Initializing page length
        self.pageLength = 40

        # Initializing variables
        self.username = ""
        self.email = ""
        self.phoneNumber = ""
        self.password = ""
        self.confirmPassword = ""
        self.birthdate = ""

        # Drawing Ui 
        ui = self.drawUi()
        print(ui)

        # Handle commands
        while(1):
            command = input("Enter the number representing your command\n")
            if command == "1":
                self.username = input_dialog(title = "Username", text = "Enter your username:",
                                             style = self.dialogStyles).run() 
                os.system('cls' if os.name == 'nt' else 'clear')
                ui = self.drawUi()
                print(ui)
            elif command == "2":
                self.email = input_dialog(title = "Email", text = "Enter your Email:", 
                                          style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                ui = self.drawUi()
                print(ui)
            elif command == "3":
                self.phoneNumber = input_dialog(title = "Phone number", 
                                                text = "Enter your Phone number:",
                                                style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                ui = self.drawUi()
                print(ui)
            elif command == "4":
                self.password = input_dialog(title = "Password", 
                                             text = "Enter your Password:", 
                                             password = True,
                                             style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                ui = self.drawUi()
                print(ui)
            elif command == "5":
                self.confirmPassword = input_dialog(title = "Confirm Password", 
                                                    text = "Enter your Password again:",
                                                    password = True,
                                                    style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                ui = self.drawUi()
                print(ui)
            elif command == "6":
                self.birthdate = input_dialog(title = "Birthdate", 
                                              text = "Enter your Birthdate:\n(ex. yyyy/mm/dd)",
                                              style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                ui = self.drawUi()
                print(ui)
            elif command == "7":
                # replace with checking if the credentials are valid and registering the user
                if True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    loginPage = LoginPage()


    def drawUi(self):
        self.pageLength = max([self.pageLength, 
                                len(self.username) + 27, 
                                len(self.email) + 20,
                                len(self.password) + 27,
                                len(self.phoneNumber) + 35,
                                len(self.confirmPassword) + 45,
                                len(self.birthdate) + 28])
        ui = self.drawLine(self.pageLength)
        ui += self.drawEndedLine(self.pageLength)
        # drawing username
        if self.username != "":
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username', ':', 
                                                     self.username)
        else:
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username') 

        # drawing email
        if self.email != "":
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Email', ':', 
                                                     self.email)
        else:
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Email') 
        
        # drawing phone number
        if self.phoneNumber != "":
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - Phone number', ':', 
                                                     self.phoneNumber)
        else:
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - Phone number') 

        # drawing password
        if self.password != "":
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - Password', ':', 
                                                     len(self.password) * "*")
        else:
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - Password') 

        # drawing confirm password
        if self.confirmPassword != "":
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '5 - Confirm Password', ':', 
                                                     len(self.confirmPassword) * "*")
        else:
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '5 - Confirm password')

        # drawing birthdate
        if self.birthdate != "":
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '6 - Birthdate', ':', 
                                                     self.birthdate)
        else:
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '6 - Birthdate')

        ui += self.drawEndedLine(self.pageLength)
        ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '7 - Confirm')
        ui += self.drawEndedLine(self.pageLength)
        ui += self.drawLine(self.pageLength)
        return ui
