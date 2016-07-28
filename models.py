
from peewee import *
import config
import random

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
db = PostgresqlDatabase(config.dbname, user=config.name)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class School(BaseModel):
    location = CharField()
    name = CharField()


class City(BaseModel):
    name = CharField()
    school = ForeignKeyField(School, related_name='city_of_school')


class Applicant(BaseModel):
    application_code = IntegerField(default=0)
    first_name = CharField()
    last_name = CharField()
    gender = CharField()
    email_address = CharField(unique=True)
    city = CharField()
    status = CharField(default='New')
    school = ForeignKeyField(City, related_name='school_of_applicant', default=None, null=True)


    @staticmethod
    def check_app_code():
        update_query_for_code = Applicant.select().where(Applicant.application_code == 0)

        for applicant in update_query_for_code:
            random.seed(applicant.id)
            random_code = random.randint(10000, 99999)
            applicant.application_code = random_code
            applicant.save()

    @staticmethod
    def check_for_school():
        update_query_for_school = Applicant.select().where(Applicant.status == 'New')

        for applicant in update_query_for_school:
            for city in City.select():
                if applicant.city == city.name:
                    applicant.school = city.school
                    applicant.save()


class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    city = CharField()
    school = ForeignKeyField(School, related_name='school_of_mentor')


class Interview(BaseModel):
    applicant = ForeignKeyField(Applicant, related_name='applicant_to_interview')
    mentor = ForeignKeyField(Mentor, related_name='mentor_of_interview')
    date = DateTimeField()

    @staticmethod
    def give_interview_slot():
        interview_query = Applicant.select().where(Applicant.status == 'New')


        for applicant in interview_query:
            free_slot = InterviewSlot.select().join(Mentor).join(Applicant, on=Applicant.school==Mentor.school).where(InterviewSlot.is_reserved == False, Applicant.city == Mentor.city).order_by(InterviewSlot.start.asc()).get()
            Interview.create(applicant =applicant.id, mentor = free_slot.mentor, date =  free_slot.start)
            applicant.status = 'in progress'
            applicant.save()
            free_slot.is_reserved = True
            free_slot.save()

class InterviewSlot(BaseModel):
    mentor = ForeignKeyField(Mentor, related_name='free_mentor')
    start = DateTimeField()
    end = DateTimeField()
    is_reserved = BooleanField()
