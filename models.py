
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
    school = ForeignKeyField(School,related_name = 'school_of_mentor')

class Interview(BaseModel):
    applicant_code = ForeignKeyField(Applicant, related_name='applicant_to_interview')
    mentor = ForeignKeyField(Mentor, related_name='mentor_of_interview')
    date = DateField()

class InterviewSlot(BaseModel):
    mentor = ForeignKeyField(Mentor, related_name='free_mentor')
    start = DateTimeField()
    end = DateTimeField()
    is_reserved = BooleanField()