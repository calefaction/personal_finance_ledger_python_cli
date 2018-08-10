#!/usr/bin/env python
import csv, os

class DataManager:
    def read(self, fileName):
        with open(fileName) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            return csv_reader

    def write(self,fileName,rowToWrite):
        path = "databases/" + fileName

        if os.path.exists(path):
            append_write = 'a'
        else:
            append_write = 'w'

        with open(path, append_write) as csv_file:
            csv_writer = csv.writer(csv_file,delimiter=",",quotechar='"')
            csv_writer.writerow(rowToWrite)

    def readFileNames(self):
        fnames = []
        for (dirpath,dirnames,filenames) in os.walk("databases"):
            fnames.extend(filenames)
            break

        return fnames
