# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!

from models import *


Applicant.check_app_code()
Applicant.check_for_school()
Interview.give_interview_slot()