from models import *


def reserve_date():
    query = InterviewSlot.select().where(InterviewSlot.is_reserved=False)
    print(query)

new_applicants = Applicant.select().where(Applicant.status =='New')
for applicant in new_applicants:
    print(applicant.first_name, applicant.last_name)
