def adduser(user, account):
    username ='user name : '
    password ='password : '
    role = input('role(1. admin 2. customer) :')

    if role == '1':
        role = 'admin'
    elif role == '2':
        role = 'customer'
    
    users.append({
        'username' : username,
        'password' : password,
        'role' : role
    })

    print('User added')
    return True

def deleteUser(users):
    for u in users:
        print(u['username'])

    while True:
        choice = input('masukan username : ')
        for u in users:
            users.remove(u)
            print('user removed')
            return True
        
#main
users = [
    {
        'username': 'rafi',
        'password': '999',
        'role': 'admin'
    }
]

cUser = {}
account = []
transaction = {}

def login(username, password, cUser):
    for u in users:
        if u['username'] == username and u['password'] == password:
            cUser.update(u)
            return True
    return False

def menu(cUser):
    # Menu admin
    if cUser['role'] == 'admin':
        while True:
            print(cUser)
            print('1. Add User')
            print('2. Delete User')
            print('3. Show Users')
            print('4. Show Transaction')
            print('5. Logout')
            choice = input('Choice : ')
            if choice == '1':
                adduser(users, account)
                print(users)
            elif choice == '2':
                deleteUser(users)
            elif choice == '3':
                showUser(users)
            elif choice == '4':
                showTransaction(transaction)
            elif choice == '5':
                cUser.clear()
                break
    # Menu customer
    elif cUser['role'] == 'customer':
        while True:
            print('1. Show Balance')
            print('2. Withdraw')
            print('3. Deposit')
            print('4. Transfer')
            print('5. Show Transaction')
            print('6. Logout')
            choice = input('CHoice : ')
            if choice == '1':
                showBalance(account, cUser['username'])
            elif choice == '2':
                withdraw(account, cUser)
            elif choice == '3':
                deposit(account, cUser)
            elif choice == '4':
                transfer(account, cUser)
            elif choice == '5':
                showTransaction(transaction, cUser['user'])
            elif choice == '6':
                cUser.clear()
                break

# Menu login
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
