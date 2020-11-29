#Name: Taylor Walden
#Date: November 29, 2020
#Program: AddressBook

import os
import sys
import re
from pyfiglet import figlet_format
from termcolor import colored
#Displays ascii art 
ascii_Art = figlet_format("Address Book")
print(ascii_Art)
#This function allows the user to add, search, modify, or delete a contact. It also allows the user to read the address book or close the file. 
def Printmenu():
    print("Open File Menu")
    print("1.Add new contact")
    print("2.Search for a contact")
    print("3.Modify a contact")
    print("4.Delete a contact")
    print("5.Read entire Address Book.")
    print("6.Close file")
#This function is the the file access menu which allows the user to search, create, or open a file or close the program. 
def mainMenu():
    print("File Access Menu")
    print("1. Search a file")
    print("2. Create a file")
    print("3. Open a file")
    print("4. Exit")
    

while True:
    mainMenu()
    selection = input("Enter your choice: ")

    if selection == str("1"):
        try:
            f = open(input("filename: "))
            f.close()
            print("File has been found!")
        except FileNotFoundError:
            print('File does not exist')
    elif selection == str("2"):
        CreateFile = input("filename: ")
        f = open(CreateFile, "x")
        print("File created successfully!")
    elif selection == str("3"):
        filename = open(input("Filename: "))
        Printmenu()
        break
    elif selection == str("4"):
        print("You have exited the program.")
        exit()
    else:
        print("Please select only numbers 1-4.")
        print("")
        

def AddName(name):
    test = open("AddressBook.txt", "a")
    test.write(name + " ")
    test.close()
def AddAddress(address):
    test = open("AddressBook.txt", "a")
    test.write(address + " ")
    test.close()
def AddPhoneNumber(phone):
    test = open("AddressBook.txt", "a")
    test.write(phone + "\n")
    test.close()

while selection == str("3"):
    for x in range (0,5):
        menu = input("Enter corresponding number from the open file menu: ")
        if menu == str("1"):
                name = input ("Enter Name: ")
                AddName(name)
                address = input("Enter Address: ")
                AddAddress(address)
                phone = input("Enter phone number:")
                AddPhoneNumber(phone)
                Printmenu()
        elif menu == str("2"):
            Name = input ("Enter the contact Name you are searching for: ")
            search = open("AddressBook.txt")
            for line in search:
                if Name in line:
                    print (line)
            Printmenu()         
        elif menu == ("5"):
            with open('AddressBook.txt', 'r') as f:
                print(f.read())
            acsending = input("Would you like to read the address book in acsending or descending order? Enter A or D: ")
            if acsending == 'A':
                with open('AddressBook.txt', 'r') as f:
                    for line in sorted(f):
                        print(line)
            elif acsending == "D":
                with open('AddressBook.txt', 'r') as f:
                    line = sorted(f, reverse=True)
                    for f in line:
                        print(f)
        elif menu == str("4"):
            removethis = input("Enter the name of the entry to be deleted: ")
            filename = 'AddressBook.txt'
            with open(filename, 'r') as fin:
                lines = fin.readlines()
            with open(filename, 'w') as fout:
                for line in lines:
                    if removethis not in line:
                       fout.write(line)
            print("The remaining entries are: ")
            with open('AddressBook.txt', 'r') as f:
                print(f.read())
        elif menu == ("6"):
            f = open("AddressBook.txt", "a")
            print("file has closed successfully.")
            f.close()
            exit()
        
        
        elif menu == str("3"):
            print("What do you want to Modify:")
            print("1.Contact Name")
            print("2.Contact Address")
            print("3.Contact Phone")
            opt = input("Enter your choice:")
            if int(opt) == 1:
                name = input("Enter the name to modify")
                new_name = input("Enter updated name")
                with open("AddressBook.txt", 'r+') as f:
                    text = f.read()
                    text = re.sub(name, new_name, text)
                    f.seek(0)
                    f.write(text)
                    f.truncate()
                Printmenu()
            elif int(opt) == 2:
                address = input("Enter the Address to modify:")
                new_address = input("Enter new address: ")
                with open("AddressBook.txt", 'r+') as f:
                    text = f.read()
                    text = re.sub(address, new_address, text)
                    f.seek(0)
                    f.write(text)
                    f.truncate()
                Printmenu()
            elif int(opt) == 3:
                phone = input("Enter the Phone number to modify:")
                new_phone = input("Enter new phone number: ")
                with open("AddressBook.txt", 'r+') as f:
                    text = f.read()
                    text = re.sub(phone, new_phone, text)
                    f.seek(0)
                    f.write(text)
                    f.truncate()
                Printmenu()
            
