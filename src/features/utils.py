from datetime import datetime, date

def get_year_range():
    today = date.today()
    years = []
   
    for i in range(2000, int(today.year) + 1):
        years.append(i)

    return years


def string_to_date(date: str, date_format="%m/%d/%Y"):

    datetime_obj = datetime.strptime(date, date_format)
    date_obj = datetime_obj.date()

    return date_obj


