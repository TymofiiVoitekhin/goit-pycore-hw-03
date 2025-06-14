import datetime

def get_days_from_today(user_date):
 now = datetime.date.today()
 difference = (now - user_date).days

 return difference

input_date = input("Введіть дату (рік-місяць-день): ")

try:
     date_from_user = datetime.datetime.strptime(input_date, "%Y-%m-%d").date()
     delta = get_days_from_today(date_from_user)
     print (delta)
except ValueError:
     print("Неправильне введення дати")
