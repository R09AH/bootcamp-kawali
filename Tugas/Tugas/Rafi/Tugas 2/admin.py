from data import write_file, read_file

def check_user(users, user):
    for u in users:
        if u['user'] == user :
            return False
    return True
        
def addUser(users, account):
    while True:
        user = input('User : ')
        if len(user) > 0 :
            while True:
                password = input('Password : ')
                if len(password) > 0 :
                    while True:
                        role = input('Role (1: admin, 2: customer) :')
                        if role == '1':
                            role = 'admin'
                            break
                        elif role == '2':
                            role = 'customer'
                            break
                        print('Masukkan role yang sesuai!')
                    
                    if check_user(users, user):
                        users.append({
                            'user' : user,
                            'password' : password,
                            'role' : role
                        }),
                        write_file('user.txt', users)
                        account.append({
                            'user' : user,
                            'amount' : 0,
                        })
                        write_file('account.txt', account)
                        print('user successfully added!')
                        return True
                    else:
                        print('username has been used!')
                else:
                    print('Enter password!')
        else:
            print('Enter name user!')

def delete_user(users, account):
    print('Daftar user :')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['user'], ' (',users[u]['role'],')')
    
    while True:
        user = input('Enter the username to be deleted : ')
        for u in range(len(users)):
            if users[u]['user'] == user:
                users.pop(u)
                account.pop(u)
                write_file('user.txt', users)
                write_file('account.txt', account)
                print('user successfully deleted!')
                return True
        print('select an existing user!')

def show_user(users):
    print('Daftar user :')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['user'], ' (',users[u]['role'],')')

def showALL_transaction(transaksi):
    if len(transaksi) > 0:
        for t in range(len(transaksi)):
            print(str(t+1), '. ','user : ', transaksi[t]['user'])
            print('   ', 'to : ', transaksi[t]['to'])
            print('   ', 'amount : ', transaksi[t]['amount'])
            print('   ', 'type : ', transaksi[t]['type'])
    else:
        print('no transactions have been made')



