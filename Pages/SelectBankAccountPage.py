from prompt_toolkit.shortcuts import yes_no_dialog, message_dialog, input_dialog
import os

from .PageMaker import PageMaker
from .PaymentPage import PaymentPage

class SelectBankAccountPage(PageMaker):
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
            command = input("Enter the number representing your card:\n")
            try:
                command = int(command)
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
                continue
            if command == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            elif 2 <= command <= len(self.banksList) + 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                paymentPage = PaymentPage(self.banksList[command - 2])
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
        self.drawLineWithParametersStartAt(self.pageLength, 2, 'Select Bank Accounts')
        self.drawEndedLine(self.pageLength)
        self.drawCardsGrid(self.pageLength, 2, self.banksList)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '1 - Back')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
