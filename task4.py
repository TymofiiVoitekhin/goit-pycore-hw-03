import datetime

def get_upcoming_birthdays (users):
    congratulation_date = []
# Цикл для перебору кожного словника
    for user in users:
# Конвертація дня народження в дату і визначення його дати саме цього року
        user["birthday"] = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        now = datetime.datetime.today().date()
        this_year = now.year
        user["birthday"] = user["birthday"].replace(year = this_year)
# Визначення пройшло чи не пройшло
        if user["birthday"] < now:
            user["birthday"] = user["birthday"].replace(year = (this_year+1))
# Визначення скільки залишилося
        days_left = user["birthday"] - now   
        weekday = user["birthday"].weekday()
# Функція фільтрування днів народжень на цей тиждень з врахуванням суботи та неділі
        if days_left < datetime.timedelta(days=7):
            if (weekday == 5): # Якщо субота
                user["birthday"] += datetime.timedelta(days=2)
                user["birthday"]  = str(user["birthday"])
                congratulation_date.append(user)
            elif (weekday == 6): # Якщо неділя
                user["birthday"] += datetime.timedelta(days=1)
                user["birthday"]  = str(user["birthday"])
                congratulation_date.append(user)
            else: # Якщо будній
                user["birthday"]  = str(user["birthday"])
                congratulation_date.append(user)
                

    return congratulation_date

users = [
    {"name": "John Doe", "birthday": "1985.06.21"},
    {"name": "Jane Smith", "birthday": "1990.06.18"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
