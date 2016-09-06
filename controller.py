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




if __name__ == '__main__':
    app.run(debug=True)