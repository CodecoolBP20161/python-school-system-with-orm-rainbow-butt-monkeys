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
        return 'Registration form uploaded to the database'
        # return redirect(config.address)
    else:
        return check + "\n\n Please go back to the form"



@app.route('/admin', methods=['GET'])
def empty_filter():
    return render_template('filter_menu.html')

@app.route('/admin', methods=['POST'])
def list_applicants():
    option = request.form['Filter By']
    filter = request.form['filter']
    if option == 'Status':
        result = Applicant.filter_status(filter)
        return render_template('filter_result.html', result=result)
    elif option == 'Time':
        result = Applicant.filter_reg_time(filter)
        return render_template('filter_result.html', result=result)
    elif option == 'Location':
        result = Applicant.filter_location(filter)
        return render_template('filter_result.html', result=result)
    elif option == 'Name':
        result = Applicant.filter_name(filter)
        return render_template('filter_result.html', result=result)
    elif option == 'Email':
        result = Applicant.filter_email(filter)
        return render_template('filter_result.html', result=result)
    elif option == 'School':
        result = Applicant.filter_school(filter)
        return render_template('filter_result.html', result=result)
    elif option == 'Mentor name':
        result = Applicant.filter_mentor(filter)
        return render_template('filter_result.html', result=result)
    else:
        return 'Not working'


if __name__ == '__main__':
    app.run(debug=True)