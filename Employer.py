class Employer:
    def __init__(self, company, app_requests, censor):
        #
        self.company = company
        self.app_requests = app_requests
        self.censor = censor

    def createAppReq(deadline, requirements):
        # allows employers to create an application request
        newApp = appRequest(deadline, requirements)
        return newApp

class appRequest:
    # allows employers to input deadline, login, and requirements for app requests
    def __init__(self, deadline, requirements):
        self.deadline = deadline
        self.requirements = requirements
        self.