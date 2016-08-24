from models import *


def menu():
    choice = True
    while choice != 0:
        try:
            choice = int(input('\nPlease choose an option: \n\n1. Mentor View\n'
                               '2. Applicant View\n3. Admin View\n0. Quit\n'))
            if choice == 1:
                mentor_view()
            elif choice == 2:
                applicant_view()
            elif choice == 0:
                exit()
            elif choice == 3:
                admin_view()
            else:
                print('Sorry, this is not an option.\n')
        except ValueError:
            print('Please enter a valid option!\n')


def admin_view():
    choice = True
    while choice != 0:
        try:
            choice = int(input('Please choose and option: \n\n1. List Applicants\n0. Back to Main menu\n'))
            if choice == 1:
                list_applicants()
            elif choice == 0:
                break
            else:
                print('Sorry, this is not an option.\n')
        except ValueError:
            print('Please enter a valid option!\n')


def list_applicants():
    choice = True
    while choice != 0:
        try:
            choice = int(input('Please choose a filter: \n\n1. Status \n2. Registration Time\n3. Location\n'
                               '4. Name\n5. Email\n6. School\n7. Mentor name\n0. Back to Admin menu\n'))
            if choice == 1:
                status = str(input('Please enter a status: \n'))
                Applicant.filter_status(status)
            elif choice == 2:
                reg_time = str(input('Please enter a registration date (please separate year, month, day with a - ): \n'))
                Applicant.filter_reg_time(reg_time)
            elif choice == 3:
                city = str(input('Please enter a city name:\n'))
                Applicant.filter_location(city)
            elif choice == 4:
                name = str(input('Please enter first or last name: \n'))
                Applicant.filter_name(name)
            elif choice == 5:
                email = str(input('Please enter an email address: \n'))
                Applicant.filter_email(email)
            elif choice == 6:
                school = str(input('Please enter the location of the School: \n'))
                Applicant.filter_school(school)
            elif choice == 7:
                mentor = str(input('Please enter the last name of the mentor: \n'))
                Applicant.filter_mentor(mentor)
            elif choice == 0:
                break
        except ValueError:
            print('Please enter a valid option!\n')


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
