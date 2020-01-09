from models.appointments import Appointments
from models.scheduling import Scheduling

from pick import pick
import pandas

class Scheduler(Appointments, Scheduling):
    def __init__(self):
        self.schedules = {}
        self.listOfSchedules = []
    
    def add_schedule(self, appointment):
        schedule = self.add_to_schedule(appointment)
        if schedule:
            self.add_new_appointment(appointment)
            print("Appointment Added!")
            return True
        else:
            print("Time is not available")
            return False
    
    def show_picker(self, options, question):
        return pick(options, question)