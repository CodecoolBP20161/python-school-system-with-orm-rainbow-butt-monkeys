import config
import datetime
from flask import *
from models import *


app = Flask(__name__)

@app.route("/", methods=["GET"])
def render():
    return render_template('form.html')


@app.route("/form", methods=["POST"])
def get_applicant():
    now = datetime.datetime.now()
    date = str(now.year) +"-" + str(now.month) +"-" + str(now.day)
    Applicant.create(first_name = request.form["first_name"],
                     last_name = request.form["last_name"],
                     gender = request.form["gender"],
                     email_address = request.form["email_address"],
                     city = request.form["city"],
                     registration_time = date)
    return redirect(config.address)




if __name__ == '__main__':
    app.run(debug=True)