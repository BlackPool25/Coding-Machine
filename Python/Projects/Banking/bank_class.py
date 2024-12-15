from tabulate import tabulate

class Bank:
    def __init__(self, type="savings"):
        self.type = type
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def update_account(self, account_number, **kwargs):
        for account in self.accounts:
            if account['account_number'] == account_number:
                for key, value in kwargs.items():
                    if key in account:
                        account[key] = value

    def display_accounts(self):
        headers = ["Account Number", "Name", "Balance"]
        table = [[acc['account_number'], acc['name'], acc['balance']] for acc in self.accounts]
        return tabulate(table, headers, tablefmt="grid")

    def save_to_file(self):
        with open("accounts.txt", 'a') as file:
            file.write(self.display_accounts())