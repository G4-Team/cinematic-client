from prompt_toolkit.shortcuts import input_dialog
import os

from .PageMaker import PageMaker

class LoginPage(PageMaker):
    def __init__(self):
        super().__init__()
        # Initializing page length
        self.pageLength = 40

        # Initializing variables
        self.username = ""
        self.password = ""

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
                self.password = input_dialog(title = "Password", 
                                             text = "Enter your Password:", 
                                             password = True,
                                             style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                ui = self.drawUi()
                print(ui)
            elif command == "3":
                # replace with checking if the user exists
                if True:
                    pass
                    #profilePage = ProfilePage()

    def drawUi(self):
        self.pageLength = max([self.pageLength, 
                                len(self.username) + 27, 
                                len(self.password) + 27])
        ui = self.drawLine(self.pageLength)
        ui += self.drawEndedLine(self.pageLength)
        ui += self.drawEndedLine(self.pageLength)
        # drawing username
        if self.username != "":
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username', ':', 
                                                     self.username)
        else:
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Username') 

        # drawing password
        if self.password != "":
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Password', ':', 
                                                     len(self.password) * "*")
        else:
            ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Password') 

        ui += self.drawEndedLine(self.pageLength)
        ui += self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - Confirm')
        ui += self.drawEndedLine(self.pageLength)
        ui += self.drawEndedLine(self.pageLength)
        ui += self.drawLine(self.pageLength)
        return ui
