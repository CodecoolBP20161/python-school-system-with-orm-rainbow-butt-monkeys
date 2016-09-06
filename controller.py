import config
import datetime
from flask import *
from models import *
from form import Form

app = Flask(__name__)

@app.route("/", methods=["GET"])
def render():
    return render_template('menu.html')


@app.route("/form", methods=["GET"])
def form():
    return render_template('form.html')


@app.route("/registration", methods=["POST"])
def get_applicant():
    form = Form(request.form)
    check = form.check()
    if check == True:
        return 'OKAY'
    else:
        return check + "\n\n Please go back to the form"

    input1 = input()
    return redirect(config.address)


@app.route('/admin', methods=['GET'])
def empty_filter():
    return render_template('filter_menu.html')

@app.route('/admin', methods=['POST'])
def list_applicants():
    option = request.form['Filter By']
    filter = request.form['filter']
    if option == 'Status':
        Applicant.filter_status(filter)
    elif option == 'Time':
        Applicant.filter_reg_time(filter)
    elif option == 'Location':
        Applicant.filter_location(filter)
    elif option == 'Name':
        Applicant.filter_name(filter)
    elif option == 'Email':
        Applicant.filter_email(filter)
    elif option == 'School':
        Applicant.filter_school(filter)
    elif option == 'Mentor name':
        Applicant.filter_mentor(filter)
    else:
        return 'Not working'


if __name__ == '__main__':
    app.run(debug=True)