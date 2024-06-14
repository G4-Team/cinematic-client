from prompt_toolkit.shortcuts import message_dialog, input_dialog
import os
import requests

from .PageMaker import PageMaker

class PaymentPage(PageMaker):
    def __init__(self, card, operation, user_id):
        super().__init__()
        # Initializing page length
        self.pageLength = 50

        # Initializing variables
        self.loadDb()
        self.currentCard = card
        self.operation = operation

        # Draw Ui 
        self.drawUi()

        # handle commands
        while(1):
            command = input("Enter the number representing your commmand:\n")
            if command == "1":
                self.cvv2 = input_dialog(title = "CVV2",
                                         text = "Enter your CVV2",
                                         password = True,
                                         style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "2":
                self.passcode = input_dialog(title = "Passcode",
                                         text = "Enter your Passcode",
                                         password = True,
                                         style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "3":
                while(1):
                    self.amount = input_dialog(title = "Amount",
                                           text = "Enter the amount of money:",
                                           style = self.dialogStyles).run()
                    try:
                        self.amount = int(self.amount)
                        break
                    except:
                        message_dialog(title = "Error", text = "Amount Should be a number",
                                        style = self.dialogStyles).run()

                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()
            elif command == "6" and operation == 'T':
                self.receivingCardNumber = input_dialog(title = 'Receiving Card number',
                                                 text = "Enter receiving card number",
                                                 style = self.dialogStyles).run()
                os.system('cls' if os.name == 'nt' else 'clear')
                self.drawUi()

            elif command == "5":
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            elif command == "4":
                if operation == 'D':
                    request = requests.post(self.url + 'bank/card/deposit/' + str(user_id) +
                        '/' + str(card['id']) + '/',
                                        cookies = self.get_cookies(),
                                        json = {
                                        "card_number": card['cardNumber'],
                                        "cvv2": self.cvv2,
                                        "expiration_date": card['expireDate'],
                                        "password": self.passcode,
                                        "amount": self.amount})

                elif operation == 'W':
                    request = requests.post(self.url + 'bank/card/withdrawal/' + str(user_id) +
                        '/' + str(card['id']) + '/',
                                        cookies = self.get_cookies(),
                                        json = {
                                        "card_number": card['cardNumber'],
                                        "cvv2": self.cvv2,
                                        "expiration_date": card['expireDate'],
                                        "password": self.passcode,
                                        "amount": self.amount})

                elif operation == 'C':
                    request = requests.put(self.url + 'users/charge-wallet/' + str(user_id) +
                        '/',
                                        cookies = self.get_cookies(),
                                        json = {
                                        "card_number": card['cardNumber'],
                                        "cvv2": self.cvv2,
                                        "expiration_date": card['expireDate'],
                                        "password": self.passcode,
                                        "amount": self.amount})

                elif operation == 'T':
                    request = requests.post(self.url + 'bank/card/wire-transfer/' + str(user_id) +
                        '/' + str(card['id']) + '/',
                                        cookies = self.get_cookies(),
                                        json = {
                                        "sending_card_number": card['cardNumber'],
                                        "cvv2": self.cvv2,
                                        "expiration_date": card['expireDate'],
                                        "password": self.passcode,
                                        "receiving_card_number": self.receivingCardNumber, 
                                        "amount": self.amount})

                if request.status_code == 200:
                    message_dialog(title = "Sueccess", text = request.json()['message'], #request.json()['message'],
                               style = self.dialogStyles).run()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    message_dialog(title = "Error", text = request.json()['message'],
                               style = self.dialogStyles).run()
            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()

    def drawUi(self):
        self.pageLength = max([self.pageLength, len(self.passcode) + 20, len(self.receivingCardNumber) + 40, 
                              len(self.cvv2) + 20, len(str(self.amount)) + 20])
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, 'Payment Page')
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, self.currentCard['bankName'] +
                                    ' - ' + self.currentCard['cardNumber'])
        self.drawEndedLine(self.pageLength)
        # drawing cvv2
        if self.cvv2 == "":
            self.drawLineWithParameters(self.pageLength, '1 - CVV2')
        else:
            self.drawLineWithParameters(self.pageLength, 
                                        '1 - CVV2: ' + len(self.cvv2) * '*')
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, 
                                    'Expire Date: ' + self.currentCard['expireDate'])
        self.drawEndedLine(self.pageLength)
        # drawing passcode
        if self.passcode == "":
            self.drawLineWithParameters(self.pageLength, '2 - Passcode')
        else:
            self.drawLineWithParameters(self.pageLength, '2 - Passcode: ' +
                                        len(self.passcode) * '*')
        self.drawEndedLine(self.pageLength)
        #drawing amount
        if self.amount == "":
            self.drawLineWithParameters(self.pageLength, '3 - Amount')
        else:
            self.drawLineWithParameters(self.pageLength, 
                                        '3 - Amount: ' + str(self.amount) + 'T')

        if self.operation == 'T':
            if self.receivingCardNumber == "":
                self.drawLineWithParameters(self.pageLength, '6 - Reciving card number')
            else:
                self.drawLineWithParameters(self.pageLength, '6 - Reciving card number: ' + self.receivingCardNumber)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '4 - Confirm', '5 - Back')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)

    def loadDb(self):
        self.passcode = ""
        self.cvv2 = ""
        self.amount = ""
        self.receivingCardNumber = ""
