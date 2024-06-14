import os
from prompt_toolkit.shortcuts import input_dialog, message_dialog
import requests

from .PageMaker import PageMaker


class AddShowtimePage(PageMaker):
    def __init__(self):
        super().__init__()
        # Initializing page length
        self.pageLength = 40

        # Initializing variables
        self.cinemaName = None
        self.time = None
        self.movieName = None
        self.movieAgeRating = None

        # Drawing Ui 
        self.drawUi()

        # Handle commands
        while(1):
            command = input("Enter the number representing your command:\n")
            if command == "1":
                self.cinemaName = input_dialog(title = "Cinema Name", text = "Enter cinema name:",
                                             style = self.dialogStyles).run() 
                if self.cinemaName == "":
                    self.cinemaName = None

            elif command == "2":
                self.time = input_dialog(title = "Time", text = "Enter time:(ex. yyyy-mm-dd hh:mm)", 
                                          style = self.dialogStyles).run()
                if self.time == "":
                    self.time = None

            elif command == "3":
                self.movieName = input_dialog(title = "Movie Name", text = "Enter Movie name:", 
                                          style = self.dialogStyles).run()
                if self.movieName == "":
                    self.movieName = None

            elif command == "4":
                self.movieAgeRating = input_dialog(title = "Movie Age Rating", 
                                             text = "Enter Movie age rating:", 
                                             style = self.dialogStyles).run()
                if self.movieAgeRating == "":
                    self.movieAgeRating = None
                try:
                    self.movieAgeRating = int(self.movieAgeRating)
                except:
                    if self.movieAgeRating is not None:
                        message_dialog(title = "Error",
                                   text = "movie age rating should be number",
                                   style = self.dialogStyles).run()
                    self.movieAgeRating = None

            elif command == "6":
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            elif command == "5":
                try:
                    payload = {}
                    if self.cinemaName is not None:
                        payload['cinema_name'] = self.cinemaName
                    if self.time is not None:
                        payload['time'] = self.time 
                    if self.movieName is not None:
                        payload['movie_name'] = self.movieName
                    if self.movieAgeRating is not None:
                        payload['movie_age_rating'] = self.movieAgeRating
                    request = requests.post(self.url + "cinema/add-showtime/", cookies = self.get_cookies(), json = payload)
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

                except:
                    message_dialog(title = "Error",
                                   text = "Server not responding",
                                   style = self.dialogStyles).run()
            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()

    def drawUi(self):
        self.pageLength = max([self.pageLength, 
                                len(str(self.cinemaName)) + 20, 
                                len(str(self.time)) + 20,
                                len(str(self.movieAgeRating)) + 40,
                                len(str(self.movieName)) + 25])
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)

        # drawing cinema name
        if self.cinemaName is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Cinema Name', ':', 
                                                     self.cinemaName)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Cinema Name') 

        # drawing time
        if self.time is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Time', ':', 
                                                     str(self.time))
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Time') 
        
        # drawing movie name 
        if self.movieName is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - Movie Name', ':', 
                                                     str(self.movieName))
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - Movie Name') 

        # drawing movie age rating
        if self.movieAgeRating is not None:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - Movie Age Rating', ':', 
                                                     str(self.movieAgeRating))
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - Movie Age Rating') 

        self.drawEndedLine(self.pageLength)
        self.drawLineWithParametersStartAt(self.pageLength, 2, '5 - Confirm')
        self.drawLineWithParametersStartAt(self.pageLength, 2, '6 - Back')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
