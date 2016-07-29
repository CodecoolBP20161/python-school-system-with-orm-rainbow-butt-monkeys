from models import *

def menu():
    try:
        choice = int(input('Please choose an option: \n 1. Mentor View\n 2. Applicant View\n 0. Quit'))
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


def mentor_view():
    try:
        choice = int(input('Please choose an option: \n 1. Interview Details\n 2. Back to Main Menu\n 0. Quit'))
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


def interview_details_m():
    user = input("Please enter your first name: ")

#     query = (
#             Mentor.select(Mentor,
#                           Interview
#                           )
#             .join(Interview, on=(Mentor.id == Interview.mentor_id))
#
#         .join(Applicant, on=(Interview.applicant_id == Applicant.id))
#         .where(Mentor.first_name == user)
#
#     print(query)
#
# interview_details_m()

def applicant_view():
    try:
        choice = int(input('Please choose an option: \n 1. Application Details\n 2. Interview Details\n
                     '3. Back to Main Menu \n 0. Quit'))
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
