from models import *


def give_interview_slot():
    interview_query = Applicant.select().where(Applicant.status == 'New')

    for applicant in interview_query:
        interview_slot_query = InterviewSlot.select().where(InterviewSlot.is_reserved == False).order_by(
            InterviewSlot.start)
        for slot in interview_slot_query:
            if slot.mentor.school == applicant.school:
                interview = Interview.create(applicant=applicant.id, mentor=slot.mentor, date=slot.start)
                MentorInterview.create(mentor=slot.mentor, interview=interview)
                applicant.status = 'In progress'
                applicant.save()
                slot.is_reserved = True
                slot.save()
                interview_slot_query2 = InterviewSlot.select().where(InterviewSlot.is_reserved == False).order_by(
                    InterviewSlot.start)
                for slot2 in interview_slot_query2:
                    if slot2.mentor.school == slot.mentor.school and slot2.start == slot.start:
                        MentorInterview.create(mentor=slot2.mentor, interview=interview)
                        slot2.is_reserved = True
                        slot2.save()
                break

Applicant.check_for_school()

give_interview_slot()