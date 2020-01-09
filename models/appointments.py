import re

class Appointments:
    def __init__(self, listOfSchedules):
        self.listOfSchedules = []
    
    def get_list(self):
        for i in range(len(self.listOfSchedules)):
            print('_______________________________')
            iteration_dict = self.listOfSchedules[i]
            date = self.format_date_string(iteration_dict['start_time'], '%Y %B %d-%A')
            start_time = self.format_date_string(iteration_dict['start_time'])
            end_time = self.format_date_string(iteration_dict['end_time'])
            guest_name = iteration_dict['guest']
            print(f'Date: {date}')
            print(f'Time: {start_time} - {end_time}')
            print(f'Guest name: {guest_name}')
            

    def add_new_appointment(self, appointment):
        self.listOfSchedules.append(appointment)

    def format_date_string(self, date, format = '%H:%M'):
        return date.strftime(format)

    def validate_time_format(self, time):
        r = re.compile('[0-2][0-9]:[0-5][0-9]')
        return r.match(time) == None

    def concatenate_inputs(self, year, month, day, time):
        return (f'{year} {str(month + 1)} {day} {time}')

    def get_next_years_list(self, current_year, years = 5):
        return [current_year + i for i in range(years)]