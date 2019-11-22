import csv
import os

class Methods(object):
    def contractorList(self):
        contractorEmailList = []
        # file_name = os.listdir("/Users/gregoryreda/Desktop/Database/drbill_contracting_new_jersey_email.csv/")
        file_name = os.listdir("/Users/gregoryreda/Desktop/Database/")

        try:
            with open('/Users/gregoryreda/Desktop/Database/'+ file_name[0], 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)
                for line in csv_reader:
                    contractorEmailList.append(line[0])
                    
            print(contractorEmailList)
            return contractorEmailList
            
        except BaseException:
            print('No more Files')