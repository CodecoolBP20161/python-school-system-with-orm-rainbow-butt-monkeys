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



random_query = City.select().order_by(fn.Random())
one_city = random_query.get()

"""applicant_1 = Applicant.create(
    application_code ='None',
    first_name = 'Dani',
    last_name = 'Kincses',
    gender ='male',
    email_address ='danikincs@gmail.com',
    city = one_city,
    status = 'New')"""

query = Applicant.select(Applicant.first_name, Applicant.last_name, Applicant.city.name).get()
print(query.first_name)


