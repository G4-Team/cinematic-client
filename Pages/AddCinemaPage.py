import os
from prompt_toolkit.shortcuts import input_dialog, message_dialog
import requests

from .PageMaker import PageMaker


class AddCinemaPage(PageMaker):
    def __init__(self):
        super().__init__()
        # Initializing page length
        self.pageLength = 40

        # Initializing variables
        self.name = ""
        self.ticketPrice = ""
        self.capacity = ""
        self.row = ""
        self.column = ""

        # Drawing Ui 
        self.drawUi()

        # Handle commands
        while(1):
            command = input("Enter the number representing your command:\n")
            if command == "1":
                self.name = input_dialog(title = "Name", text = "Enter cinema name:",
                                             style = self.dialogStyles).run() 
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "2":
                self.ticketPrice = input_dialog(title = "Ticket Price", text = "Enter Ticket price:", 
                                          style = self.dialogStyles).run()
                try:
                    self.ticketPrice = int(self.ticketPrice)
                except:
                    message_dialog(title = "Error",
                                   text = "ticket price should be number",
                                   style = self.dialogStyles).run()
                    self.ticketPrice = ""
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "3":
                self.row = input_dialog(title = "Row", text = "Enter The number of rows:", 
                                          style = self.dialogStyles).run()
                try:
                    self.row = int(self.row)
                except:
                    message_dialog(title = "Error",
                                   text = "row should be number",
                                   style = self.dialogStyles).run()
                    self.row = ""
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()

            elif command == "4":
                self.column = input_dialog(title = "Column", 
                                             text = "Enter the number of columns:", 
                                             style = self.dialogStyles).run()
                try:
                    self.column = int(self.column)
                except:
                    message_dialog(title = "Error",
                                   text = "column should be number",
                                   style = self.dialogStyles).run()
                    self.column = ""

                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "6":
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            elif command == "5":
                request = requests.post(self.url + "cinema/add-cinema/", cookies = self.get_cookies(), json = {
                    "name": self.name,
                    "ticket_price": self.ticketPrice,
                    "capacity": self.row * self.column,
                    "number_of_row": self.row,
                    "number_of_col": self.column})

                if request.status_code == 201:
                    message_dialog(title = "Success",
                                   text = request.json()['message'],
                                   style = self.dialogStyles).run()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    message_dialog(title = "Error",
                                   text = request.json()['message'],
                                   style = self.dialogStyles).run()

            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()



    def drawUi(self):
        self.pageLength = max([self.pageLength, 
                                len(self.name) + 20, 
                                len(str(self.ticketPrice)) + 20,
                                len(str(self.row)) + 20,
                                len(str(self.column)) + 35])
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)

        # drawing name
        if self.name != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Name', ':', 
                                                     self.name)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Name') 

        # drawing ticketPrice
        if self.ticketPrice != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Ticket Price', ':', 
                                                     str(self.ticketPrice))
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Ticket Price') 
        
        # drawing row
        if self.row != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - Row', ':', 
                                                     str(self.row))
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - Row') 

        # drawing columns
        if self.column != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - Columns', ':', 
                                                     str(self.column))
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - Columns') 

        self.drawEndedLine(self.pageLength)
        self.drawLineWithParametersStartAt(self.pageLength, 2, '5 - Confirm')
        self.drawLineWithParametersStartAt(self.pageLength, 2, '6 - Back')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
