from flask import *
from models import *
from form import Form
from flask.ext.login import LoginManager
from user import *

app = Flask(__name__)

# Log in logic
login_manager = LoginManager()
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

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
        return 'You are know registered to Codecool !'
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
        result = Applicant.filter_mentor(filter.replace(" ", ""))
        try:
            return render_template('filter_result.html', result=result)
        except:
            return "Mentor not found! Please go back, and correct the name ! "
    else:
        return 'Not working'


if __name__ == '__main__':
    app.run(debug=True)
