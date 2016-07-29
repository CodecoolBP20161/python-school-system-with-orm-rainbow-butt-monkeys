
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


class Mentor(BaseModel):  # normal data, and their school
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, related_name='school_of_mentor')


class Interview(BaseModel):  # Stores reserved interview slots
    applicant = ForeignKeyField(Applicant, related_name='applicant_to_interview')
    mentor = ForeignKeyField(Mentor, related_name='mentor_of_interview')
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

class InterviewSlot(BaseModel):
    mentor = ForeignKeyField(Mentor, related_name='free_mentor')
    start = DateTimeField()
    end = DateTimeField()
    is_reserved = BooleanField()
