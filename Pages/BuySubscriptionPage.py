from prompt_toolkit.shortcuts import yes_no_dialog, message_dialog
import os
import requests

from .PageMaker import PageMaker

class BuySubscriptionPage(PageMaker):
    def __init__(self, user_id):
        super().__init__()
        # Initializing page length
        self.pageLength = 30

        # Initializing variables
        self.currentSubscription = "Silver"

        # draw ui 
        self.drawUi()

        # Handle commands
        while(1):
            command = input("Enter the number representing your command:\n")
            if command == "1":
                yesNo = yes_no_dialog(title = "Confirm Purchase",
                                      text = "Are you sure you want to buy the Silver subscription for 300T?", 
                                      style = self.dialogStyles).run()
                if yesNo:
                    request = requests.put(self.url + 'users/buy-subscription/' + str(user_id) + '/',
                                           cookies = self.get_cookies(), json = {
                        "type_subscription": 'silver'
                    })
                    break
                    if request.status_code == 200:
                        message_dialog(title = 'Success',
                                       text = request.json()['message'],
                                       style = self.dialogStyles).run()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    else:
                        message_dialog(title = 'Error',
                                       text = request.json()['message'],
                                       style = self.dialogStyles).run()
                else:
                    continue
            elif command == "2":
                yesNo = yes_no_dialog(title = "Confirm Purchase",
                                      text = "Are you sure you want to buy the Gold subscription for 600T?", 
                                      style = self.dialogStyles).run()
                if yesNo:
                    request = requests.put(self.url + 'users/buy-subscription/' + str(user_id) + '/', 
                                           cookies = self.get_cookies(),
                                           json = {
                        "type_subscription": 'gold'
                    })
                    break
                    if request.status_code == 200:
                        message_dialog(title = 'Success',
                                       text = request.json()['message'],
                                       style = self.dialogStyles).run()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    else:
                        message_dialog(title = 'Error',
                                       text = request.json()['message'],
                                       style = self.dialogStyles).run()
                else:
                    continue
            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()

    def drawUi(self):
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, 'Buy Subscription')
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '1 - Silver')
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '2 - Gold')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)

