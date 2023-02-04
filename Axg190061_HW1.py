## Afaf Guesmia axg190061
## CS 4395.001
## This is a python program that reads for a file, process the text to be more standaedized.


import csv
import sys
import re
import pickle
## Create class person
class person:
    ##create def method for class person
    def __init__(self,id,last,first,mi,phone):
        self.last=last
        self.first=first
        self.mi=mi
        self.id=id
        self.phone=phone
    ## Create diplay method to display the employee's information
    def display(self):

        print("Employee ID: ", self.id)
        print(self.last,self.first,self.mi,self.phone)




## main method
if __name__=='__main__':
    ## Check if the user enter an argument
    if len(sys.argv) < 2:
        print("Please enter the name of the file as system arg")
        quit()
    else:
        ##open the csv file
        with open("data/data.csv", 'r') as file:
            csvreader = csv.reader(file, delimiter=',')
            file_ew = csv.DictReader(file)
            line2 = file.readline()[0:] ## read the file line by line and ignore the first line
            for row in csvreader:
                ##create list of each row
                list_of_last = list(row[0])
                list_of_mi = list(row[2])

                list_of_id = list(row[3])
                new_last = str.upper(row[0])
                new_first = str.upper(row[1])
                ## check if the mi row is empty if true replace it with X
                if len(list_of_mi) == 0:
                    list_of_mi = list("X")
                else:
                    list_of_mi
                    ## check if the ID row countains 2 letters and 4 numbers if true leave it if false, fix it using if-else statement
                result_id = re.findall(r'^[a-zA-Z][a-zA-z]\d\d\d\d', row[3], re.MULTILINE)
                if (result_id):
                    result_id
                else:
                    print("ID invalid:", row[3])
                    print("ID is two letters followed by 4 digits")
                    row[3] = input("Please enter a valid id: ")
                 ## check if the phone number row is in form of 123-456-7890
                result_num = re.findall(r"\d\d\d-\d\d\d-\d\d\d\d", row[4], re.MULTILINE)

                if (result_num):
                    result_num
                else:
                    print("Phone", row[4], "is invalid")
                    print("Enter phone number in form 123-456-7890")
                    row[4] = input("Enter phone number:")
                    ## emp1 object to save the new employee information
                    emp1 = person(row[3], new_last, new_first, list_of_mi, row[4])
                    print(emp1.display())
            ## create a pickle file and load into it

            dict_person={}
            pickle.dump(dict_person,open("dict_person.pickle",'wb'))
            dict_in=pickle.load(open('dict_person.pickle','rb'))




































































































































































