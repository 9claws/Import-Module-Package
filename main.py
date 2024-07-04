import application.db.people
from application.salary import calculate_salary
from datetime import datetime
import requests
current_date = datetime.now()

if __name__ == '__main__':
    application.db.people.get_employees()
    calculate_salary()
    print(current_date)


print(requests.get("https://netology.ru/"))