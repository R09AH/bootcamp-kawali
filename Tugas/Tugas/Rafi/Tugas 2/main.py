from admin import addUser, delete_user, show_user, showALL_transaction
from customer import balance_check, tarikTunai, setorTunai, transfer, show_Transaction
from data import write_file, read_file
users = read_file('user.txt')
cUser = {}

transaksi = read_file('transaksi.txt')

account = read_file('account.txt')



def infoLogin(user, password, cUser):
    for u in users:
        if u['user'] == user and u['password'] == password:
            cUser.update(u)
            return True
    return False


def login(cUser):
    while True:
        user = input('User : ')
        passsword = input('Password : ')
        if infoLogin(user, passsword, cUser):
            print('Login success')
            break
        else:
            print('Login failed')

def menu(cUser):
    if cUser['role'] == 'admin':
        while True:
            print('== Menu ==')
            print('1. Add User')
            print('2. Delete user')
            print('3. Show Users')
            print('4. Show transaction')
            print('5. Logout')
            pilihan = input('choose menu : ')
            if pilihan == '1':
                addUser(users, account)
            elif pilihan == '2':
                delete_user(users, account)
            elif pilihan == '3':
                show_user(users)
            elif pilihan == '4':
                showALL_transaction(transaksi)
            elif pilihan == '5':
                cUser.clear()
                break
    
    elif cUser['role'] == 'customer':
        while True:
            print('== Menu ==')
            print('1. Show balance')
            print('2. Tarik Tunai')
            print('3. Setor Tunai')
            print('4. Transfer')
            print('5. Show transaksi')
            print('6. Logout')
            pilihan = input('choose Menu : ')
            if pilihan == '1':
                balance_check(account, cUser['user'])
            elif pilihan == '2':
                tarikTunai(account, transaksi, cUser['user'])
            elif pilihan == '3':
                setorTunai(account, transaksi, cUser['user'])
            elif pilihan == '4':
                transfer(account, transaksi, cUser['user'])
            elif pilihan == '5':
                show_Transaction(transaksi, cUser['user'])
            elif pilihan == '6':
                cUser.clear()
                break


def main():
    while True:
        print('1. Login')
        print('2. Exit')
        pilihan = input('choose menu: ')
        if pilihan == '1':
            login(cUser)
            menu(cUser)
        elif pilihan == '2':
            break
        print('\033c', end='')

main()
