import sys
from user import authentication
from transactions import journal
from banking import reconciliation
from banking.fvb import reconciliation as fvbrecon
from banking.ubsa import reconciliation as ubsarecon
from banking.online import reconciliation as onlinebanking
import banking
import requests


def run_app():
    #help("modules")
    for i in sys.argv:
        print(i)
    amount = 100.00
    authentication.authenticate_user()
    journal.receive_income(amount)
    journal.pay_expense(amount)
    #reconciliation.do_reconciliation()
    fvbrecon.do_reconciliation()
    ubsarecon.do_reconciliation()
    response = requests.get("https://www.wethinkcode.co.za")
    onlinebanking.do_reconciliation()
    print(response.status_code)

if __name__ == "__main__":
        run_app()