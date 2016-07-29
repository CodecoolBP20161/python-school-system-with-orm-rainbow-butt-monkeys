from models import *

# Write here your console application

Applicant.check_app_code()
print('Add application codes to the Applicants.')
Applicant.check_for_school()
print('Assign school to the Applicants.')
Interview.give_interview_slot()
print('Reserve an interview slot to the Applicants.')
