#ATM CODE
#Suppose for usere x the atm pin is 1234 and initial balance is 10000 units

correct_password = 1234
balance = 10000

while True:
    attempts = 0
    access = False

    while attempts < 3:
        password = int(input('Enter you pin: '))
        if password == correct_password:
            print('Access Granted')
            access = True
            break
        if password != correct_password:
            print('Wrong password please try again')
        attempts += 1
        if attempts == 3:
            print('Access blocked. Too many wrong attempts.')
            break

    if access == True:
        while True:
            print('1. CHEACK BALANCE\n2. DEPOSIT\n3. WITHDRAW\n4. EXIT')
            x = int(input('Please choose your desired operation:'))

            if x == 1:
                print(balance)

            elif x == 2:
                while True:
                    y = float(input('Enter the amount you would like to deposit: '))
                    if y < 0:
                        print('Enter a correct amount')
                    else:
                        balance += y
                        print('Your updated balance is', balance)
                        break

            elif x == 3:
                while True:
                    y = float(input('Enter the amount yu would like to withdraw: '))
                    if y > balance:
                        print('Insufficient balance')
                    else:
                        balance -= y
                        print('Your remaining balance is', balance)
                        break

            elif x == 4:
                print('Thankyou for using ATM')
                break

            else:
                print('Error')

    else:
        break