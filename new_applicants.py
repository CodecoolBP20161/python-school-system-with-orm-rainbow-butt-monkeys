# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!

from models import *

applicants = [{'first_name': 'Dóri', 'last_name': 'Medgyasszay',
               'gender': 'female', 'email_address': 'dorim@gmail.com', 'city': 'Budapest', 'status': 'New'},
              { 'first_name': 'Márk', 'last_name': 'Makai',
               'gender': 'male', 'email_address': 'makaimark@gmail.com', 'city': 'Sopron', 'status': 'New'},
              { 'first_name': 'Dani', 'last_name': 'Salamon',
               'gender': 'male', 'email_address': 'dani@gmail.com', 'city': 'Warsav', 'status': 'New'},
              {'first_name': 'Gábor', 'last_name': 'Seres',
               'gender': 'male', 'email_address': 'sgabi@gmail.com', 'city': 'Pusztaszentjakab', 'status': 'New'},
              { 'first_name': 'Dani', 'last_name': 'Kincses',
               'gender': 'male', 'email_address': 'danikincs@gmail.com', 'city': 'Balatonlelle', 'status': 'New'}
              ]

for applicant in applicants:
    Applicant.create(**applicant)

Applicant.check_app_code()
Applicant.check_for_school()
