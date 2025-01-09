from bankaccount import BankAccount

def main():
    my_account = BankAccount ( "12 3456 5555 9090 1111 0000 7722" )
    my_account.show_balance()
    my_account.deposit(25.30)
    my_account.show_balance()
    my_account.withdraw(31.70)
    my_account.show_balance()
    my_account.withdraw(23)
if __name__ =="__main__":
    main()
