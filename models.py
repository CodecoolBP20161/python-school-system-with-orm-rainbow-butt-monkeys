from peewee import *
import config
import random
import email_sender

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
db = PostgresqlDatabase(config.dbname, user=config.name)


class BaseModel(Model):  # Main Class with the database connection.
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db


class School(BaseModel):  # School class only for information.
    location = CharField()
    name = CharField()


class City(BaseModel):  # Ensure connection between School and Applicant.
    name = CharField()
    school = ForeignKeyField(School, related_name='city_of_school')


class Applicant(BaseModel):  # Main class, stores the data required.
    application_code = IntegerField(default=0)
    first_name = CharField()
    last_name = CharField()
    gender = CharField()
    email_address = CharField(unique=True)
    city = CharField()
    status = CharField(default='New')
    school = ForeignKeyField(School, related_name='school_of_applicant', default=None, null=True)
    registration_time = DateField()

    @staticmethod
    def app_details():
        query_for_details = Applicant.select(Applicant, School).join(School).where(Applicant.status == 'New')
        for applicant in query_for_details:
            # smtp call
            email_sender.Emailsender.send_email(applicant.email_address, applicant.first_name,
                                                applicant.application_code, applicant.school.location)

    @staticmethod
    def app_details_for_interview():
        mentors = []
        interview_query = Interview.select()
        for interview in interview_query:
            mentor_query = MentorInterview.select(MentorInterview)\
                .where(MentorInterview.interview == interview.id)
            for i in mentor_query:
                print(i.mentor.id)
                mentors.append(i.mentor)
            email_sender.Emailsender.send_email_for_interview(interview.applicant.email_address,
                                                              interview.applicant.first_name,
                                                              mentors[0].first_name,mentors[1].first_name, interview.date)
            mentors = []

    @staticmethod
    def interview_details_for_mentor():
        mentor_query = Mentor.select()
        for mentor in mentor_query:
            query = MentorInterview.select(MentorInterview, Interview) \
                .join(Interview, on=Interview.id==MentorInterview.interview) \
                .where(MentorInterview.mentor == mentor.id)
            for interview in query:
                email_sender.Emailsender.send_email_to_mentor(mentor.email_address, mentor.first_name,
                                                        interview.interview.applicant.first_name, interview.interview.date)


    @staticmethod
    def filter_status(input_status):
        for applicant in Applicant.select().where(Applicant.status == input_status):
            print(applicant.first_name, applicant.last_name)

    @staticmethod
    def filter_reg_time(reg_time):
        for applicant in Applicant.select().where(Applicant.registration_time == reg_time):
            print(applicant.first_name, applicant.last_name)

    @staticmethod
    def filter_location(input_location):  # we are waiting for the city of the applicant
        for applicant in Applicant.select().where(Applicant.city == input_location):
            print(applicant.first_name, applicant.last_name)

    @staticmethod
    def filter_name(input_name):
        for applicant in Applicant.select().where((Applicant.first_name.contains(input_name) |
                                                       (Applicant.last_name.contains(input_name)))):
            print(applicant.first_name, applicant.last_name)

    @staticmethod
    def filter_email(input_email):
        for applicant in Applicant.select().where(Applicant.email_address == input_email):
            print(applicant.first_name, applicant.last_name)

    @staticmethod
    def filter_school(input_school):
        look_for_school_id = School.get(School.location == input_school)
        for applicant in Applicant.select().where(Applicant.school == look_for_school_id.id):
            print(applicant.first_name, applicant.last_name)

    @staticmethod
    def filter_mentor(input_mentor_lastname):
        mentor = Mentor.get(Mentor.last_name == input_mentor_lastname)
        for interview in mentor.interviews:
            print(interview.applicant.first_name, interview.applicant.last_name)

    @staticmethod
    def check_app_code():  # Generate a uniqe code for every new applicant.
        update_query_for_code = Applicant.select().where(Applicant.application_code == 0)

        for applicant in update_query_for_code:
            random_code = random.randint(10000, 99999)
            applicant.application_code = random_code
            applicant.save()

    @staticmethod
    def check_for_school():  # Assign a school to every applicant, based on their city.
        update_query_for_school = Applicant.select().where(Applicant.status == 'New')

        for applicant in update_query_for_school:
            for city in City.select():
                if applicant.city == city.name:
                    applicant.school = city.school
                    applicant.save()

    @staticmethod
    def application_details(
            app_code):  # search for the Applicant school name, and status by the given Application code.
        app_details_querry = (
            Applicant.select(
                Applicant,
                School
            )
                .join(School)
                .where(
                Applicant.application_code == app_code
            ))

        for i in app_details_querry:  # Print out the informations we need
            print(" Your School:", i.school.name, ", Your Status:", i.status)


class Mentor(BaseModel):  # normal data, and their school
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, related_name='school_of_mentor')
    email_address = CharField()

    @staticmethod
    def interview_details(mentor_id):
        query = MentorInterview.select(MentorInterview, Interview) \
            .join(Interview, on=Interview.id == MentorInterview.interview) \
            .where(MentorInterview.mentor == mentor_id)
        for interview in query:
            print("\nDate of interview: ", interview.interview.date, "\nName of applicant: ", interview.interview.applicant.first_name, "",
                  interview.interview.applicant.last_name, "\nApplication code: ", interview.interview.applicant.application_code)


class Interview(BaseModel):  # Stores reserved interview slots
    applicant = ForeignKeyField(Applicant, related_name='interview')
    # mentor = ForeignKeyField(Mentor, related_name='interviews')
    date = DateTimeField()

    @staticmethod
    def give_interview_slot():
        interview_query = Applicant.select().where(Applicant.status == 'New')

        for applicant in interview_query:
            interview_slot_query = InterviewSlot.select().where(InterviewSlot.is_reserved == False).order_by(
                InterviewSlot.start)
            for slot in interview_slot_query:
                if slot.mentor.school == applicant.school:
                    interview = Interview.create(applicant=applicant.id, mentor=slot.mentor, date=slot.start)
                    MentorInterview.create(mentor=slot.mentor, interview=interview)
                    applicant.status = 'In progress'
                    applicant.save()
                    slot.is_reserved = True
                    slot.save()
                    interview_slot_query2 = InterviewSlot.select().where(InterviewSlot.is_reserved == False).order_by(
                        InterviewSlot.start)
                    for slot2 in interview_slot_query2:
                        if slot2.mentor.school == slot.mentor.school and slot2.start == slot.start:
                            MentorInterview.create(mentor=slot2.mentor, interview=interview)
                            slot2.is_reserved = True
                            slot2.save()
                    break

    @staticmethod
    def interview_details(applicant):  # search for the Applicant school name, Her/His mentor's full name, and the date.
        mentors_query = (
            Mentor.select()
                .join(MentorInterview)
                .join(Interview)
                .where(
                applicant.interview.id == MentorInterview.interview.id
            ))

        for i in mentors_query:
            print("Your School:", i.school.name, ", Your Mentor:", i.last_name, i.first_name,
                  ", Your Interview date:", i.interview.reserved_slot.date)


class MentorInterview(BaseModel):
    mentor = ForeignKeyField(Mentor, related_name='interview')
    interview = ForeignKeyField(Interview, related_name='reserved_slot')


class InterviewSlot(BaseModel):
    mentor = ForeignKeyField(Mentor, related_name='free_slot')
    start = DateTimeField()
    end = DateTimeField()
    is_reserved = BooleanField()
