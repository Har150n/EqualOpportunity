# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from Application import Application
import Application
from Employer import appRequest


# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/openApp/')
def openApp():
    return render_template('openApp.html') #open applications


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


#page to send in new applicatoin
@app.route('/application/')
def applicationform():
    return render_template('applicationform.html')


#page to create a new job position
@app.route('/apprequest/')
def apprequestform():
    return render_template('apprequestform.html')




@app.route('/applicationdisplay', methods= ['POST', 'GET'])
def applicationdisplay():
    if request.method == 'POST':
        form_data = request.form
        gpa = form_data.get("GPA")
        workEligibility = form_data.get("Work Eligibility")
        newAppRequest = appRequest("deadline", "gpa", True)
        return render_template('applicationdisplay.html', form_data=form_data)

@app.route('/apprequestdisplay', methods = ['POST', 'GET'])
def apprequestdisplay():
    if request.method == 'POST':
        form_data = request.form
        gpa = form_data.get("GPA")
        workEligibility = form_data.get("Work Eligibility")
        newAppRequest = appRequest("deadline", "gpa", True)
        return render_template('apprequestdisplay.html', form_data=form_data)






# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
