# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
from Application import Application
import Application



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
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

#page to send in new applicatoin
@app.route('/applicationform/', methods=['POST'])
def applicationform():
    if request.method == 'POST':
        form_data = request.form
        name = form_data.get("Name")
        gpa = form_data.get("GPA")
        workEligibility = form_data.get("Work Eligibility")
        coverLetter = form_data.get("Cover Letter")
        resume = form_data.get("Resume")
        newapp = (name, gpa, workEligibility, coverLetter, resume) #creates new application
        return render_template('applicationform.html', form_data=form_data)




@app.route('/form')
def form():
    return render_template('form.html')





# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)