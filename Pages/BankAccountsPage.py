from prompt_toolkit.shortcuts import yes_no_dialog, message_dialog, input_dialog
import os

from .PageMaker import PageMaker

class BankAccountsPage(PageMaker):
    def __init__(self):
        super().__init__()
        # Initializing page length
        self.pageLength = 40

        # Initializing variables
        self.loadDb()

        # Draw Ui 
        self.drawUi()

        # Handle command
        while(1):
            command = input("Enter the number representing your command:\n")
            if command == "1":
                pass
                #addBankAccountPage = AddBankAccountPage()
            elif command == "2":
                removeCard = input_dialog(title = "Remove Card", 
                                        text = "Enter the number of the card you want to delele:",
                                        style = self.dialogStyles).run()
                if removeCard is not None:
                    yesNo = yes_no_dialog(title = "Remove Card",
                                      text = "Are you Sure you want to delete card " + removeCard,
                                      style = self.dialogStyles).run()
                    if yesNo:
                        message_dialog(title = "Remove Card",
                                   text = "Card removed successfuly!",
                                   style = self.dialogStyles).run()
            elif command == "3":
                pass
                #chargeAccountPage = ChargeAccountPage()
            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()

    def loadDb(self):
        self.banksList = [
            {
                "bankName": "meli",
                "cardNumber": "6231 0231 4342 1234",
                "expireDate": "1403/20"
            },
            {
                "bankName": "meli",
                "cardNumber": "6231 0231 4342 1234",
                "expireDate": "1403/20"
            },
            {
                "bankName": "meli",
                "cardNumber": "6231 0231 4342 1234",
                "expireDate": "1403/20"
            },
            {
                "bankName": "meli",
                "cardNumber": "6231 0231 4342 1234",
                "expireDate": "1403/20"
            },
            {
                "bankName": "meli",
                "cardNumber": "6231 0231 4342 1234",
                "expireDate": "1403/20"
            },
            {
                "bankName": "meli",
                "cardNumber": "6231 0231 4342 1234",
                "expireDate": "1403/20"
            },
            {
                "bankName": "meli",
                "cardNumber": "6231 0231 4342 1234",
                "expireDate": "1403/20"
            },
            {
                "bankName": "meli",
                "cardNumber": "6231 0231 4342 1234",
                "expireDate": "1403/20"
            },
            {
                "bankName": "meli",
                "cardNumber": "6231 0231 4342 1234",
                "expireDate": "1403/20"
            },
            {
                "bankName": "meli",
                "cardNumber": "6231 0231 4342 1234",
                "expireDate": "1403/20"
            },
            {
                "bankName": "meli",
                "cardNumber": "6231 0231 4342 1234",
                "expireDate": "1403/20"
            },
            {
                "bankName": "meli",
                "cardNumber": "6231 0231 4342 1234",
                "expireDate": "1403/20"
            },
        ]
    
    def drawUi(self):
        for card in self.banksList:
            self.pageLength = max(self.pageLength, len(card['bankName']) 
                                  + len(card['cardNumber']) + len(card['expireDate']) + 23)
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParametersStartAt(self.pageLength, 2, 'Bank Accounts')
        self.drawEndedLine(self.pageLength)
        self.drawCardsGrid(self.pageLength, self.banksList)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '1 - Add', '2 - Remove')
        self.drawLineWithParameters(self.pageLength, '3 - Charge Accounts')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
