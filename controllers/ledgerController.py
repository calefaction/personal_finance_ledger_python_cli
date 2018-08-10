#!/usr/bin/env python
import csv, os
from datalayer.dataManager import DataManager

class LedgerController:
    def readLedger(self,accountName):
        dataManager = DataManager()

        with open("databases/" + accountName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")

            line_count = 0
            print "\r\n"

            print("{0: <16}\t\t{1: <16}\t{2: <16}\t{3: <16}\t{4: <16}".format("Payee", "Credit ($)", "Debit ($)", "Date", "Memo"))
            print "\r\n"

            for row in csv_reader:
                payee = row[0]
                credit = row[1]
                debit = row[2]
                date = row[3]
                memo = row[4]


                print("{0: <16}\t\t{1: <16}\t{2: <16}\t{3: <16}\t{4: <16}".format(payee, credit, debit, date, memo))

            print "\r\n"

    def totalLedger(self):
        dataManager = DataManager()
        accountNames = dataManager.readFileNames()

        totalDebits = 0.00
        totalCredits = 0.00
        runningBalance = 0.00

        for accountName in accountNames:
            with open("databases/" + accountName) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")

                line_count = 0
                for row in csv_reader:
                    payee = row[0]
                    credit = row[1]
                    debit = row[2]
                    date = row[3]
                    memo = row[4]

                    totalDebits -= float(debit)
                    totalCredits += float(credit)

        runningBalance = totalCredits + totalDebits

        print "\r\n"
        print("Total credits: ${0:.2f}").format(totalCredits)
        print("Total debits: ${0:.2f}").format(totalDebits)
        print "\r\n"
        print("Running balance is: ${0:.2f}").format(runningBalance)
        print "\r\n"

    def listAccounts(self):
        dataManager = DataManager()
        accountNames = dataManager.readFileNames()

        print '\r\n'
        for accountName in accountNames:

            print('\t{}').format(accountName)

        print '\r\n'

    def appendToLedger(self,accountName, payee, credit, debit, date, memo):
        dataManager = DataManager()
        dataManager.write(accountName, [payee,credit,debit,date,memo])
