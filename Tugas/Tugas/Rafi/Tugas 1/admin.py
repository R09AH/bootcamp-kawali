def cekuser(users, username):
    for u in users:
        if u['username'] == username :
            return True
        return False
        
def adduser(users, account):
    while True:
        username = input('Username : ')
        password = input('Password : ')

        while True:
            role = input('Role (1: admin, 2: customer) :')
            if role == '1':
                role = 'admin'
                break
            elif role == '2':
                role = 'customer'
                break
            print('Masukkan role yang sesuai!')
        
        if cekuser(users, username) == False:
            users.append({
                'username' : username,
                'password' : password,
                'role' : role
            }),
            account.append({
                'username' : username,
                'amount' : 0,
            })
            print('User berhasil di tambahkan!')
            return True
        else:
            print('Username sudah digunakan!')

def deleteuser(users, account):
    print('Daftar user :')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['username'], ' (',users[u]['role'],')')
    
    while True:
        choice = input('Masukan username user yang mau di hapus : ')
        for u in range(len(users)):
            if users[u]['username'] == choice:
                users.pop(u)
                account.pop(u)
                print('User removed')
                return True
        print('Pilih username yang ada!')

def showuser(users):
    print('Daftar user :')
    for u in range(len(users)):
        print(str(u+1), '. ', users[u]['username'], ' (',users[u]['role'],')')

def showAllTransaction(transaction):
    for t in range(len(transaction)):
        print(str(t+1), '. ','username : ', transaction[t]['username'])
        print('   ', 'to : ', transaction[t]['to'])
        print('   ', 'amount : ', transaction[t]['amount'])
        print('   ', 'typr : ', transaction[t]['type'])