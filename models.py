
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
    email_address= CharField(unique=True)
    city = ForeignKeyField(City, related_name='city_of_applicant')
    status = CharField(default='New')


    @staticmethod
    def check_app_code():
        update_query = Applicant.select().where(Applicant.application_code == 0)

        for applicant in update_query:
            random.seed(applicant.id)
            random_code = random.randint(10000, 99999)
            applicant.application_code = random_code
            applicant.save()

class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, related_name='school_of_mentor')

class Interview(BaseModel):
    applicant = ForeignKeyField(Applicant, related_name='applicant_to_interview')
    mentor = ForeignKeyField(Mentor, related_name='mentor_of_interview')
    date = DateField()

    @staticmethod
    def give_interview_slot():
        interview_query = Applicant.select().where(Applicant.status == 'New')


        for applicant in interview_query:
            free_slot = InterviewSlot.select().where(InterviewSlot.is_reserved == False).get()
            Interview.create(applicant =applicant.id, mentor = free_slot.mentor,date =  free_slot.start)
            applicant.status = 'in progress'
            applicant.save()
            free_slot.is_reserved = True
            free_slot.save()


class InterviewSlot(BaseModel):
    mentor = ForeignKeyField(Mentor, related_name='free_mentor')
    start = DateTimeField()
    end = DateTimeField()
    is_reserved = BooleanField()