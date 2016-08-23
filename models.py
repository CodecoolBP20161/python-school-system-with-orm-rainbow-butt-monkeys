
from peewee import *
import config
import random

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
db = PostgresqlDatabase(config.dbname, user=config.name)


class BaseModel(Model):  # Main Class with the database connection.
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class School(BaseModel):  # School class only for information.
    location = CharField()
    name = CharField()


class City(BaseModel):  # Ensure connection between School and Applicant.
    name = CharField()
    school = ForeignKeyField(School, related_name='city_of_school')


class Applicant(BaseModel):  # Main class, stores the data required.
    application_code = IntegerField(default=0)
    first_name = CharField()
    last_name = CharField()
    gender = CharField()
    email_address = CharField(unique=True)
    city = CharField()
    status = CharField(default='New')
    school = ForeignKeyField(School, related_name='school_of_applicant', default=None, null=True)
    registration_time = DateField()

    @staticmethod
    def filter_status(input_status):
        query_for_status = Applicant.select().where(Applicant.status == input_status)
        for i in query_for_status:
            print(i.first_name, i.last_name)

    @staticmethod
    def filter_reg_time(reg_time):
        query_for_regtime = Applicant.select().where(Applicant.registration_time == reg_time)
        for i in query_for_regtime:
            print(i.first_name, i.last_name)

    @staticmethod
    def filter_location(input_location):    # we are waiting for the city of the applicant
        query_for_location = Applicant.select().where(Applicant.city == input_location)
        for i in query_for_location:
            print(i.first_name, i.last_name)

    @staticmethod
    def filter_name(input_name):
        query_for_name = Applicant.select().where(Applicant.first_name == input_name)
        for i in query_for_name:
            print(i.first_name, i.last_name)
        query_for_name = Applicant.select().where(Applicant.last_name == input_name)
        for i in query_for_name:
            print(i.first_name, i.last_name)

    @staticmethod
    def filter_email(input_email):
        query_for_email = Applicant.select().where(Applicant.email_address == input_email)
        for i in query_for_email:
            print(i.first_name, i.last_name)

    @staticmethod
    def filter_school(input_school):
        look_for_school_id = School.select().where(School.location == input_school).get()
        query_for_school = Applicant.select().where(Applicant.school == look_for_school_id.id)
        for i in query_for_school:
            print(i.first_name, i.last_name)

    @staticmethod
    def filter_mentor(input_mentor_lastname):
        mentor = Mentor.get(Mentor.last_name == input_mentor_lastname)
        for interview in mentor.interviews:
            print(interview.applicant.first_name, interview.applicant.last_name)
            
    @staticmethod
    def check_app_code():  # Generate a uniqe code for every new applicant.
        update_query_for_code = Applicant.select().where(Applicant.application_code == 0)

        for applicant in update_query_for_code:
            random_code = random.randint(10000, 99999)
            applicant.application_code = random_code
            applicant.save()

    @staticmethod
    def check_for_school():  # Assign a school to every applicant, based on their city.
        update_query_for_school = Applicant.select().where(Applicant.status == 'New')

        for applicant in update_query_for_school:
            for city in City.select():
                if applicant.city == city.name:
                    applicant.school = city.school
                    applicant.save()

    @staticmethod
    def application_details(
            app_code):  # search for the Applicant school name, and status by the given Application code.
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
            print(" Your School:", i.school.name, ", Your Status:", i.status)

class Mentor(BaseModel):  # normal data, and their school
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, related_name='school_of_mentor')


    @staticmethod
    def interview_details(mentor_id):
        interview_query = Interview.select(Interview, Applicant).join(Applicant).where(Interview.mentor == mentor_id)
        for interview in interview_query:
            print("\nDate of interview: ", interview.date, "\nName of applicant: ", interview.applicant.first_name, "",
                  interview.applicant.last_name, "\nApplication code: ", interview.applicant.application_code)


class Interview(BaseModel):  # Stores reserved interview slots
    applicant = ForeignKeyField(Applicant, related_name='interview')
    mentor = ForeignKeyField(Mentor, related_name='interviews')
    date = DateTimeField()

    @staticmethod
    def give_interview_slot():
        interview_query = Applicant.select().where(Applicant.status == 'New')

        for applicant in interview_query:
            interview_slot_query = InterviewSlot.select().where(InterviewSlot.is_reserved == False).order_by(InterviewSlot.start)
            for slot in interview_slot_query:
                if slot.mentor.school == applicant.school:
                    Interview.create(applicant=applicant.id, mentor = slot.mentor, date = slot.start)
                    applicant.status = 'In progress'
                    applicant.save()
                    slot.is_reserved = True
                    slot.save()
                    break

    @staticmethod
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


class InterviewSlot(BaseModel):
    mentor = ForeignKeyField(Mentor, related_name='free_mentor')
    start = DateTimeField()
    end = DateTimeField()
    is_reserved = BooleanField()
