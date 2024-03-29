import sys
from user import authentication
from transactions import journal
import banking
# from banking import reconciliation
#from banking.fvb import reconciliation as fvbrecon
# from banking.ubsa import reconciliation as ubsarecon
# from banking.online import reconciliation as onlinebanking
#import requests


def run_app():
    #help("modules")
    if len(sys.argv) > 1:
        for i in sys.argv:
            print(i)
    amount = 100.00
    authentication.authenticate_user()
    journal.receive_income(amount)
    journal.pay_expense(amount)
    banking.fvbrecon.do_reconciliation()
    #reconciliation.do_reconciliation()
    #fvbrecon.do_reconciliation()
    #ubsarecon.do_reconciliation()
    #response = requests.get("https://www.wethinkcode.co.za")
    #print(response.status_code)
    #onlinebanking.do_reconciliation()

if __name__ == "__main__":
        run_app()