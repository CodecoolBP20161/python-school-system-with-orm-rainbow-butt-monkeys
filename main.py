from models import *

# Write here your console application



Applicant.check_app_code()
print('Add application codes to the Applicants.\n')
app_querry = Applicant.select()
for i in app_querry:
    print(i.last_name, i.first_name,"Applicant code:", i.application_code)

input1 = input()

Applicant.check_for_school()
print('Assign school to the Applicants.\n')
app_querry_2 = Applicant.select()
for i in app_querry_2:
    print(i.last_name, i.first_name, "School:", i.school.location)

input1 = input()

Applicant.app_details()
print('Email sent to NEW applicants about the details\n')

input1 = input()

Interview.give_interview_slot()

print('Reserve an interview slot to the Applicants.\n')

input1 = input()

query_for_details = Applicant.select(Applicant, Interview)\
    .join(Interview)\
    .where(Applicant.status == 'In progress')


for applicant in query_for_details:
    print(applicant.last_name, applicant.first_name, "Interview slot:", applicant.interview.date)

input1 = input()

Applicant.app_details_for_interview()
print('\nEmail sent to applicants about interview details\n')
'''
Applicant.interview_details_for_mentor()
print('\nmentors got emails about interviews\n')
'''