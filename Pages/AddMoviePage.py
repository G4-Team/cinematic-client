from prompt_toolkit.shortcuts import input_dialog, message_dialog
import os

from .PageMaker import PageMaker

class AddMoviePage(PageMaker):
    def __init__(self):
        super().__init__()
        # Initializing page lenght
        self.pageLength = 40

        # Initializing variables
        self.loadDb()

        # draw ui 
        self.drawUi()

        # Handle command
        while(1):
            command = input("Enter the number representing your command:\n")
            if command == "1":
                self.moviename = input_dialog(title = "movie name", text = "Enter movie name:",
                                             style = self.dialogStyles).run() 
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "2":
                self.dateofrealease = input_dialog(title = "date of realease", text = "Enter date: \n(ex. yyyy/mm/dd)", 
                                          style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "3":
                self.director = input_dialog(title = "director", 
                                                text = "Enter director name:",
                                                style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "4":
                self.genres = input_dialog(title = "genres", 
                                             text = "Enter genres:", 
                                             password = True,
                                             style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "5":
                self.moviedimensions = input_dialog(title = "movie dimensions", 
                                              text = "Enter movie dimensions: ",
                                              style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "6":
                message_dialog(title = "Info", text = "Movie add successfully!",
                               style = self.dialogStyles).run()
                break
            elif command == "7":
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()


    def loadDb(self):
        self.moviename = ""
        self.dateofrealease = ""
        self.director = ""
        self.genres = ""
        self.moviedimensions = ""

    def drawUi(self):
        # makeing sure page can contain all content
        self.pageLenght = max([self.pageLength, len(self.moviename) + 20,
                              len(self.dateofrealease) + 20,
                              len(self.director) + 20,
                              len(self.genres) + 20,
                              len(self.moviedimensions) + 20,])
        self.drawLine(self.pageLenght)
        self.drawEndedLine(self.pageLength)
        # drawing movie name
        if self.moviename != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - movie name', ':', 
                                                     self.moviename)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - movie name') 

        # drawing date of release
        if self.dateofrealease != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - date of release', ':', 
                                                     self.dateofrealease)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - date of release') 
        
        # drawing director
        if self.director != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - director', ':', 
                                                     self.director)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - director') 

        # drawing genres
        if self.genres != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - genres', ':', 
                                                     self.genres)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - genres') 

        # drawing movie daimenstions
        if self.moviedimensions != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '5 - movie dimensions', ':',
                                                     self.moviedimensions)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '5 - movie dimensions')


        self.drawLineWithParametersStartAt(self.pageLength, 2, '6 - Confirm')
        self.drawLineWithParametersStartAt(self.pageLength, 2, '7 - Back')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
