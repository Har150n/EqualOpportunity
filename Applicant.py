import Application
class Applicant:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.application_list = []

#creates an Application object
    def createApp(self):
        resume = "my resume link"
        cover_letter = "letterl ink"
        newApp = Application(self.name, self.age, resume, cover_letter)


