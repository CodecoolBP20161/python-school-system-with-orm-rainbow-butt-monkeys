# This script can generate example data for "City" and "InterviewSlot" models.

from models import *


'''codecool_budapest = School.create(location = 'Budapest', name = 'Codecool_Budapest')
codecool_miskolc = School.create(location = 'Miskolc', name = 'Codecool_Miskolc')
codecool_krakow = School.create(location = 'Krakow', name = 'Codecool_Krakow')

cities = [{'name': 'Budapest', 'school': codecool_budapest}, {'name': 'Lillafüred', 'school': codecool_miskolc},
          {'name': 'Balatonlelle', 'school': codecool_budapest}, {'name': 'Warsav', 'school': codecool_krakow},
          {'name': 'Pusztaszentjakab', 'school': codecool_miskolc}, {'name': 'Sopron', 'school': codecool_budapest}]

for city in cities:
    City.create(name=city['name'], school=city['school'])'''





'''query = Applicant.select(Applicant.first_name, Applicant.last_name, Applicant.city.name).get()
print(query.first_name)'''

'''
codecool_bp = School.select().where(School.location == "Budapest")
codecool_miskolc = School.select().where(School.location == "Miskolc")
codecool_krakow = School.select().where(School.location == "Krakow")

mentors = [{'first_name': 'Miki', 'last_name': 'Beöthy', 'school': codecool_bp},
           {'first_name': 'Tomi', 'last_name': 'Tompa', 'school': codecool_bp},
           {'first_name': 'Dani', 'last_name': 'Salamon', 'school': codecool_bp},
           {'first_name': 'Mateus', 'last_name': 'Grabowski', 'school': codecool_krakow}]

for mentor in mentors:
    Mentor.create(**mentor)
'''

