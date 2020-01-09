from models.appointments import Appointments
from models.scheduling import Scheduling

class Scheduler(Appointments, Scheduling):
    def __init__(self):
        self.schedules = {}
        self.listOfSchedules = []

    def getScheduleList(self):
        self.getList()
    
    def addSchedule(self, appointment):
        schedule = self.add_to_schedule(appointment)
        if schedule:
            self.addNewAppointment(appointment)
            print("Appointment Added!")
            return True
        else:
            print("Time is not available")
            return False