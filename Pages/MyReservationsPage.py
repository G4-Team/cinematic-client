from prompt_toolkit.shortcuts import message_dialog, input_dialog, yes_no_dialog
import os
import requests

from .PageMaker import PageMaker

class MyReservationsPage(PageMaker):
    def __init__(self):
        super().__init__()
        # Initializing page length
        self.pageLength = 50

        # Initializing varibales
        self.loadDb()

        # draw Ui 
        self.drawUi()

        # Handle Commands
        while(1):
            command = input("Enter the number representing your command:\n")
            if command == "10":
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            elif command == "11" and self.currentPage < (len(self.movieList) + 8) // 8:
                self.currentPage += 1

            elif command == "12" and self.currentPage > 1:
                self.currentPage -= 1

            elif command == "9":
                cancelReservation = input_dialog(title = "Cancel Reservation", 
                                        text = "Enter the number of the reservation you want to cancel:",
                                        style = self.dialogStyles).run()
                if cancelReservation is not None:
                    yesNo = yes_no_dialog(title = "Cancel Reservation",
                                      text = "Are you Sure you want to cancel resevation number " + cancelReservation,
                                      style = self.dialogStyles).run()
                    if yesNo:
                        message_dialog(title = "Cancel Reservation",
                                   text = "Reservation canceled successfuly!",
                                   style = self.dialogStyles).run()

            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()

    def drawUi(self):
        # Makeing sure the pageLength can contain everything 
        maxLen = 0
        for movie in self.movieList:
            maxLen = max(maxLen, len(movie['name']) + len(movie['date']) 
                + len(movie['capacityLeft']) + len(movie['price']))
        maxLen += 25
        self.pageLength = max(maxLen, self.pageLength)
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParametersStartAt(self.pageLength, 2, 'My Reservations')
        self.drawEndedLine(self.pageLength)
        self.drawMovieGrid(self.pageLength, self.movieList, self.currentPage)
        self.drawEndedLine(self.pageLength)
        # drawing next and previous page if needed
        if self.currentPage == 1:
            self.drawLineWithParameters(self.pageLength, '11 - Next')
        elif self.currentPage == (len(self.movieList) + 8 ) // 8:
            self.drawLineWithParameters(self.pageLength, '12 - Previous')
        else:
            self.drawLineWithParameters(self.pageLength, '12 - Previous', '11 - Next')
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '9 - Cancel', '10 - Back')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)

    def loadDb(self):
        self.currentPage = 1
        self.movieList = []
        request = requests.get()
