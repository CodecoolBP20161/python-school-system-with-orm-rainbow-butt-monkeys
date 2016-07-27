
from peewee import *
import config

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
    application_code = CharField()
    first_name = CharField()
    last_name = CharField()
    gender = CharField()
    email_address= CharField(unique=True)
    city = ForeignKeyField(City, related_name='city_of_applicant')
    status = CharField(default='New')