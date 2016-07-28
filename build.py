# This script can create the database tables based on your models

from models import *

db.connect()
# List the tables here what you want to create...

print("Drop tables")  # Drop all tables automatic.
db.drop_tables([Applicant, School, City, Mentor, Interview, InterviewSlot], safe=True)
print("Create tables")  # Create all tables automatic.
db.create_tables([Applicant, School, City, Mentor, Interview, InterviewSlot], safe=True)
