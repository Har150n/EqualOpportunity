class Employer:
    def __init__(self, company, app_requests, censor):
        #
        self.company = company
        self.app_requests = app_requests
        self.censor = censor

    def createAppReq(self, requirements):
        # allows employers to create an application request
        newApp = appRequest(requirements)
        return newApp

class appRequest:
    # allows employers to input deadline, login, and requirements for app requests
    def __init__(self, deadline, gpa, workEligibility):
        self.deadline = deadline
        self.gpa = gpa
        self.workEligibility = workEligibility
        self.listOfApps = []

    def meetRequirements(self,Application,gpa,workEligibility):
        if self.gpa <= Application.gpa and self.workEligibility == Application.workEligibility:
            return True