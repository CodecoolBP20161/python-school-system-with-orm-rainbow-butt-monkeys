# This script can generate example data for "City" and "InterviewSlot" models.

from models import *

codecool_bp = School.create(location = 'Budapest', name = 'Codecool_Budapest')
codecool_miskolc = School.create(location = 'Miskolc', name = 'Codecool_Miskolc')
codecool_krakow = School.create(location = 'Krakow', name = 'Codecool_Krakow')

cities = [{'name': 'Budapest', 'school': codecool_bp}, {'name': 'Lillafüred', 'school': codecool_miskolc},
          {'name': 'Balatonlelle', 'school': codecool_bp}, {'name': 'Warsav', 'school': codecool_krakow},
          {'name': 'Pusztaszentjakab', 'school': codecool_miskolc}, {'name': 'Sopron', 'school': codecool_bp}]

for city in cities:
    City.create(name=city['name'], school=city['school'])


codecool_bp = School.select().where(School.location == "Budapest")
codecool_miskolc = School.select().where(School.location == "Miskolc")
codecool_krakow = School.select().where(School.location == "Krakow")


applicants = [{'first_name': 'Dóri', 'last_name': 'Medgyasszay',
               'gender': 'female', 'email_address': 'dorim@gmail.com', 'city': 'Sopron', 'status': 'New'},
              { 'first_name': 'Márk', 'last_name': 'Makai',
               'gender': 'male', 'email_address': 'makaimark@gmail.com', 'city': 'Balatonlelle', 'status': 'New'},
              { 'first_name': 'Dani', 'last_name': 'Salamon',
               'gender': 'male', 'email_address': 'dani@gmail.com', 'city': 'Budapest', 'status': 'New'},
              {'first_name': 'Gábor', 'last_name': 'Seres',
               'gender': 'male', 'email_address': 'sgabi@gmail.com', 'city': 'Pusztaszentjakab', 'status': 'New'},
              { 'first_name': 'Dani', 'last_name': 'Kincses',
               'gender': 'male', 'email_address': 'danikincs@gmail.com', 'city': 'Warsav', 'status': 'New'}
              ]

for applicant in applicants:
    Applicant.create(**applicant)

mentors = [{'first_name': 'Miki', 'last_name': 'Beöthy', 'school': codecool_bp},
           {'first_name': 'Tomi', 'last_name': 'Tompa', 'school': codecool_bp},
           {'first_name': 'Dani', 'last_name': 'Salamon', 'school': codecool_bp},
           {'first_name': 'Mateus', 'last_name': 'Grabowski', 'school': codecool_krakow}]

for mentor in mentors:
    Mentor.create(**mentor)


mentors = Mentor.select()
interview_slots = [{'mentor': mentors[0], 'start': '2016-08-01 12:00:00', 'end': '2016-08-01 13:00:00', 'is_reserved': False},
                   {'mentor': mentors[1], 'start': '2016-08-01 14:00:00', 'end': '2016-08-01 15:00:00','is_reserved': False},
                   {'mentor': mentors[2], 'start': '2016-08-01 12:00:00', 'end': '2016-08-01 13:00:00','is_reserved': False},
                   {'mentor': mentors[2], 'start': '2016-08-04 12:00:00', 'end': '2016-08-04 13:00:00','is_reserved': False},
                    {'mentor': mentors[1], 'start': '2016-08-07 12:00:00', 'end': '2016-08-07 13:00:00','is_reserved': False}]

for slot in interview_slots:
    InterviewSlot.create(**slot)
