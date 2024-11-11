from ff import *
number = 1
print('\tThis game is a 1 vs computer game as well as a multiplayer game\n\t\tDEVELOPER IS ARYAN AGRAWAL\n')

try:
    number = int(input('Press 1 for vs computer and any other number for Multiplayer: '))
except ValueError:
    print('Invalid input, assuming multiplayer game')

if number != 1:
    name1 = input("Enter user1 name: ")
    name2 = input("Enter user2 name: ")
    sboard = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    board(sboard)
    flag = 3
    run = 1

    while True:
        if flag != 0:
            u1 = int(input("Enter the number you want to place 'x': "))
            fla = 0
            if u1 > 8:
                fla = 20
                flag = 1
                print('INDEX OUT OF RANGE, VALUE MUST BE LESS THAN 9')
            if fla != 20:
                if sboard[u1] != 'x' and sboard[u1] != 'o':
                    sboard[u1] = 'x'
                    board(sboard)
                    flag = 3
                    if rcheck('x', sboard) == 'win':
                        print(f"CONGRATULATIONS!!!! {name1}, you win!")
                        break
                else:
                    print("THE SPACE IS ALREADY OCCUPIED, TRY AGAIN")
                    flag = 1

            if all(cell == 'x' or cell == 'o' for cell in sboard):
                print("SORRY, BUT THE GAME IS A TIE")
                break

        if flag != 1:
            if run == 1:
                u1 = int(input("Enter the number you want to place 'o': "))
                fla = 0
                if u1 > 8:
                    fla = 20
                    flag = 0
                    print('INDEX OUT OF RANGE, VALUE MUST BE LESS THAN 9')
                if fla != 20:
                    if sboard[u1] != 'x' and sboard[u1] != 'o':
                        sboard[u1] = 'o'
                        board(sboard)
                        flag = 3
                        if rcheck('o', sboard) == 'win':
                            print(f"CONGRATULATIONS!!!! {name2}, you win!")
                            break
                    else:
                        print("THE SPACE IS ALREADY OCCUPIED, TRY AGAIN")
                        run = 1
                        flag = 0

                if all(cell == 'x' or cell == 'o' for cell in sboard):
                    print("SORRY, BUT THE GAME IS A TIE")
                    break

if number == 1:
    name1 = input("Enter user name: ")
    print("\nThe Game has 2 levels: ")
    print("\n1. EASY\n2. HARD\n")
    fk = int(input("ENTER YOUR LEVEL: "))

    if fk == 1:
        sboard = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        board(sboard)
        flag = 3
        while True:
            u1 = int(input("Enter the number you want to place 'x': "))
            fla = 0
            if u1 > 8:
                fla = 20
                flag = 1
                print('INDEX OUT OF RANGE, VALUE MUST BE LESS THAN 9')
            if fla != 20:
                if sboard[u1] != 'x' and sboard[u1] != 'o':
                    sboard[u1] = 'x'
                    board(sboard)
                    flag = 3
                    if rcheck('x', sboard) == 'win':
                        print(f"CONGRATULATIONS!!!! {name1}, you win!")
                        break
                else:
                    print("THE SPACE IS ALREADY OCCUPIED, TRY AGAIN")
                    flag = 1

            if all(cell == 'x' or cell == 'o' for cell in sboard):
                print("SORRY, BUT THE GAME IS A TIE")
                break

            if flag != 1:
                for i in range(8):
                    if sboard[i] == 'x' or sboard[i] == 'o':
                        i += 1
                    else:
                        sboard[i] = 'o'
                        print("Computer's turn")
                        board(sboard)
                        break

                if rcheck('o', sboard) == 'win':
                    print("COMPUTER WINS!!!")
                    break

                if all(cell == 'x' or cell == 'o' for cell in sboard):
                    print("SORRY, BUT THE GAME IS A TIE")
                    break

    if fk == 2:
        a = ['1', '2', '3']
        b = ['4', 'X', '6']
        c = ['7', '8', '9']
        print('\n', a, '\n', b, '\n', c, '\n')

        t = 0
        while True:
            if t % 2 == 0:
                print("USER TURN")
            else:
                print("Computer's turn\n")

            # Human section
            if t % 2 == 0:
                x = int(input("\nEnter location: "))

                if x in range(1, 10):
                    if x <= 3:
                        if a[x - 1] == 'X' or a[x - 1] == 'O':
                            print("Invalid Choice")
                            continue
                        a[x - 1] = 'O'
                    elif x <= 6:
                        if b[x - 4] == 'X' or b[x - 4] == 'O':
                            print("Invalid Choice")
                            continue
                        b[x - 4] = 'O'
                    elif x <= 9:
                        if c[x - 7] == 'X' or c[x - 7] == 'O':
                            print("Invalid Choice")
                            continue
                        c[x - 7] = 'O'
                    print('\n', a, '\n', b, '\n', c, '\n')
                    t += 1
                    if check_colu(a, b, c) or check_row(a, b, c) or check_diago(a, b, c):
                        break
                else:
                    print("!!! Invalid Location Chosen !!!")

            # Computer Section
            else:
                if ai_win_move(a, b, c):
                    pass
                elif check_ai_col(a, b, c) or check_ai_row(a, b, c):
                    pass
                elif check_ai_cor(a, b, c):
                    pass
                else:
                    print("!!! \tWell Played\t !!!\n\tMatch Drawn ")
                    break

                print('\n', a, '\n', b, '\n', c, '\n')
                t += 1
                if check_colu(a, b, c) or check_row(a, b, c) or check_diago(a, b, c):
                    break

            if t == 9:
                print("!!! \tWell Played\t !!!\n\tMatch Drawn ")
                break
