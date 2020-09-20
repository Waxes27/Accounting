from user import authentication
from user import journal


def run_app():
    amount = 100.00

    print("[{}] User Authentication loaded.".format("Module"))
    authentication.authenticate_user()
    journal.recieve_income(amount)
    journal.pay_expense(amount)

if __name__ == "__main__":
    run_app()