from models import *
import datetime

class Form():

    def __init__(self, request_form):
        self.first_name = request_form['first_name']
        self.last_name = request_form['last_name']
        self.gender = request_form['gender']
        self.email_address = request_form['email_address']
        self.city = request_form['city']

    @staticmethod
    def is_digit(string):
        for char in list(string):
            if char.isdigit():
                return True

    def check(self):
        if self.first_name == "":
            return "Enter first name!"
        elif self.last_name == "":
            return "Enter last name!"
        elif self.gender == "":
            return "Select an option!"
        elif self.email_address == "":
            return "Enter email address!"
        elif self.city == "":
            return "Select an option!"
        elif self.is_digit(self.first_name) or self.is_digit(self.last_name) is True:
            return "Your first name or last name contains a number, pls check it again!"
        else:
            now = datetime.datetime.now()
            date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
            Applicant.create(first_name=self.first_name,
                             last_name=self.last_name,
                             gender=self.gender,
                             email_address=self.email_address,
                             city=self.city,
                             registration_time=date)
            return True
