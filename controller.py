from flask import *
from models import *
from form import Form
from flask import session
from user import *
from flask_login import login_user , logout_user , current_user , login_required, LoginManager
from flask.ext.session import Session


app = Flask(__name__)
SESSION_TYPE = 'filesystem'

sess = Session()


# Log in logic
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id):
    return User.get(User.id == id)


@app.route('/admin', methods=['GET'])
def empty_filter():
    if session["logged_in"] is True:
        return render_template('filter_menu.html')
    else:
        return redirect(config.address + "/login")


@app.route('/login', methods=['GET'])
def login_render():
    return render_template('log_in.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    try:
        registered_user = User.get(User.username == username, User.password == password)
        session['logged_in'] = True
        return redirect(config.address + '/admin')
    except User.DoesNotExist:
        return 'Username or Password is invalid'


@app.route('/login/applicant', methods=['POST'])
def login_applicant():
    e_mail = request.form['username']
    registration_code = request.form['password']
    try :
        registered_applicant = Applicant.get(Applicant.email_address == e_mail,
                                             Applicant.application_code == registration_code)
        session['applicant_logged_in'] = True
        return redirect(config.address + '/profil')
    except User.DoesNotExist:
        return 'E-mail or Password is invalid'



@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(config.address + "/")


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


@app.route('/admin', methods=['POST'])
def list_applicants():
    option = request.form['Filter By']
    filter = request.form['filter']

    if option == 'Name':
        result = Applicant.filter_name(filter)
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
        result = Applicant.filter_by(filter, option)
        return render_template('filter_result.html', result=result)


@app.route('/admin_int', methods=['POST'])
def list_interviews():
    option = request.form['interview_filter']
    filter = request.form['Filter By']
    if option == 'School':
        try:
            result = Interview.filter_by_school(filter)
            return render_template('filter_interviews.html', result=result)
        except:
            return "invalid school location"
    elif option == 'Applicant':
        try:
            result = Interview.filter_by_applicant(filter)
            return render_template('filter_interviews.html', result=result)
        except:
            return "invalid applicant name"
    elif option == 'Mentor':
        try:
            result = Interview.filter_by_mentor(filter)
            return render_template('filter_interviews.html', result=result)
        except:
            return "invalid mentor name"
    elif option == 'Date':
        try:
            result = Interview.filter_by_date(filter)
            return render_template('filter_interviews.html', result=result)
        except:
            return "invalid date"
    else:
        return 'Not working!'


if __name__ == '__main__':
    app.secret_key = 'secret'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)
    app.run(debug=True)
