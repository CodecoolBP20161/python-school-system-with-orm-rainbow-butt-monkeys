from models import *
from applicant_view import *

def menu():
    try:
        choice = int(input('Please choose an option: \n 1. Mentor View\n 2. Applicant View\n 0. Quit\n'))
        if choice == 1:
            mentor_view()
        elif choice == 2:
            applicant_view()
        elif choice == 0:
            exit()
        else:
            print('Sorry, this is not an option.')
    except ValueError:
        print('Please enter a valid option!')


def mentor_view():
    try:
        choice = int(input('Please choose an option: \n 1. Interview Details\n 2. Back to Main Menu\n 0. Quit\n'))
        if choice == 1:
            print('ONE')
        elif choice == 2:
            print('TWO')
        elif choice == 0:
            exit()
        else:
            print('Sorry, this is not an option.')
    except ValueError:
        print('Please enter a valid option!')


def applicant_view():
    try:
        choice = int(input('Please choose an option: \n 1. Application Details\n 2. Interview Details'
                           '\n 3. Back to Main Menu \n 0. Quit\n'))
        if choice == 1:
            app_code = input("Please write your application code:")
            application_details(app_code)
        elif choice == 2:
            print('TWO')
        elif choice == 0:
            exit()
        else:
            print('Sorry, this is not an option.')
    except ValueError:
        print('Please enter a valid option!')


menu()
