from admin import adduser, deleteuser, showuser, showAllTransaction
from customer import showbalance, withdraw, deposit, transfer, showtransaction
users = [
    {
        'username': 'rafi',
        'password': '999',
        'role': 'admin'
    }
]

cUser = {}
transaction = []

account = [
    {
        'username':'rafi',
        'amount': 0
    },
]


def login(username, password, cUser):
    for u in users:
        if u['username'] == username and u['password'] == password:
            cUser.update(u)
            return True
    return False



def login_process(cUser):
    while True:
        username = input('Username : ')
        passsword = input('Password : ')
        if login(username, passsword, cUser):
            print('Login Success')
            break
        else:
            print('Login Failed')

def menu(cUser):

    if cUser['role'] == 'admin':
        while True:
            print('====')
            print('Menu')
            print('====')
            print('1. Add User')
            print('2. Delete User')
            print('3. Show Users')
            print('4. Show Transaction')
            print('5. Logout')
            choice = input('Choice : ')
            if choice == '1':
                adduser(users, account)
            elif choice == '2':
                deleteuser(users, account)
            elif choice == '3':
                showuser(users)
            elif choice == '4':
                showAllTransaction(transaction)
            elif choice == '5':
                cUser.clear()
                break

    elif cUser['role'] == 'customer':
        while True:
            print('==============')
            print('Menu')
            print('==============')
            print('1. Show Balance')
            print('2. Withdraw')
            print('3. Deposit')
            print('4. Transfer')
            print('5. Show Transaction')
            print('6. Logout')
            choice = input('Choice : ')
            if choice == '1':
                showbalance(account, cUser['username'])
            elif choice == '2':
                withdraw(account, transaction, cUser['username'])
            elif choice == '3':
                deposit(account, transaction, cUser['username'])
            elif choice == '4':
                transfer(account, transaction, cUser['username'])
            elif choice == '5':
                showtransaction(transaction, cUser['username'])
            elif choice == '6':
                cUser.clear()
                break


def main():
    while True:
        print('1. Login')
        print('2. Exit')
        choice = input('Choice: ')
        if choice == '1':
            login_process(cUser)
            menu(cUser)
        elif choice == '2':
            break
        print('\033c', end='')

main()