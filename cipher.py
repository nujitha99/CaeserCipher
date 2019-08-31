alphsim = list('abcdefghijklmnopqrstuvwxyz')
alphcap = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def methodfunc():
    if method == 'e':
        encrypt()

    elif method == 'd':
        decrypt()

    elif method == 'a':
        analyse()

    elif method == 'q':
        print('program terminates...')

    else:
        print('you entered something wrong... try again')


    ################# encrypt ######################


def encrypt():
    real = input("Enter the text you want to encrypt : ")  # gets the input from the user
    key = int(input('Enter the key :'))

    while key > 26 or key < 0:  # checks for the key in valid range
        key = int(input('wrong, Enter a key between 1 - 26 : '))

    print('\n')
    print('cypher text : ', end='')

    for i in real:  # prints the text
        if i in alphcap:
            print (i, end='')

        elif i in alphsim:
            cyph = alphsim[(alphsim.index(i) + key) % 26]
            print (cyph, end='')

        else:
            print (i, end='')

    print('\n')  # starts a new iteration

    method = input("Enter \n 'a' to analyse\n 'e' to encrypt\n 'd' to decrypt\n 'q' to quit :")
    if method == 'e':
        encrypt()

    elif method == 'd':
        decrypt()

    elif method == 'a':
        analyse()

    elif method == 'q':
        print('program terminates...')

    else:
        print('you entered something wrong... try again')

    ################### decrypt #####################


def decrypt():
    cyph = input("Enter the text you want to decrypt : ")  # gets the input from the user
    key = int(input('Enter the key :'))

    while key > 26 or key < 0:  # checks for the key in valid range
        key = int(input('wrong, Enter a key between 1 - 26 : '))

    print('\n')
    print('Real text : ', end='')

    for i in cyph:      # prints the text
        if i in alphcap:
            print (i, end='')
        elif i in alphsim:
            real = alphsim[(alphsim.index(i) - key) % 26]
            print(real, end='')
        else:
            print (i, end='')

    print('\n')  # starts a new iteration
    method = input("Enter \n 'a' to analyse\n 'e' to encrypt\n 'd' to decrypt\n 'q' to quit : ")

    if method == 'e':
        encrypt()

    elif method == 'd':
        decrypt()

    elif method == 'a':
        analyse()

    elif method == 'q':
        print('program terminates...')

    else:
        print('you entered something wrong... try again')

    ################# analyse ###################


def analyse():
    key_1 = 0
    key_2 = 0
    cyph = input("Enter the text you want to decrypt : ")
    real = input('Enter part of original text from the beginning : ')

    for j in cyph:
        if j in alphsim:
            key_1 = alphsim.index(j)    # assigns the index value in cypher text
            break
        continue

    for k in real:
        if k in alphsim:
            key_2 = alphsim.index(k)    # assigns the index value in real text
            break
        continue

    key = key_1 - key_2     # calculates the key

    print('\n')

    print("key : ", key)    # prints the key value

    print("Real text : ", end='')

    for i in cyph: # prints the text
        if i in alphcap:
            print(i, end='')
        elif i in alphsim:
            real = alphsim[(alphsim.index(i) - key) % 26]
            print(real, end='')
        else:
            print(i, end='')

    print('\n')  # starts a new iteration
    method = input("Enter \n 'a' to analyse\n 'e' to encrypt\n 'd' to decrypt\n 'q' to quit : ")
    if method == 'e':
        encrypt()

    elif method == 'd':
        decrypt()

    elif method == 'a':
        analyse()

    elif method == 'q':
        print('program terminates...')

    else:
        print('you entered something wrong... try again')


####### initially starts the programme ######


method = input("Enter \n 'a' to analyse\n 'e' to encrypt\n 'd' to decrypt\n 'q' to quit :")
if method == 'e':
    encrypt()
elif method == 'd':
    decrypt()
elif method == 'a':
    analyse()
elif method == 'q':
    print('program terminates...')
else:
    print('you entered something wrong... try again')
    method = input("Enter 'a' to analyse\n 'e' to encrypt\n 'd' to decrypt\n 'q' to quit :")
    methodfunc()
