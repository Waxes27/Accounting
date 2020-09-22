# [Module] Journal loaded.
print("[{}] Journal loaded.".format("Module"))
def receive_income(amount):
    amount = float(amount)
    print("[{}] Received R{:.2f}".format("Journal",amount))


def pay_expense(amount):
    amount = float(amount)
    print("[{}] Paid R{:.2f}".format("Journal",amount))