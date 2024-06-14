from prompt_toolkit.shortcuts import message_dialog, input_dialog
import os
import requests

from .PageMaker import PageMaker

class AddBankAccountPage(PageMaker):
    def __init__(self, user_id):
        super().__init__()
        # Initializing page length
        self.pageLength = 50

        # Initilizing variables
        self.bankName = ""
        self.cardNumber = ""
        self.cvv2 = ""
        self.passcode = ""
        self.expireDate = ""
        self.balance = ""

        # draw Ui 
        self.drawUi()

        # Handle commands
        self.flag = True
        while(self.flag):
            command = input("Enter the number representing your command:\n")
            if command == "1":
                self.bankName = input_dialog(title = 'Bank Name',
                                             text = 'Enter Bank Name:',
                                             style = self.dialogStyles).run()
            elif command == "2":
                self.cardNumber = input_dialog(title = "Card Number",
                                    text = "Enter Card number:\n(ex. xxxx xxxx xxxx xxxx)",
                                    style = self.dialogStyles).run()
            elif command == "3":
                self.cvv2 = input_dialog(title = "CVV2",
                                         text = "Enter CVV2",
                                         style = self.dialogStyles,
                                         password = True).run()
            elif command == "4":
                self.expireDate = input_dialog(title = "Expire Date",
                                               text = "Enter Expire Date:\n(ex. 1403-06)",
                                               style = self.dialogStyles).run()
            elif command == "5":
                self.passcode = input_dialog(title = "Passcode",
                                             text = "Enter Passcode",
                                             style = self.dialogStyles,
                                             password = True).run()
            elif command == "6":
                self.balance = input_dialog(title = "Balance",
                                            text = "Enter Balance",
                                            style = self.dialogStyles).run()
                try:
                    self.balance = int(self.balance)
                except:
                    self.balance = ""
                    message_dialog(title = "Error", 
                                   text = "Balance should be number",
                                   style = self.dialogStyles).run()
            elif command == "7":
                request = requests.post(self.url + 'bank/card/add/' + str(user_id) + '/',
                                        cookies = self.get_cookies(), json = {
                                        "bank_name": self.bankName,
                                        "card_number": self.cardNumber,
                                        "cvv2": self.cvv2,
                                        "expiration_date": self.expireDate,
                                        "password": self.passcode,
                                        "balance": self.balance})
                if request.status_code == 201:
                    message_dialog(title = "Success",
                               text = request.json()['message'], 
                               style = self.dialogStyles).run()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("what")
                    break
                else:
                    message_dialog(title = "Error",
                               text = request.json()['message'], 
                               style = self.dialogStyles).run()
            elif command == "8":
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            os.system('cls' if os.name == 'nt' else 'clear')
            self.drawUi()
        print("over")

    def drawUi(self):
        self.pageLength = max([self.pageLength, 
                                len(self.bankName) + 30, 
                                len(self.cardNumber) + 30,
                                len(self.cvv2) + 25,
                                len(self.passcode) + 30,
                                len(self.expireDate) + 30])
        self.drawLine(self.pageLength)
        self.drawEndedLine(self.pageLength)
        # drawing bank name
        if self.bankName != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Bank Name', ':', 
                                                     self.bankName)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '1 - Bank Name') 

        # drawing card number
        if self.cardNumber != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Card Number', ':', 
                                                     self.cardNumber)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '2 - Card Number') 

        # drawing cvv2
        if self.cvv2 != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - CVV2', ':', 
                                                     len(self.cvv2) * '*')
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '3 - CVV2') 
        
        # drawing expire date
        if self.expireDate != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - Expire Date', ':', 
                                                     self.expireDate)
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '4 - Expire Date') 

        # drawing passcode
        if self.passcode != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '5 - Passcode', ':', 
                                                     len(self.passcode) * "*")
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '5 - Passcode') 

        self.drawEndedLine(self.pageLength)
        #draw balance
        if self.balance != "":
            self.drawLineWithParametersStartAt(self.pageLength, 2, '6 - Balance', ':', 
                                                     str(self.balance))
        else:
            self.drawLineWithParametersStartAt(self.pageLength, 2, '6 - Balance') 
        self.drawEndedLine(self.pageLength)
        self.drawLineWithParametersStartAt(self.pageLength, 2, '7 - Confirm     ', '8 - Back')
        self.drawEndedLine(self.pageLength)
        self.drawLine(self.pageLength)
