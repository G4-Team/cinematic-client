import os
import requests

from .PageMaker import PageMaker
from .EditProfilePage import EditProfilePage
from .AddCinemaPage import AddCinemaPage
from .AddShowtimePage import AddShowtimePage


class AdminProfilePage(PageMaker):
    def __init__(self, user_id):
        super().__init__()
        # Initializing page length
        self.pageLength = 50

        # Initializing variables
        self.loadDb(user_id)

        self.currentPage = 1

        # Drawing ui 
        self.drawUi()

        # Handle Commands
        while(1):
            command = input("Enter the number representing your command:\n")
            if command == "9":
                os.system('cls' if os.name == 'nt' else 'clear')
                editProfilePage = EditProfilePage(user_id)
                os.system('cls' if os.name == 'nt' else 'clear')
                self.loadDb(user_id)

            elif command == "11":
                os.system('cls' if os.name == 'nt' else 'clear')
                addCinemaPage = AddCinemaPage()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.loadDb(user_id)

            elif command == "10":
                os.system('cls' if os.name == 'nt' else 'clear')
                addShowtimePage = AddShowtimePage()
            elif command == "12" and self.currentPage < (len(self.movieList) + 8) // 8:
                self.currentPage += 1

            elif command == "13" and self.currentPage > 1:
                self.currentPage -= 1

            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()

    def loadDb(self, user_id):
        request = requests.get(self.url + 'users/profile/' + str(user_id) + '/',
                                   cookies = self.get_cookies())
        self.username = 'Username: ' + request.json()['user']['username']
        self.movieList = []
        request = requests.get(self.url + 'cinema/showtimes/',
                                  cookies = self.get_cookies())
        for key, value in request.json()['showtimes'].items():
            dic = {}
            dic['name'] = value['movie']['name']
            dic['date'] = value['time']
            dic['capacityLeft'] = str(value['capacity'])
            dic['price'] = str(value['cinema']['ticket_price'])
            self.movieList.append(dic)

    def drawUi(self):
        # Makeing sure the pageLength can contain everything 
        maxLen = 0
        for movie in self.movieList:
            maxLen = max(maxLen, len(movie['name']) + len(movie['date']) 
                + len(movie['capacityLeft']) + len(movie['price']) + 20)
        maxLen += 20
        self.pageLength = max([self.pageLength, maxLen, len(self.username) + 20])
           
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, self.username)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '9 - Profile', '10 - Add Showtime')
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '11 - Add Cinema')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawMovieGrid(self.pageLength, self.movieList, self.currentPage)
        self.drawEndedLine(self.pageLength)
        # drawing next and previous page if needed
        if self.currentPage == 1:
            self.drawLineWithParameters(self.pageLength, '12 - Next')
        elif self.currentPage == (len(self.movieList) + 8 ) // 8:
            self.drawLineWithParameters(self.pageLength, '13 - Previous')
        else:
            self.drawLineWithParameters(self.pageLength, '13 - Previous', '12 - Next')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
