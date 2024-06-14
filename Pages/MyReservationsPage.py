from prompt_toolkit.shortcuts import message_dialog, input_dialog, yes_no_dialog
import os
import requests

from .PageMaker import PageMaker

class MyReservationsPage(PageMaker):
    def __init__(self, user_id):
        super().__init__()
        # Initializing page length
        self.pageLength = 50

        # Initializing varibales
        self.loadDb(user_id)

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
                                        text = "Enter the id of the reservation you want to cancel:",
                                        style = self.dialogStyles).run()
                try:
                    cancelReservation = int(cancelReservation)
                except:
                    message_dialog(title = "Error",
                                   text = "id should be a number",
                                   style = self.dialogStyles).run()
                    continue
                if cancelReservation is not None:
                    yesNo = yes_no_dialog(title = "Cancel Reservation",
                                      text = "Are you Sure you want to cancel resevation number " + str(cancelReservation),
                                      style = self.dialogStyles).run()
                    if yesNo:
                        try:
                            request = requests.delete(self.url + 'cinema/cancel/' + str(user_id) + '/' + str(cancelReservation) + '/',
                                                      cookies = self.get_cookies())
                            if request.status_code == 200:
                                message_dialog(title = "Cancel Reservation",
                                    text = request.json()['message'], 
                                    style = self.dialogStyles).run()
                                self.loadDb(user_id)
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
        # Makeing sure the pageLength can contain everything 
        maxLen = 0
        for movie in self.movieList:
            maxLen = max(maxLen, len(movie['name']) + len(movie['date']) 
                + len(movie['seat']) + len(movie['price']))
        maxLen += 25
        self.pageLength = max(maxLen, self.pageLength)
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParametersStartAt(self.pageLength, 2, 'My Reservations')
        self.drawEndedLine(self.pageLength)
        self.drawMovieGridR(self.pageLength, self.movieList, self.currentPage)
        self.drawEndedLine(self.pageLength)
        # drawing next and previous page if needed
        if (len(self.movieList) + 8) // 8 != 1:
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

    def loadDb(self, user_id):
        self.currentPage = 1
        self.movieList = []
        try:
            request = requests.get(self.url + 'cinema/reserved-seats/' + str(user_id) + '/',
                               cookies = self.get_cookies())
            for key, value in request.json()['reservations'].items():
                req = requests.get(self.url + 'cinema/showtimes/' + str(value['showtime_id']) + '/',
                               cookies = self.get_cookies())
                dic = {}
                dic['id'] = str(value['id'])
                dic['name'] = req.json()['showtimes']['showtime0']['movie']['name']
                dic['date'] = req.json()['showtimes']['showtime0']['time']
                dic['price'] =  str(req.json()['showtimes']['showtime0']['cinema']['ticket_price'])
                dic['seat'] = 'row: ' + str(value['row']) + ' - col: ' + str(value['col'])
                self.movieList.append(dic)
        except:
            message_dialog(title = "Error",
                           text = "Server not responding",
                           style = self.dialogStyles).run()

