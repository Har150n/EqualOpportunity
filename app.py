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



# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['Username'] == 'employer' and request.form['Password'] == 'employer':
            print("employer success")


            return redirect(url_for('home'))
        elif request.form['Username'] == 'applicant' and request.form['Password'] == 'applicant':
            print("applicant success")
            return redirect(url_for('openApp'))
        else:
            error = 'Invalid Credentials. Please try again.'

    return render_template('login.html', error=error)


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




headings = ("Position", "Company", "Submission closes on:","Minimum GPA", "Work Visa")
data = readAppRequests("./appRequests.txt")

@app.route('/openApp/')
def openApp():
    return render_template('appWebsite.html', headings = headings, data = data)

@app.route('/applicationdisplay', methods= ['POST', 'GET'])
def applicationdisplay():
    if request.method == 'POST':
        form_data = request.form
        gpa = form_data.get("GPA")
        workEligibility = form_data.get("Work Eligibility")
        newAppRequest = appRequest("company", "deadline", "date")
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
        return render_template('apprequestdisplay.html', form_data=form_data)

@app.route('/about')
def about():
    return render_template('about.html')






# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
