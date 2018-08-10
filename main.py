#!/usr/bin/env python
import csv, os

class Main:
    def readLedger(accountName):
        with open("databases/" + accountName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            for row in csv_reader:
                payee = row[0]
                credit = row[1]
                debit = row[2]
                date = row[3]
                memo = row[4]
                # print(f'{payee}\t{credit}\t{debit}\t{date}\t{memo}')
                print("{0: <16}\t\t{1: <16}\t{2: <16}\t{3: <16}\t{4: <16}".format(payee, credit, debit, date, memo))
    def totalLedger():
        accountNames = []
        for (dirpath,dirnames,filenames) in os.walk("databases"):
            accountNames.extend(filenames)
            break

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

        print("Total credits: ${0:.2f}").format(totalCredits)
        print("Total debits: ${0:.2f}").format(totalDebits)
        print "\r\n"
        print("Running balance is: ${0:.2f}").format(runningBalance)

    def listAccoounts():
        accountNames = []
        for (dirpath,dirnames,filenames) in os.walk("databases"):
            accountNames.extend(filenames)
            break

        print '\r\n'
        for accountName in accountNames:

            print('\t{}').format(accountName)

        print '\r\n'

    def appendToLedger(accountName, payee, credit, debit, date, memo):
        if os.path.exists("databases/" + accountName):
            append_write = 'a'
        else:
            append_write = 'w'

        with open("databases/" + accountName, append_write) as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",",quotechar='"')
            csv_writer.writerow([payee,credit,debit,date,memo])

    # listAccoounts()
    totalLedger()
    # viewOrAdd = raw_input("Would you like to view or add to the ledger?(View/Add): ")
    # if(viewOrAdd in ['view','VIEW','View']):
    #     accountName = raw_input("Account name?: ")
    #     readLedger(accountName)
    # elif(viewOrAdd in ['add','Add','ADD']):
    #     accountName = raw_input('Account name?: ')
    #     payee = raw_input('Payee?: ')
    #     credit = raw_input('Credit?: ')
    #     debit = raw_input('Debit?: ')
    #     date = raw_input('Date?: ')
    #     memo = raw_input('Memo?: ')
    #
    #     appendToLedger(accountName, payee, credit, debit, date, memo)
    # else:
    #     print "Incorrect input, please try again."
