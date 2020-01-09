from datetime import timedelta, datetime, date
from time import strptime

class Scheduling():
    def __init__(self):
        self.schedules = {}
    
    def add_to_schedule(self, date):
        
        key = self.convert_date_to_string(date, 'start_time', '%Y%m%d')
        
        if key in self.schedules:
            time_available = self.check_availability(key, date['start_time'])
            
            if time_available:
               self.schedules[key] = self.format_data(date['start_time'], date['end_time'], key)
               return True
            return False
        
        else:
            self.schedules[key] = self.format_data(date['start_time'], date['end_time'], key)
            return True
    
    def check_availability(self, day, given_time):
        for i in range(len(self.schedules[day])):
            start = self.schedules[day][i]['start_time']
            end = self.schedules[day][i]['end_time']
            
            if start <= given_time <= end:
                return False
       
        return True
    
    def convert_date_to_string(self, date, key, format):
        return date[key].strftime(format)
    
    def format_data(self, start_time, end_time, key):
        return [{'start_time': start_time, 'end_time': end_time}]
    
    def convert_type_string_to_duration(self, type):
        return timedelta(hours=1) if type == 'Haircut + Shampoo' else timedelta(minutes=30)

    def calculate_end_time(self, start_time, duration):
        return start_time + duration

    def create_datetime_from_string(self, date_string, format = '%Y %m %d %H:%M'):
        return datetime.strptime(date_string, format)
    
    def get_current_year(self):
        return date.today().year

    def get_current_month(self):
        return date.today().month
    
    def get_current_day(self):
        return date.today().day

    def get_current_day_date(self):
        return date.today()
    
    def get_last_day_of_year(self):
        return date(self.get_current_year(), 12, 31)

    def convert_month_to_int(self, month):
        return strptime(month, '%B').tm_mon