from datetime import datetime, timedelta, date
from time import strptime
import calendar

#Install these
from pick import pick
import pandas

from scheduler import Scheduler

schedule = Scheduler()
user_input=''

while user_input != 'exit':
    user_input = input('Please enter the command (List, Exit, Add): ').lower()
    if user_input == 'list':
        schedule.getScheduleList()
    elif user_input == 'add':
        type_question = 'Please enter appointment type (h - Haircut, hs - Haircut + Shampoo):'
        type_options = ['Haircut', 'Haircut + Shampoo']
        appointment_type = pick(type_options, type_question)
        appointment_duration = timedelta(hours=1) if appointment_type[0] == 'Haircut + Shampoo' else timedelta(minutes=30)
        
        #Pick year
        year_question = 'Please select year'
        current_year = date.today().year
        year_options = [current_year + i for i in range(5)]
        year = pick(year_options, year_question)

        # Pick month
        month_question = 'Please select month:'
        current_day = date.today()
        last_day_in_year = date(current_year, 12, 31)
        if year[0] == current_year:
            month_options = pandas.date_range(current_day.strftime('%Y %m %d'),last_day_in_year.strftime('%Y %m %d'), freq='M').strftime('%B').tolist()
        else:
            month_options = [calendar.month_name[i] for i in range(1, 13)]
        month = pick(month_options, month_question)

        # Pick day
        day_question = 'Please select day:'
        year_to_int = int(year[0])
        month_number = int(month[1]) + 1
        selected_month_to_int = strptime(month[0], '%B').tm_mon
        current_month = date.today().month

        if current_month == selected_month_to_int:
            day_options = [str(i + 1) for i in range(date.today().day, calendar.monthrange(year_to_int, month_number)[1])]
        else: 
            day_options = [str(i + 1) for i in range(calendar.monthrange(year_to_int, month_number)[1])]
        day = pick(day_options, day_question)
        
        # Input Time
        time = input('Please enter the appointment time in 24-hour clock format with minutes (e.g. 14:30): ')


        appointment_datetime = (f'{year[0]} {str(month[1] + 1)} {day[0]} {time}')
        appointment_start_time = datetime.strptime(appointment_datetime, '%Y %m %d %H:%M')
        
        appointment_end_time = appointment_start_time + appointment_duration
    
        appointment_guest = input('Please enter appointment guest name: ')
         
        isScheduleAdded = schedule.addSchedule({
            'type': appointment_type,
            'start_time': appointment_start_time,
            'end_time': appointment_end_time,
            'guest': appointment_guest
        })