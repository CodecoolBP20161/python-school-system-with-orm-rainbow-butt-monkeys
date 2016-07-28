from models import *
import logging
logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

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