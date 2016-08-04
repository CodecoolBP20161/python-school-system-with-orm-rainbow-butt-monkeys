from models import *


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
        choice = int(input('Please choose an option: \n 1. Interview Details\n 0. Quit\n'))
        if choice == 1:
            mentor_id = int(input("Please enter your id."))
            Mentor.interview_details(mentor_id)
        elif choice == 0:
            exit()
        else:
            print('Sorry, this is not an option.')
    except ValueError:
        print('Please enter a valid option!')


def applicant_view():
    try:
        choice = int(input('Please choose an option: \n 1. Application Details\n 2. Interview Details'
                           '\n 0. Quit\n'))
        if choice == 1:
            app_code = input("Please write your application code:")
            Applicant.application_details(app_code)
        elif choice == 2:
            app_code = input("Please write your application code:")
            Interview.interview_details(app_code)
        elif choice == 0:
            exit()
        else:
            print('Sorry, this is not an option.')
    except ValueError:
        print('Please enter a valid option!')


menu()
