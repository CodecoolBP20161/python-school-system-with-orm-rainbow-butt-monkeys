from models import *

def interview_details(mentor_id):
    interview_query = Interview.select(Interview, Applicant).join(Applicant).where(Interview.mentor==mentor_id)
    for interview in interview_query:
        print ("\nDate of interview: ", interview.date, "\nName of applicant: ",interview.applicant.first_name, "",
               interview.applicant.last_name, "\nApplication code: ", interview.applicant.application_code)