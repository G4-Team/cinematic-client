import os

from .PageMaker import PageMaker
from .EditAdminProfilePage import EditAdminProfilePage
from .AddMoviePage import AddMoviePage



class AdminProfilePage(PageMaker):
    def __init__(self):
        super().__init__()
        # Initializing page length
        self.pageLength = 50

        # Initializing variables
        self.username = "admin"
        self.addmovie = "add movie"

        self.currentPage = 1

        # should connect to backend and get date from database later
        self.movieList = [
            {
                "name": "openhaimerjdlfajsdfjalsdjflajsdjlajsdls",
                "date": "2024/06/20",
                "capacityLeft": "12",
                "price": "20 000T"
            },
            {
                "name": "barbe",
                "date": "2022/11/12",
                "capacityLeft": "30",
                "price": "42 000T"
            },
            {
                "name": "SpiderMan no way home",
                "date": "2023/02/30",
                "capacityLeft": "6",
                "price": "35 000T"
            },
            {
                "name": "openhaimerjdlfajsdfjalsdjflajsdjlajsdls",
                "date": "2024/06/20",
                "capacityLeft": "12",
                "price": "20 000T"
            },
            {
                "name": "barbe",
                "date": "2022/11/12",
                "capacityLeft": "30",
                "price": "42 000T"
            },
            {
                "name": "SpiderMan no way home",
                "date": "2023/02/30",
                "capacityLeft": "6",
                "price": "35 000T"
            },
            {
                "name": "openhaimerjdlfajsdfjalsdjflajsdjlajsdls",
                "date": "2024/06/20",
                "capacityLeft": "12",
                "price": "20 000T"
            },
            {
                "name": "barbe",
                "date": "2022/11/12",
                "capacityLeft": "30",
                "price": "42 000T"
            },
            {
                "name": "SpiderMan no way home",
                "date": "2023/02/30",
                "capacityLeft": "6",
                "price": "35 000T"
            },
            {
                "name": "openhaimerjdlfajsdfjalsdjflajsdjlajsdls",
                "date": "2024/06/20",
                "capacityLeft": "12",
                "price": "20 000T"
            },
            {
                "name": "barbe",
                "date": "2022/11/12",
                "capacityLeft": "30",
                "price": "42 000T"
            },
            {
                "name": "SpiderMan no way home",
                "date": "2023/02/30",
                "capacityLeft": "6",
                "price": "35 000T"
            },
            {
                "name": "openhaimerjdlfajsdfjalsdjflajsdjlajsdls",
                "date": "2024/06/20",
                "capacityLeft": "12",
                "price": "20 000T"
            },
            {
                "name": "barbe",
                "date": "2022/11/12",
                "capacityLeft": "30",
                "price": "42 000T"
            },
            {
                "name": "SpiderMan no way home",
                "date": "2023/02/30",
                "capacityLeft": "6",
                "price": "35 000T"
            },
            {
                "name": "openhaimerjdlfajsdfjalsdjflajsdjlajsdls",
                "date": "2024/06/20",
                "capacityLeft": "12",
                "price": "20 000T"
            },
            {
                "name": "barbe",
                "date": "2022/11/12",
                "capacityLeft": "30",
                "price": "42 000T"
            },
            {
                "name": "SpiderMan no way home",
                "date": "2023/02/30",
                "capacityLeft": "6",
                "price": "35 000T"
            },
            {
                "name": "openhaimerjdlfajsdfjalsdjflajsdjlajsdls",
                "date": "2024/06/20",
                "capacityLeft": "12",
                "price": "20 000T"
            },
            {
                "name": "barbe",
                "date": "2022/11/12",
                "capacityLeft": "30",
                "price": "42 000T"
            },
            {
                "name": "SpiderMan no way home",
                "date": "2023/02/30",
                "capacityLeft": "6",
                "price": "35 000T"
            },
            {
                "name": "openhaimerjdlfajsdfjalsdjflajsdjlajsdls",
                "date": "2024/06/20",
                "capacityLeft": "12",
                "price": "20 000T"
            },
            {
                "name": "barbe",
                "date": "2022/11/12",
                "capacityLeft": "30",
                "price": "42 000T"
            },
            {
                "name": "SpiderMan no way home",
                "date": "2023/02/30",
                "capacityLeft": "6",
                "price": "35 000T"
            },
            {
                "name": "openhaimerjdlfajsdfjalsdjflajsdjlajsdls",
                "date": "2024/06/20",
                "capacityLeft": "12",
                "price": "20 000T"
            },
            {
                "name": "barbe",
                "date": "2022/11/12",
                "capacityLeft": "30",
                "price": "42 000T"
            },
            {
                "name": "SpiderMan no way home",
                "date": "2023/02/30",
                "capacityLeft": "6",
                "price": "35 000T"
            },
            {
                "name": "openhaimerjdlfajsdfjalsdjflajsdjlajsdls",
                "date": "2024/06/20",
                "capacityLeft": "12",
                "price": "20 000T"
            },
            {
                "name": "barbe",
                "date": "2022/11/12",
                "capacityLeft": "30",
                "price": "42 000T"
            },
            {
                "name": "SpiderMan no way home",
                "date": "2023/02/30",
                "capacityLeft": "6",
                "price": "35 000T"
            },
            {
                "name": "openhaimerjdlfajsdfjalsdjflajsdjlajsdls",
                "date": "2024/06/20",
                "capacityLeft": "12",
                "price": "20 000T"
            },
            {
                "name": "barbe",
                "date": "2022/11/12",
                "capacityLeft": "30",
                "price": "42 000T"
            },
            {
                "name": "SpiderMan no way home",
                "date": "2023/02/30",
                "capacityLeft": "6",
                "price": "35 000T"
            },
            {
                "name": "openhaimerjdlfajsdfjalsdjflajsdjlajsdls",
                "date": "2024/06/20",
                "capacityLeft": "12",
                "price": "20 000T"
            },
            {
                "name": "barbe",
                "date": "2022/11/12",
                "capacityLeft": "30",
                "price": "42 000T"
            },
            {
                "name": "SpiderMan no way home",
                "date": "2023/02/30",
                "capacityLeft": "6",
                "price": "35 000T"
            },
        ]

        # Drawing ui 
        self.drawUi()

        # Handle Commands
        while(1):
            command = input("Enter the number representing your command:\n")
            if command == "9":
                os.system('cls' if os.name == 'nt' else 'clear')
                editaddminProfilePage = EditAdminProfilePage()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "10":
                os.system('cls' if os.name == 'nt' else 'clear')
                addMovePage = AddMoviePage()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "11" and self.currentPage < (len(self.movieList) + 8) // 8:
                self.currentPage += 1
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "12" and self.currentPage > 1:
                self.currentPage -= 1
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()

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
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '9 - Profile', '10 - Add Movie')
        self.drawEndedLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
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
        self.drawLine(self.pageLength)