import calendar

#Install these
import pandas
from controllers.scheduler import Scheduler

schedule = Scheduler()
user_input=''

while user_input != 'exit':
    user_input = input('Please enter the command (List, Exit, Add): ').lower()
    if user_input == 'list':
        schedule.get_list()
    elif user_input == 'add':
        appointment_type = schedule.show_picker(['Haircut', 'Haircut + Shampoo'], 'Please enter appointment type (h - Haircut, hs - Haircut + Shampoo):')
        appointment_duration = schedule.convert_type_string_to_duration(appointment_type[0])
        
        #Pick year
        current_year = schedule.get_current_year()
        list_of_years = schedule.get_next_years_list(current_year, 5)
        year = schedule.show_picker(list_of_years, 'Please select year:')

        # Pick month
        # If current year, show only available months
        if year[0] == current_year:
            current_day = schedule.get_current_day_date()
            last_day_in_year = schedule.get_last_day_of_year()
            month_options = pandas.date_range(current_day.strftime('%Y %m %d'),last_day_in_year.strftime('%Y %m %d'), freq='M').strftime('%B').tolist()
        # Else show all 12 months
        else:
            month_options = [calendar.month_name[i] for i in range(1, 13)]
        
        month = schedule.show_picker(month_options, 'Please select month:')

        # Pick day
        year_to_int = int(year[0])
        month_number = int(month[1]) + 1
        selected_month_to_int = schedule.convert_month_to_int(month[0])
        current_month = schedule.get_current_month()

        # if current month is selected show only available days in current month
        if current_month == selected_month_to_int:
            day_options = [str(i + 1) for i in range(schedule.get_current_day(), calendar.monthrange(year_to_int, month_number)[1])]
        # show all days in selected month
        else: 
            day_options = [str(i + 1) for i in range(calendar.monthrange(year_to_int, month_number)[1])]
        
        day = schedule.show_picker(day_options, 'Please select day:')
        
        # Input Time
        time = ''
        # Make sure user inputs the correct format of time
        while schedule.validate_time_format(time):
            time = input('Please enter the appointment time in 24-hour clock format with minutes (e.g. 14:30): ')
        
        # Concatenate all inputs
        appointment_datetime = schedule.concatenate_inputs(year[0], month[1], day[0], time)
        # Create datetime class instance
        appointment_start_time = schedule.create_datetime_from_string(appointment_datetime)
        appointment_end_time = schedule.calculate_end_time(appointment_start_time, appointment_duration)
    
        appointment_guest = input('Please enter appointment guest name: ')
         
        isScheduleAdded = schedule.add_schedule({
            'type': appointment_type,
            'start_time': appointment_start_time,
            'end_time': appointment_end_time,
            'guest': appointment_guest
        })