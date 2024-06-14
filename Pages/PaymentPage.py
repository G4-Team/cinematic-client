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
                if self.cvv2 == "":
                    self.cvv2 = None
            elif command == "2":
                self.passcode = input_dialog(title = "Passcode",
                                         text = "Enter your Passcode",
                                         password = True,
                                         style = self.dialogStyles).run()
                if self.passcode == "":
                    self.passcode = None
            elif command == "3":
                self.amount = input_dialog(title = "Amount",
                                           text = "Enter the amount of money:",
                                           style = self.dialogStyles).run()
                try:
                    self.amount = int(self.amount)
                except:
                    if self.amount is not None:
                        message_dialog(title = "Error", text = "Amount Should be a number",
                                        style = self.dialogStyles).run()
                    self.amount = None

            elif command == "6" and operation == 'T':
                self.receivingCardNumber = input_dialog(title = 'Receiving Card number',
                                                 text = "Enter receiving card number",
                                                 style = self.dialogStyles).run()
                if self.receivingCardNumber == "":
                    self.receivingCardNumber = None
            elif command == "5":
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            elif command == "4":
                payload = {}
                if self.cvv2 is not None:
                    payload['cvv2'] = self.cvv2
                if self.passcode is not None:
                    payload['password'] = self.passcode
                if self.amount is not None:
                    payload['amount'] = self.amount
                if self.receivingCardNumber is not None:
                    payload['receiving_card_number'] = self.receivingCardNumber
                payload['expiration_date'] = card['expireDate']
                if operation == 'D':
                    payload['card_number'] = card['cardNumber']
                    try:
                        request = requests.post(self.url + 'bank/card/deposit/' + str(user_id) +
                            '/' + str(card['id']) + '/',
                                        cookies = self.get_cookies(),
                                        json = payload)
                    except:
                        message_dialog(title = "Error",
                                       text = "Server not responding",
                                       style = self.dialogStyles).run()

                elif operation == 'W':
                    payload['card_number'] = card['cardNumber']
                    try:
                        request = requests.post(self.url + 'bank/card/withdrawal/' + str(user_id) +
                            '/' + str(card['id']) + '/',
                                        cookies = self.get_cookies(),
                                        json = payload)
                    except:
                        message_dialog(title = "Error",
                                       text = "Server not responding",
                                       style = self.dialogStyles).run()

                elif operation == 'C':
                    payload['card_number'] = card['cardNumber']
                    try:
                        request = requests.put(self.url + 'users/charge-wallet/' + str(user_id) + '/',
                                        cookies = self.get_cookies(),
                                        json = payload)
                    except:
                        message_dialog(title = "Error",
                                       text = "Server not responding",
                                       style = self.dialogStyles).run()

                elif operation == 'T':
                    payload['sending_card_number'] = card['cardNumber']
                    try:
                        request = requests.post(self.url + 'bank/card/wire-transfer/' + str(user_id) +
                            '/' + str(card['id']) + '/',
                                        cookies = self.get_cookies(),
                                        json = payload)
                    except:
                        message_dialog(title = "Error",
                                       text = "Server not responding",
                                       style = self.dialogStyles).run()

                try:
                    if request.status_code == 200:
                        message_dialog(title = "Sueccess", text = request.json()['message'], #request.json()['message'],
                               style = self.dialogStyles).run()
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    else:
                        message_dialog(title = "Error", text = request.json()['message'],
                               style = self.dialogStyles).run()
                except:
                    message_dialog(title = "Error",
                                   text = "Server not responding",
                                   style = self.dialogStyles).run()
            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()

    def drawUi(self):
        self.pageLength = max([self.pageLength, len(str(self.passcode)) + 20, len(str(self.receivingCardNumber)) + 40, 
                              len(str(self.cvv2)) + 20, len(str(self.amount)) + 20])
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, 'Payment Page')
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, self.currentCard['bankName'] +
                                    ' - ' + self.currentCard['cardNumber'])
        self.drawEndedLine(self.pageLength)
        # drawing cvv2
        if self.cvv2 is None:
            self.drawLineWithParameters(self.pageLength, '1 - CVV2')
        else:
            self.drawLineWithParameters(self.pageLength, 
                                        '1 - CVV2: ' + len(self.cvv2) * '*')
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, 
                                    'Expire Date: ' + self.currentCard['expireDate'])
        self.drawEndedLine(self.pageLength)
        # drawing passcode
        if self.passcode is None:
            self.drawLineWithParameters(self.pageLength, '2 - Passcode')
        else:
            self.drawLineWithParameters(self.pageLength, '2 - Passcode: ' +
                                        len(self.passcode) * '*')
        self.drawEndedLine(self.pageLength)
        #drawing amount
        if self.amount is None:
            self.drawLineWithParameters(self.pageLength, '3 - Amount')
        else:
            self.drawLineWithParameters(self.pageLength, 
                                        '3 - Amount: ' + str(self.amount) + 'T')

        if self.operation == 'T':
            if self.receivingCardNumber is None:
                self.drawLineWithParameters(self.pageLength, '6 - Reciving card number')
            else:
                self.drawLineWithParameters(self.pageLength, '6 - Reciving card number: ' + self.receivingCardNumber)
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParameters(self.pageLength, '4 - Confirm', '5 - Back')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)

    def loadDb(self):
        self.passcode = None
        self.cvv2 = None
        self.amount = None
        self.receivingCardNumber = None
