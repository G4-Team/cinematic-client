from prompt_toolkit.shortcuts import yes_no_dialog, message_dialog, input_dialog
import os
import requests

from .PageMaker import PageMaker
from .SelectBankAccountPage import SelectBankAccountPage
from .AddBankAccountPage import AddBankAccountPage

class BankAccountsPage(PageMaker):
    def __init__(self, user_id):
        super().__init__()
        # Initializing page length
        self.pageLength = 40

        # Initializing variables
        self.loadDb(user_id)

        # Draw Ui 
        self.drawUi()

        # Handle command
        while(1):
            command = input("Enter the number representing your command:\n")
            if command == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                addBankAccountPage = AddBankAccountPage(user_id)
                self.loadDb(user_id)

            elif command == "2":
                # Transfer
                os.system('cls' if os.name == 'nt' else 'clear')
                selectBankAccountPage = SelectBankAccountPage('T', user_id)

            elif command == "3":
                # Withdraw
                os.system('cls' if os.name == 'nt' else 'clear')
                selectBankAccountPage = SelectBankAccountPage('W', user_id)

            elif command == "4":
                # Deposit
                os.system('cls' if os.name == 'nt' else 'clear')
                selectBankAccountPage = SelectBankAccountPage('D', user_id)

            elif command == "5":
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()

    def loadDb(self, user_id):
        requestGetAllCards = requests.get(self.url + 'bank/card/list/' + str(user_id) + '/',
                                          cookies = self.get_cookies())
        print(requestGetAllCards.json())
        self.banksList = []
        for key, value in requestGetAllCards.json()['cards'].items():
            dic = {}
            dic['bankName'] = value['bank_name']
            dic['cardNumber'] = value['card_number']
            dic['cvv2'] = value['cvv2']
            dic['expireDate'] = value['expiration_date']
            self.banksList.append(dic)
    
    def drawUi(self):
        for card in self.banksList:
            self.pageLength = max(self.pageLength, len(card['bankName']) 
                                  + len(card['cardNumber']) + len(card['expireDate']) + 23)
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParametersStartAt(self.pageLength, 2, 'Bank Accounts')
        self.drawEndedLine(self.pageLength)
        self.drawCardsGrid(self.pageLength, 5, self.banksList)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '1 - Add', '2 - Transfer')
        self.drawLineWithParameters(self.pageLength, '3 - Withdraw', '4 - Deposit')
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '5 - Back')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
