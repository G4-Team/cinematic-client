import os
import requests
from prompt_toolkit.shortcuts import message_dialog

from .PageMaker import PageMaker
from .BuySubscriptionPage import BuySubscriptionPage
from .EditProfilePage import EditProfilePage
from .BankAccountsPage import BankAccountsPage
from .MyReservationsPage import MyReservationsPage
from .SelectBankAccountPage import SelectBankAccountPage
from .ShowtimeDetailsPage import ShowtimeDetailsPage


class ProfilePage(PageMaker):
    def __init__(self, user_id):
        super().__init__()
        # Initializing page length
        self.pageLength = 50

        # Initializing variables
        self.loadDb(user_id)
        #self.username = "Username: shk84"
        #self.balance = "Balance: 527 000T"
        #self.subscription = "Subscription: Gold"
        self.currentPage = 1

        # Drawing ui 
        self.drawUi()

        # Handle Commands
        while(1):
            command = input("Enter the number representing your command:\n")
            try:
                command = int(command)
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
                continue
            if 1 <= command <= 8:
                os.system('cls' if os.name == 'nt' else 'clear')
                showtimeDetailsPage = ShowtimeDetailsPage(self.showtimeDetails[command - 1 + (self.currentPage - 1) * 8], user_id)
                self.loadDb(user_id)

            elif command == 9:
                os.system('cls' if os.name == 'nt' else 'clear')
                editProfilePage = EditProfilePage(user_id)
                self.loadDb(user_id)

            elif command == 10:
                os.system('cls' if os.name == 'nt' else 'clear')
                myReservationsPage = MyReservationsPage(user_id)
                self.loadDb(user_id)

            elif command == 11:
                os.system('cls' if os.name == 'nt' else 'clear')
                bankAccountsPage = BankAccountsPage(user_id)
                self.loadDb(user_id)

            elif command == 12:
                os.system('cls' if os.name == 'nt' else 'clear')
                buySubscriptionPage = BuySubscriptionPage(user_id)
                self.loadDb(user_id)

            elif command == 16:
                os.system('cls' if os.name == 'nt' else 'clear')
                selectBankAccountPage = SelectBankAccountPage('C', user_id)
                self.loadDb(user_id)

            elif command == 15:
                os.system('cls' if os.name == 'nt' else 'clear')
                os.remove('cookie.txt')
                break

            elif command == 14 and self.currentPage < (len(self.movieList) + 8) // 8:
                self.currentPage += 1

            elif command == 13 and self.currentPage > 1:
                self.currentPage -= 1

            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()


    def loadDb(self, user_id):
        self.movieList = []
        self.username = "Username: Not found"
        self.balance = "Balance: Not found"
        self.subscription = "Subscription: Not found"
        try:
            request = requests.get(self.url + 'users/profile/' + str(user_id) + '/',
                               cookies = self.get_cookies())
            self.username = 'Username: ' + request.json()['user']['username']
            self.balance = 'Balance: ' + str(request.json()['user']['wallet'])
            self.subscription = 'Subscription: ' + request.json()['user']['cinema-subscription']['type']
            requestMovieList = requests.get(self.url + 'cinema/showtimes/' + str(user_id) + '/',
                                        cookies = self.get_cookies())
            self.showtimeDetails = []
            for key, value in requestMovieList.json()['showtimes'].items():
                dic = {}
                dic['name'] = value['movie']['name']
                dic['date'] = value['time']
                dic['capacityLeft'] = str(value['capacity'])
                dic['price'] = str(value['cinema']['ticket_price'])
                self.showtimeDetails.append(value)
                self.movieList.append(dic)
        except:
            message_dialog(title = "Error",
                           text = "Server not responding wtf",
                           style = self.dialogStyles).run()

    def drawUi(self):
        # Makeing sure the pageLength can contain everything 
        maxLen = 0
        for movie in self.movieList:
            maxLen = max(maxLen, len(movie['name']) + len(movie['date']) 
                + len(movie['capacityLeft']) + len(movie['price']))
        maxLen += 25
        self.pageLength = max([self.pageLength, maxLen, len(self.username) 
            + len(self.balance) + len(self.subscription) + 25])

        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, self.username, 
                                         self.balance, self.subscription)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '9 - Profile', '10 - My reservations', '15 - Logout')
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '11 - Bank accounts',
                                        '16 - Charge Account',
                                         '12 - Buy subscription')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawMovieGrid(self.pageLength, self.movieList, self.currentPage)
        self.drawEndedLine(self.pageLength)
        # drawing next and previous page if needed
        if (len(self.movieList) + 8) // 8 != 1:
            if self.currentPage == 1:
                self.drawLineWithParameters(self.pageLength, '14 - Next')
            elif self.currentPage == (len(self.movieList) + 8 ) // 8:
                self.drawLineWithParameters(self.pageLength, '13 - Previous')
            else:
                self.drawLineWithParameters(self.pageLength, '13 - Previous', '14 - Next')
            self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
