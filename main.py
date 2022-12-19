from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime
from square.run import square_run


if __name__ == '__main__':
    square_run()
    print(datetime.now().strftime('%Y-%m-%d %H.%M'))
    get_employees()
    calculate_salary()