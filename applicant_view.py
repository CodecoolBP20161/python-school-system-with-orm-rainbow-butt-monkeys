from models import *


def application_details(app_code):  # search for the Applicant school name, and status by the given Application code.
    app_details_querry = (
        Applicant.select(
            Applicant,
            School
        )
            .join(School)
            .where(
            Applicant.application_code == app_code
        ))

    for i in app_details_querry:  # Print out the informations we need
        print(", Your School:", i.school.name, ", Your Status:", i.status)


def interview_details(app_code):  # search for the Applicant school name, Her/His mentor's full name, and the date.
    interview_details_querry = (
        Applicant.select(
            Applicant,
            Interview,
            Mentor
        )
            .join(Interview)
            .join(Mentor)
            .where(
            Applicant.application_code == app_code
        ).naive())

    for i in interview_details_querry:
        print("Your School:", i.school.name, ", Your Mentor:", i.last_name, i.first_name,
              ", Your Interview date:", i.date)
