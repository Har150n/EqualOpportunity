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