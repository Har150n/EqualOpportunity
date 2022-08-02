# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from Application import Application
import Application
from Employer import appRequest
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

# create the application object
app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')

# Route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('openApp'))
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    print('1')
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

#page to send in new applicatoin
@app.route('/application/')
def applicationform():
    return render_template('applicationform.html')


#page to create a new job position
@app.route('/apprequest/')
def apprequestform():
    return render_template('apprequestform.html')

#reads added employee app requests
def readAppRequests(file):
    list = []
    with open(file) as f:
        lines = f.readlines()
        f.close()
    i = 0
    while i < len(lines):
        tup = (lines[i], lines[i+1], lines[i+2], lines[i+3], lines[i+4])

        list.append(tup)
        i += 5

    return list

def writeAppRequests(file, app):
    with open(file, 'a') as w:
        w.write(app.position +"\n")
        w.write(app.company+"\n")
        w.write(app.deadline+"\n")
        w.write(app.gpa+"\n")
        w.write(app.workEligibility+"\n")
        w.close()





headings = ("Position", "Company", "Submission closes on:","Minimum GPA", "Work Visa")


@app.route('/openApp/')
@login_required
def openApp():
    data = readAppRequests("./appRequests.txt")
    return render_template('appWebsite.html', headings = headings, data = data)

@app.route('/applicationdisplay', methods= ['POST', 'GET'])
def applicationdisplay():
    if request.method == 'POST':
        form_data = request.form
        name = form_data.get("Name")
        city = form_data.get("GPA")
        country = form_data.get("Country")
        gpa = form_data.get("GPA")
        workEligibility = form_data.get("Work Eligibility")
        coverLetter = form_data.get("Cover Letter")
        resume = form_data.get("Resume")
        new_app = Application(name, gpa, workEligibility, coverLetter, resume)
        return render_template('applicationdisplay.html', form_data=form_data)


@app.route('/apprequestdisplay', methods = ['POST', 'GET'])
def apprequestdisplay():
    if request.method == 'POST':
        form_data = request.form
        gpa = form_data.get("GPA")
        workEligibility = form_data.get("Work Eligibility")
        position = form_data.get("Position")
        company = form_data.get("Company")
        deadline = form_data.get("Deadline")
        newAppRequest = appRequest(position, company, deadline, gpa, workEligibility) #creates new application
        writeAppRequests("./appRequests.txt", newAppRequest)
        return render_template('apprequestdisplay.html', form_data=form_data)

@app.route('/about')
def about():
    return render_template('about.html')






# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
