
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
    