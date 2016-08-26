# This script will generate data for all tables

from models import *

# Fill School table with data
codecool_bp = School.create(location='Budapest', name='Codecool_Budapest')
codecool_miskolc = School.create(location='Miskolc', name='Codecool_Miskolc')
codecool_krakow = School.create(location='Krakow', name='Codecool_Krakow')

cities = [{'name': 'Budapest', 'school': codecool_bp}, {'name': 'Lillafüred', 'school': codecool_miskolc},
          {'name': 'Balatonlelle', 'school': codecool_bp}, {'name': 'Warsav', 'school': codecool_krakow},
          {'name': 'Pusztaszentjakab', 'school': codecool_miskolc}, {'name': 'Sopron', 'school': codecool_bp}]

for city in cities:
    City.create(name=city['name'], school=city['school'])


codecool_bp = School.select().where(School.location == "Budapest")
codecool_miskolc = School.select().where(School.location == "Miskolc")
codecool_krakow = School.select().where(School.location == "Krakow")

# Fill Applicant table with data:
applicants = [{'first_name': 'Dori', 'last_name': 'Medgyasszay',
               'gender': 'female', 'email_address': 'dora.medgyasszay@gmail.com', 'city': 'Sopron', 'status': 'New',
               'registration_time': '2016-07-18'},
              {'first_name': 'Mark', 'last_name': 'Makai',
               'gender': 'male', 'email_address': 'makaimark@gmail.com', 'city': 'Balatonlelle', 'status': 'New',
               'registration_time': '2016-07-28'},
              {'first_name': 'Guy', 'last_name': 'Creepy',
               'gender': 'male', 'email_address': 'shevah292@gmail.com', 'city': 'Budapest', 'status': 'New',
               'registration_time': '2016-08-08'},
              {'first_name': 'Gabor', 'last_name': 'Seres',
               'gender': 'male', 'email_address': 'sheva1h92@gmail.com', 'city': 'Pusztaszentjakab', 'status': 'New',
               'registration_time': '2016-08-28'},
              {'first_name': 'Dani', 'last_name': 'Kincses',
               'gender': 'male', 'email_address': 'shevah92@gmail.com', 'city': 'Warsav', 'status': 'New',
               'registration_time': '2016-08-11'}
              ]

for applicant in applicants:
    Applicant.create(**applicant)

app_querry = Applicant.select()
print('Applicants:')
for i in app_querry:
    print("- ", i.last_name, i.first_name,", email:", i.email_address,", City:", i.city,", Status:", i.status, i.registration_time, "-")


# Fill Mentor table with data:
mentors = [{'first_name': 'Miki', 'last_name': 'Beothy', 'school': codecool_bp, 'email_address': 'rbm.codecool+Miki@gmail.com'},
            {'first_name': 'Dani', 'last_name': 'Salamon', 'school': codecool_bp, 'email_address': 'rbm.codecool+Dani@gmail.com'},
            {'first_name': 'Tomi', 'last_name': 'Tompa', 'school': codecool_bp, 'email_address': 'rbm.codecool+Tomi@gmail.com'},
            {'first_name': 'Sandor', 'last_name': 'Szodoray', 'school': codecool_miskolc, 'email_address': 'rbm.codecool+Sandor@gmail.com'},
            {'first_name': 'Pal', 'last_name': 'Monoczki', 'school': codecool_miskolc, 'email_address': 'rbm.codecool+Pal@gmail.com'},
           {'first_name': 'Attila', 'last_name': 'Molnar', 'school': codecool_miskolc, 'email_address': 'rbm.codecool+Attila@gmail.com'},
           {'first_name': 'Leon', 'last_name': 'Aprofi', 'school': codecool_krakow, 'email_address': 'rbm.codecool+Leon@gmail.com'},
           {'first_name': 'Mateus', 'last_name': 'Grabowski', 'school': codecool_krakow, 'email_address': 'rbm.codecool+Mateus@gmail.com'}]

for mentor in mentors:
    Mentor.create(**mentor)

mentor_querry = Mentor.select()
print("Mentors:")
for i in mentor_querry:
    print("- ", i.last_name, i.first_name,", email:", i.email_address, "-")



# Fill InterviewSlot table with data:
mentors = Mentor.select()

interview_slots = [{'mentor': mentors[0], 'start': '2016-08-01 12:00:00', 'end': '2016-08-01 13:00:00',
                    'is_reserved': False},
                   {'mentor': mentors[0], 'start': '2016-08-02 12:00:00', 'end': '2016-08-01 13:00:00',
                    'is_reserved': False},
                   {'mentor': mentors[0], 'start': '2016-08-01 14:00:00', 'end': '2016-08-01 15:00:00',
                    'is_reserved': False},
                   {'mentor': mentors[1], 'start': '2016-08-01 12:00:00', 'end': '2016-08-01 13:00:00',
                   'is_reserved': False},
                   {'mentor': mentors[1], 'start': '2016-08-02 12:00:00', 'end': '2016-08-01 13:00:00',
                    'is_reserved': False},
                   {'mentor': mentors[1], 'start': '2016-08-07 14:00:00', 'end': '2016-08-07 15:00:00',
                   'is_reserved': False},
                   {'mentor': mentors[2], 'start': '2016-08-07 14:00:00', 'end': '2016-08-07 15:00:00',
                   'is_reserved': False},
                   {'mentor': mentors[2], 'start': '2016-08-01 14:00:00', 'end': '2016-08-01 15:00:00',
                    'is_reserved': False},
                   {'mentor': mentors[3], 'start': '2016-08-01 12:00:00', 'end': '2016-08-01 13:00:00',
                    'is_reserved': False},
                   {'mentor': mentors[3], 'start': '2016-08-01 14:00:00', 'end': '2016-08-01 15:00:00',
                    'is_reserved': False},
                   {'mentor': mentors[4], 'start': '2016-08-01 12:00:00', 'end': '2016-08-01 13:00:00',
                    'is_reserved': False},
                   {'mentor': mentors[4], 'start': '2016-08-07 14:00:00', 'end': '2016-08-07 15:00:00',
                    'is_reserved': False},
                   {'mentor': mentors[5], 'start': '2016-08-07 14:00:00', 'end': '2016-08-07 15:00:00',
                    'is_reserved': False},
                   {'mentor': mentors[5], 'start': '2016-08-01 14:00:00', 'end': '2016-08-01 14:00:00',
                    'is_reserved': False},
                   {'mentor': mentors[6], 'start': '2016-08-01 12:00:00', 'end': '2016-08-01 13:00:00',
                    'is_reserved': False},
                   {'mentor': mentors[6], 'start': '2016-08-07 12:00:00', 'end': '2016-08-07 13:00:00',
                    'is_reserved': False},
                   {'mentor': mentors[7], 'start': '2016-08-01 12:00:00', 'end': '2016-08-01 13:00:00',
                    'is_reserved': False},
                   {'mentor': mentors[7], 'start': '2016-08-07 12:00:00', 'end': '2016-08-07 13:00:00',
                    'is_reserved': False}
                   ]


for slot in interview_slots:
    InterviewSlot.create(**slot)

print("The tables are filled with data now.")