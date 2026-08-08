from datetime import datetime, date

def get_year_range():
    today = date.today()
    years = []
   
    for i in range(2000, int(today.year) + 1):
        years.append(i)

    return years

# Pass month year and day\
'''
format = ""
if not month or year or day:
    adjust format

date with values

'''
def string_to_date(date_str, date_format="%Y-%m-%d"):  
    
    datetime_obj = datetime.strptime(date_str, date_format) 
    date_obj = datetime_obj.date() 

    return date_obj

