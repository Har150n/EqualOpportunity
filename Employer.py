class Employer:
    def __init__(self, company, censor):
        #
        self.company = company
        self.app_requests = []
        self.censor = censor

    def createAppReq(self, position, company, deadline):
        # allows employers to create an application request
        newApp = appRequest(position, company, deadline)
        return newApp

class appRequest:
    # allows employers to input deadline, login, and requirements for app requests
    def __init__(self, position, company, deadline, gpa, workEligibility):
        self.position = position
        self.company = company
        self.deadline = deadline
        self.gpa = gpa
        self.workEligibility = workEligibility
        self.listOfApps = []

