from models import *

# Write here your console application



Applicant.check_app_code()
print('Add application codes to the Applicants.')
app_querry = Applicant.select()
for i in app_querry:
    print(i.last_name, i.first_name,"Applicant code:", i.application_code)

Applicant.check_for_school()
print('Assign school to the Applicants.')
app_querry_2 = Applicant.select()
for i in app_querry_2:
    print(i.last_name, i.first_name, "School:", i.school.location)

Interview.give_interview_slot()

print('Reserve an interview slot to the Applicants.')
query_for_details = Interview.select(Applicant, Interview, Mentor) \
                    .join(Applicant, on=Applicant.id == Interview.applicant) \
                    .join(Mentor, on=Mentor.id == Interview.mentor) \
                    .where(Applicant.status == 'In progress')

for i in query_for_details:
    print(i.applicant.last_name, i.applicant.first_name, "Interview slot:", i.date)

Applicant.app_details()
print('Email sent to  NEW applicants about the details')

Applicant.app_details_for_interview()
print('Email sent to applicants about interview details')

Applicant.interview_details_for_mentor()
print('mentors got emails about interviews')
