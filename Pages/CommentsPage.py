from prompt_toolkit.shortcuts import message_dialog, input_dialog
import os
import requests

from .PageMaker import PageMaker

class CommentsPage(PageMaker):
    def __init__(self, user_id, movie_id):
        super().__init__()
        # Initializing page length
        self.pageLength = 60

        # Initializing variables
        self.loadDb(movie_id)

        # Draw Ui 
        self.drawUi()

        # Handlling commands
        while(1):
            command = input("Enter The number representing your command:\n")
            if command == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            elif command == "1":
                self.rate = input_dialog(title = "Rate",
                                         text = "Rate this movie from 0 to 5:",
                                         style = self.dialogStyles).run()
                self.text = input_dialog(title = "Text",
                                         text = "Enter your comment:",
                                         style = self.dialogStyles).run()
                if self.rate is None or self.rate == "":
                    message_dialog(title = "Error",
                                   text = "rate cant be empty",
                                   style = self.dialogStyles).run()
                    continue
                if self.text is None or self.text == "":
                    message_dialog(title = "Error",
                                   text = "text cant be empty",
                                   style = self.dialogStyles).run()
                    continue
                try:
                    request = requests.post(self.url + 'movie/review/add/' + str(user_id) + '/' + str(movie_id) + '/',
                                        cookies = self.get_cookies(), json = {
                                        "rate": int(self.rate),
                                        "text": self.text
                                        })
                    if request.status_code == 201:
                        message_dialog(title = "Success",
                                   text = request.json()['message'],
                                   style = self.dialogStyles).run()
                        self.loadDb(movie_id)

                    else:
                        message_dialog(title = "Error",
                                   text = request.json()['message'],
                                   style = self.dialogStyles).run()
                except:
                    message_dialog(title = "Error",
                                   text = "Server not reponding",
                                   style = self.dialogStyles).run()
            elif command == "2":
                self.replyOn = input_dialog(title = "Id",
                                            text = "Enter The id of the comment you want to reply to:",
                                            style = self.dialogStyles).run()

                self.text = input_dialog(title = "Text",
                                         text = "Enter your response:",
                                         style = self.dialogStyles).run()
                if self.replyOn is None or self.replyOn == "":
                    message_dialog(title = "Error",
                                   text = "id cant be empty",
                                   style = self.dialogStyles).run()
                    continue
                if self.text is None or self.text == "":
                    message_dialog(title = "Error",
                                   text = "text cant be empty",
                                   style = self.dialogStyles).run()
                    continue
                try:
                    request = requests.post(self.url + 'movie/comment/add/' + str(user_id) + '/' + self.replyOn + '/',
                                        cookies = self.get_cookies(), json = {
                                        "text": self.text})

                    if request.status_code == 201:
                        message_dialog(title = "Success",
                                   text = request.json()['message'],
                                   style = self.dialogStyles).run()
                        self.loadDb(movie_id)

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
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, 'Comment Section')
        self.drawEndedLine(self.pageLength)
        self.drawComments(self.comments, 0)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '1 - Add Comment', '2 - Add Reply')
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '3 - Back')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)


    def loadDb(self, movie_id):
        self.comments = {}
        try:
            request = requests.get(self.url + 'movie/comment/list/' + str(movie_id) + '/',
                                   cookies = self.get_cookies())
            self.comments = request.json()['movie_comments']
        except:
            message_dialog(title = "Error",
                           text = "Server not responding",
                           style = self.dialogStyles).run()

    def drawComments(self, comments, depth):
        line = ""
        for key, value in comments.items():
            line = depth * '>>>>'
            self.drawLineWithParametersStartAt(self.pageLength, 2, line + str(value['id']) + ' - ' + value['username'])
            self.drawLineWithParametersStartAt(self.pageLength, 2, line + str(value['id']) + ' - ' + value['text'])
            self.drawLineWithParametersStartAt(self.pageLength, 2, line + str(value['id']) + ' - ' + value['created_at'])
            if value.get('replies', 0) != 0:
                self.drawComments(value['replies'], depth + 1)
