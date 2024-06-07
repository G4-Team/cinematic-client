from prompt_toolkit.shortcuts import yes_no_dialog
import os

from .PageMaker import PageMaker

class BuySubscriptionPage(PageMaker):
    def __init__(self):
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
                                      text = "Are you sure you want to buy the Silver subscription for 100 000T?", style = self.dialogStyles).run()
                if yesNo:
                    break
                else:
                    continue
            elif command == "2":
                yesNo = yes_no_dialog(title = "Confirm Purchase",
                                      text = "Are you sure you want to buy the Gold subscription for 200 000T?", style = self.dialogStyles).run()
                if yesNo:
                    break
                else:
                    continue
            else:
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

