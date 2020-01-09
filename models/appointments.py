class Appointments:
    def __init__(self, listOfSchedules):
        self.listOfSchedules = []
    
    def getList(self):
        print(self.listOfSchedules)

    def addNewAppointment(self, appointment):
        self.listOfSchedules.append(appointment)