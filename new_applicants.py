# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!

from models import *
import random

cities = []
for i in range(0, 5):
    random_query = City.select().order_by(fn.Random())
    one_city = random_query.get()
    cities.append(one_city)

'''applicants = [{'application_code': 0, 'first_name': 'Dóri', 'last_name': 'Medgyasszay',
               'gender': 'female', 'email_address': 'dorim@gmail.com', 'city': cities[0], 'status': 'New'},
              {'application_code': 0, 'first_name': 'Márk', 'last_name': 'Makai',
               'gender': 'male', 'email_address': 'makaimark@gmail.com', 'city': cities[1], 'status': 'New'},
              {'application_code': 0, 'first_name': 'Dani', 'last_name': 'Salamon',
               'gender': 'male', 'email_address': 'dani@gmail.com', 'city': cities[2], 'status': 'New'},
              {'application_code': 0, 'first_name': 'Gábor', 'last_name': 'Seres',
               'gender': 'male', 'email_address': 'sgabi@gmail.com', 'city': cities[3], 'status': 'New'},
              {'application_code': 0, 'first_name': 'Dani', 'last_name': 'Kincses',
               'gender': 'male', 'email_address': 'danikincs@gmail.com', 'city': cities[4], 'status': 'New'}
              ]

for applicant in applicants:
    Applicant.create(**applicant)'''

Applicant.check_app_code()