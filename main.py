from models import *

# Write here your console application


Interview.give_interview_slot()
'''
query = Interview.select()
for i in query:
    print(i.mentor.first_name, i.applicant.last_name, i.date)

applicant = Applicant.select().where(Applicant.last_name=='Kincses').get()
free_slot = InterviewSlot.select().join(Mentor, on=Mentor.id==InterviewSlot.mentor).join(School, on=applicant.school == Mentor.school).where(InterviewSlot.is_reserved == False
                                ).order_by(
                                InterviewSlot.start.asc()).get()
print(applicant.__dict__)
print(free_slot.__dict__)
'''

Applicant.check_app_code()
print('Add application codes to the Applicants.')
Applicant.check_for_school()
print('Assign school to the Applicants.')
Interview.give_interview_slot()
print('Reserve an interview slot to the Applicants.')

