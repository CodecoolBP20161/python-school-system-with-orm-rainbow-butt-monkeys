from flask import *
from models import *
from form import Form
from flask import session
from user import *
from flask_login import login_user , logout_user , current_user , login_required, LoginManager
from flask.ext.session import Session
from functools import wraps


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
@login_required
def empty_filter():
    return render_template('filter_menu.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        if session['logged_in'] is False :
            return render_template('log_in.html')
        else:
            return render_template('filter_menu.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            registered_user = User.get(User.username == username, User.password == password)
            session['logged_in'] = True
            return redirect(config.address + '/admin')
        except User.DoesNotExist:
            return 'Username or Password is invalid'


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap


@app.route('/logout')
def logout():
    logout_user()
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
