import requests
print("[{}] online.Reconciliation loaded.".format("Module") )
def do_reconciliation():
    print("Doing Online Bank reconciliation.")
    response = requests.get("https://www.wethinkcode.co.za")
    print(response.status_code)
