



def run_app():
    #help("modules")
    for i in sys.argv:
        print(i)
    amount = 100.00
    authentication.authenticate_user()
    journal.receive_income(amount)
    journal.pay_expense(amount)
    reconciliation.do_reconciliation()
    fvbrecon.do_reconciliation()
    ubsarecon.do_reconciliation()
    response = requests.get("https://www.wethinkcode.co.za")
    print(response.status_code)
    onlinebanking.do_reconciliation()

if __name__ == "__main__":
        run_app()