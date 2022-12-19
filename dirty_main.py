from application.db.people import *
from application.salary import *
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now().strftime('%Y-%m-%d %H.%M'))
    get_employees()
    calculate_salary()