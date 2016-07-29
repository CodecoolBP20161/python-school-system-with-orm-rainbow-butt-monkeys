from models import *

def application_details(app_code):
    details_querry = (
        Applicant.select(
            Applicant,
            School
        )
            .join(School)
            .where(
            Applicant.application_code == app_code
        ))

    for i in details_querry:
        print(", Your School:", i.school.name, ", Your Status:", i.status)
