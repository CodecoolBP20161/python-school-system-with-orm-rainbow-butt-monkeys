from models import *


def menu():
    try:
        choice = int(input('Please choose an option: \n 1. Mentor View\n 2. Applicant View\n 3. Admin View\n 0. Quit\n'))
        if choice == 1:
            mentor_view()
        elif choice == 2:
            applicant_view()
        elif choice == 0:
            exit()
        elif choice == 3:
            admin_view()
        else:
            print('Sorry, this is not an option.')
    except ValueError:
        print('Please enter a valid option!')

def admin_view():
    try:
        choice = int(input('Please choose and option: \n 1.List Applicants\n 0. Quit\n'))
        if choice == 1:
            list_applicants()
        elif choice == 0:
            exit()
        else:
            print('Sorry, this is not an option.')
    except ValueError:
        print('Please enter a valid option!')


def list_applicants():
    try:
        choice = int(input('Please choose a filter: \n 1. Status \n 2. Registration Time\n 3. Location\n'
                            ' 4. Name\n 5. Email\n 6. School\n 7. Mentor name\n 0. Quit\n'))
        if choice == 1:
            status = str(input('Please enter a status: \n'))
            #method call comes here
        elif choice == 2:
            reg_time = str(input('Please enter a registration date (please separate year, month, day with a - ): \n'))
            #method call comes here
        elif choice == 3:
            city = str(input('Please enter a city name:\n'))
            #method call comes here
        elif choice == 4:
            name = str(input('Please enter a name: \n'))
            #method call comes here
        elif choice == 5:
            email = str(input('Please enter an email address: \n'))
            #method call comes here
        elif choice == 6:
            school = str(input('Please enter the name of the School: \n'))
            # method call comes here
        elif choice == 7:
            mentor = str(input('Please enter the name of the mentor: \n'))
            # method call comes here
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
