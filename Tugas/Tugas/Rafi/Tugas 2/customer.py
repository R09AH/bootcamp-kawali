from data import write_file, read_file

def check_user(users, user):
    for u in users:
        if u['user'] == user :
            return False
    return True

def cekTujuan(account, tujuan):
    for a in range(len(account)):
        if account[a]['user'] == tujuan:
            return True
    return False



def balance_check(account, user):
    for a in account:
        if a['user'] == user:
            print('your balance: Rp. ', str(a['amount']))

def tarikTunai(account, transaksi, user):
    amount = input('Enter the withdrawal amount : ')
    for a in range(len(account)):
        if account[a]['user'] == user:
            if account[a]['amount'] - int(amount) >= 0:
                account[a]['amount'] -= int(amount)
                write_file('account.txt', account)
                transaksi.append(
                    {
                        'user':user,
                        'to': 'self',
                        'amount': int(amount),
                        'type': 'withdraw',
                    }
                )
                write_file('transaksi.txt', transaksi)
                print('cash withdrawal successful!')
            else:
                print('sorry your balance is insufficient!')

def setorTunai(account, transaksi, user):
    amount = input('Enter the nominal deposit : ')
    for a in range(len(account)):
        if account[a]['user'] == user:
            account[a]['amount'] += int(amount)
            write_file('account.txt', account)
            transaksi.append(
                {
                    'user':user,
                    'to': 'self',
                    'amount': int(amount),
                    'type': 'deposit',
                }
            )
            print('Balance added successfully!')
            write_file('transaksi.txt', transaksi)
def transfer(account, transaksi, user):
    amount = input('Enter transfer amount : ')
    while True:
        tujuan = input('Enter the destination name : ')
        if cekTujuan(account, tujuan):
            for a in range(len(account)):
                if account[a]['user'] == user:
                    if account[a]['amount'] - int(amount) >= 0:
                        account[a]['amount'] -= int(amount)
                        for a in range(len(account)):
                            if account[a]['user'] == tujuan:
                                account[a]['amount'] += int(amount)
                                write_file('account.txt', account)
                                transaksi.append(
                                    {
                                        'user':user,
                                        'to': tujuan,
                                        'amount': int(amount),
                                        'type': 'transfer',
                                    }
                                )
                                write_file('transaksi.txt', transaksi)
                                print('transfer was successful!')
                                return True
                    else:
                        print('your balance is insufficient!')
                        return False
        else:
            print('destination name not available!')
                

def show_Transaction(transaksi, user):
    for t in range(len(transaksi)):
        if transaksi[t]['user'] == user:
            i = 1
            for t in range(len(transaksi)):
                if transaksi[t]['user'] == user:
                    print('')
                    print('=== Transaksi ', str(i), '===')
                    print('user : ', transaksi[t]['user'])
                    print('to : ', transaksi[t]['to'])
                    print('amount : ', transaksi[t]['amount'])
                    print('type : ', transaksi[t]['type'])
                    print('')
                i += 1
            return True
    print('You havent made any transactions!')