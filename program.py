#!/usr/bin/env python

from controllers.ledgerController import LedgerController

class Program:
    def main(self):
        # Present options to CLI
        while True:
            print "***** PROGRAM OPTIONS *****"
            print "View an account (Enter 1)"
            print "Add to a ledger (Enter 2)"
            print "List accounts (Enter 3)"
            print "Get summary (Enter 4)"

            selection = int(raw_input(""));

            ledgerController = LedgerController()

            if(selection == 1):
                    ledgerController.listAccounts()
                    accountName = raw_input("Which of the above accounts?: ")
                    ledgerController.readLedger(accountName)

            elif(selection == 2):
                ledgerController.listAccounts()
                accountName = raw_input("Enter one of the existing accounts or a new account name: ")
                payee = raw_input('Who is the payee?: ')
                credit = raw_input('Credit?: ')
                debit = raw_input('Debit?: ')
                date = raw_input('What is the date?: ')
                memo = raw_input('Any memo?: ')

                ledgerController.appendToLedger(accountName, payee, credit, debit, date, memo)

            elif(selection == 3):
                ledgerController.listAccounts()

            elif(selection == 4):
                ledgerController.totalLedger()

            else:
                print "Incorrect input, please try again."

program = Program()
program.main()
