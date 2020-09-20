from user import authentication
from transactions import journal
from banking import reconciliation
from 

def run_app():
    amount = 100.00

    authentication.authenticate_user()
    journal.receive_income(amount)
    journal.pay_expense(amount)
    reconciliation.do_reconciliation()

if __name__ == "__main__":
    run_app()