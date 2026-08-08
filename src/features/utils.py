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
def string_to_date(year=None, month=None, day=None):  
    # TODO improve filter
        
    if year and month and day:
        year = int(year)
        month = int(month)
        day = int(day)

        return date(year, month, day) 

    if year and month:
        year = int(year)
        month = int(month)

        return date(year, month, 1)
    
    if year:
        year = int(year)
        return date(year, 1, 1)
     
