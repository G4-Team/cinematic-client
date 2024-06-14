from prompt_toolkit.shortcuts import input_dialog, yes_no_dialog, message_dialog
import os
import requests

from .PageMaker import PageMaker
from .CommentsPage import CommentsPage

class ShowtimeDetailsPage(PageMaker):
    def __init__(self, showtime, user_id):
        super().__init__()
        # Initializing page length
        self.pageLength = 40

        # Initializing varibales
        self.showtime = showtime
        self.loadDb(showtime['id'])

        # Draw Ui 
        self.drawUi()

        # Handle Commands
        while(1):
            command = input("Enter the number representing your command:\n")
            if command == "1":
                self.selectedRow = input_dialog(title = "Row",
                                        text = "Enter row:",
                                        style = self.dialogStyles).run()
                self.selectedCol = input_dialog(title = "Column",
                                                text = "Enter column:",
                                                style = self.dialogStyles).run()
                if self.selectedRow is None or self.selectedCol is None or self.selectedRow == "" or self.selectedCol == "":
                    message_dialog(title = "Error",
                                   text = "Row or Col cant be empty",
                                   style = self.dialogStyles).run()
                    continue
                yesNo = yes_no_dialog(title = "Confirm",
                                      text = "Are you sure you want to reserve seat" + self.selectedRow + ' ' + self.selectedCol + "?",
                                      style = self.dialogStyles).run()
                if yesNo:
                    try:
                        request = requests.post(self.url + 'cinema/reserve/' + str(user_id) + '/' + 
                            str(self.getId(self.selectedRow, self.selectedCol)) + '/',
                                            cookies = self.get_cookies())
                        if request.status_code == 200:
                            message_dialog(title = "Success",
                                       text = request.json()['message'],
                                       style = self.dialogStyles).run()
                            self.loadDb(showtime['id'])

                        else:
                            message_dialog(title = "Error",
                                       text = request.json()['message'],
                                       style = self.dialogStyles).run()
                    except:
                        message_dialog(title = "Error",
                                       text = "Server not responding",
                                       style = self.dialogStyles).run()
            if command == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                commentsPage = CommentsPage(user_id, showtime['movie']['movie_id'])
                self.loadDb(showtime['id'])

            if command == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()
                

            
    def loadDb(self, showtime_id):
        try:
            request = requests.get(self.url + 'cinema/showtime-seats/' + str(showtime_id) + '/',
                               cookies = self.get_cookies())
            self.row = 0
            self.col = 0
            self.seatsRaw = request.json()['seats']
            for key, value in request.json()['seats'].items():
                self.row = max(self.row, value['row'] + 1)
                self.col = max(self.col, value['col'] + 1)

            self.seats = [['*' for i in range(self.col)] for j in range(self.row)] 
            for key, value in request.json()['seats'].items():
                if value['is_reserved']:
                    self.seats[value['row']][value['col']] = '#'

            request = requests.get(self.url + 'cinema/showtime/' + str(showtime_id) + '/',
                               cookies = self.get_cookies())
            self.showtime = request.json()['showtime']
        except:
            message_dialog(title = "Error",
                           text = "Server not responding",
                           style = self.dialogStyles).run()

    def drawUi(self):
        self.pageLength = max([self.pageLength, self.col + 10,
                              len(self.showtime['movie']['name']) + len(self.showtime['cinema']['name']) + 40,
                              len(str(self.showtime['movie']['age-rating'])) + len(str(self.showtime['capacity'])) + 50,
                              len(self.showtime['time']) + 20])
                              
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, 'Movie: ' + self.showtime['movie']['name'], 'Cinema: ' + self.showtime['cinema']['name'])
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, 'Age Rating: +' + str(self.showtime['movie']['age-rating']), 
                                    'Capacity: ' + str(self.showtime['capacity']))
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, 'Time: ' + self.showtime['time'])
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawSeatsGrid(self.pageLength, self.seats)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '1 - Reserve', '2 - Comments')
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '3 - Back')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)

    def getId(self, row, col):
        for key, value in self.seatsRaw.items():
            if value['row'] == int(row) - 1 and value['col'] == int(col) - 1:
                return value['id']
