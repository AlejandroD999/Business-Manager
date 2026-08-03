import calendar

def parse_expense_date(expenses):
    
    months = {}
    for expense in expenses:
        months[expense.date[6:]] = calendar.month_name[int(expense.date[:2])]

    return months
