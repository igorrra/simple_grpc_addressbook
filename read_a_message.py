#!/usr/bin/env python3.7

import addressbook_pb2
import sys


# Iterates though all people in the AddressBook and prints info about them.
def ListPeople(book):
    """"""
    for person in book.people:
        print("Person ID:", person.id)
        print("  Name:", person.name)
        if person.HasField('email'):
            print("  E-mail address:", person.email)

        for phone_number in person.phones:
            if phone_number.type == addressbook_pb2.Person.PhoneType.MOBILE:
                print("  Mobile phone #: ",)
            elif phone_number.type == addressbook_pb2.Person.PhoneType.HOME:
                print("  Home phone #: ",)
            elif phone_number.type == addressbook_pb2.Person.PhoneType.WORK:
                print("  Work phone #: ",)
            print("    ", phone_number.number, "\n")

        for address in person.addresses:
            print("  Street:", address.street)
            if address.type == addressbook_pb2.Person.BuildingType.private:
                print("  Private house #: ",)
            elif address.type == addressbook_pb2.Person.BuildingType.flat:
                print("  Flat #: ",)
            print("    ", address.number, "\n")


# Main procedure:  Reads the entire address book from a file and prints all
#   the information inside.
if len(sys.argv) >= 2:
    print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
    sys.exit(-1)

address_book = addressbook_pb2.AddressBook()

# Read the existing address book.
f = open('address_book', "rb")
address_book.ParseFromString(f.read())
f.close()

ListPeople(address_book)
