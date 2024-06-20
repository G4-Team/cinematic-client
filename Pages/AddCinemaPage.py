import os

import requests
from prompt_toolkit.shortcuts import input_dialog, message_dialog

from .PageMaker import PageMaker


class AddCinemaPage(PageMaker):
    def __init__(self):
        super().__init__()
        # Initializing page length
        self.pageLength = 40

        # Initializing variables
        self.name = None
        self.ticketPrice = None
        self.capacity = None
        self.row = None
        self.column = None

        # Drawing Ui
        self.drawUi()

        # Handle commands
        while 1:
            command = input("Enter the number representing your command:\n")
            if command == "1":
                self.name = input_dialog(
                    title="Name", text="Enter cinema name:", style=self.dialogStyles
                ).run()
                if self.name == "":
                    self.name = None

            elif command == "2":
                self.ticketPrice = input_dialog(
                    title="Ticket Price",
                    text="Enter Ticket price:",
                    style=self.dialogStyles,
                ).run()
                if self.ticketPrice == "":
                    self.ticketPrice = None
                try:
                    self.ticketPrice = int(self.ticketPrice)
                except:
                    if self.ticketPrice is not None:
                        message_dialog(
                            title="Error",
                            text="ticket price should be number",
                            style=self.dialogStyles,
                        ).run()
                    self.ticketPrice = None

            elif command == "3":
                self.row = input_dialog(
                    title="Row",
                    text="Enter The number of rows:",
                    style=self.dialogStyles,
                ).run()
                if self.row == "":
                    self.row = None
                try:
                    self.row = int(self.row)
                except:
                    if self.row is not None:
                        message_dialog(
                            title="Error",
                            text="row should be number",
                            style=self.dialogStyles,
                        ).run()
                    self.row = None

            elif command == "4":
                self.column = input_dialog(
                    title="Column",
                    text="Enter the number of columns:",
                    style=self.dialogStyles,
                ).run()
                if self.column == "":
                    self.column = None
                try:
                    self.column = int(self.column)
                except:
                    if self.column is not None:
                        message_dialog(
                            title="Error",
                            text="column should be number",
                            style=self.dialogStyles,
                        ).run()
                    self.column = None

            elif command == "6":
                os.system("cls" if os.name == "nt" else "clear")
                break

            elif command == "5":
                try:
                    payload = {}
                    if self.name is not None:
                        payload["name"] = self.name
                    if self.ticketPrice is not None:
                        payload["ticket_price"] = self.ticketPrice
                    if self.row is not None:
                        payload["number_of_row"] = self.row
                    if self.column is not None:
                        payload["number_of_col"] = self.column
                    if self.column is not None and self.row is not None:
                        payload["capacity"] = self.row * self.column
                    request = requests.post(
                        self.url + "cinema/add-cinema/",
                        cookies=self.get_cookies(),
                        json=payload,
                    )
                    if request.status_code == 201:
                        message_dialog(
                            title="Success",
                            text=request.json()["message"],
                            style=self.dialogStyles,
                        ).run()
                        os.system("cls" if os.name == "nt" else "clear")
                        break
                    else:
                        message_dialog(
                            title="Error",
                            text=request.json()["message"],
                            style=self.dialogStyles,
                        ).run()
                except:
                    message_dialog(
                        title="Error",
                        text="Server not reponding",
                        style=self.dialogStyles,
                    ).run()

            os.system("cls" if os.name == "nt" else "clear")
            self.drawUi()

    def drawUi(self):
        self.pageLength = max(
            [
                self.pageLength,
                len(str(self.name)) + 20,
                len(str(self.ticketPrice)) + 20,
                len(str(self.row)) + 20,
                len(str(self.column)) + 35,
            ]
        )
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)

        # drawing name
        if self.name is not None:
            self.drawLineWithParametersStartAt(
                self.pageLength, 2, "1 - Name", ":", self.name
            )
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, "1 - Name")

        # drawing ticketPrice
        if self.ticketPrice is not None:
            self.drawLineWithParametersStartAt(
                self.pageLength, 2, "2 - Ticket Price", ":", str(self.ticketPrice)
            )
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, "2 - Ticket Price")

        # drawing row
        if self.row is not None:
            self.drawLineWithParametersStartAt(
                self.pageLength, 2, "3 - Row", ":", str(self.row)
            )
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, "3 - Row")

        # drawing columns
        if self.column is not None:
            self.drawLineWithParametersStartAt(
                self.pageLength, 2, "4 - Columns", ":", str(self.column)
            )
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, "4 - Columns")

        self.drawEndedLine(self.pageLength)
        self.drawLineWithParametersStartAt(self.pageLength, 2, "5 - Confirm")
        self.drawLineWithParametersStartAt(self.pageLength, 2, "6 - Back")
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
