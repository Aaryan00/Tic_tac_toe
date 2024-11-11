def check_colu(a, b, c):                  
    for i in range(3):
        if a[i] == b[i] == c[i]:
            print(f"{a[i]} is Winner")
            return 1

def board(sboard):
    print(f"{sboard[0]} {sboard[1]} {sboard[2]}")
    print(f"{sboard[3]} {sboard[4]} {sboard[5]}")
    print(f"{sboard[6]} {sboard[7]} {sboard[8]}")

def check(u, b1, b2, b3, sboard):
    if sboard[b1] == u and sboard[b2] == u and sboard[b3] == u:
        return "win"

def rcheck(u, sboard):
    if check(u, 0, 1, 2, sboard) == 'win':
        return 'win'
    elif check(u, 3, 4, 5, sboard) == 'win':
        return 'win'
    elif check(u, 6, 7, 8, sboard) == 'win':
        return 'win'
    elif check(u, 0, 4, 8, sboard) == 'win':
        return 'win'
    elif check(u, 0, 3, 6, sboard) == 'win':
        return 'win'
    elif check(u, 1, 4, 7, sboard) == 'win':
        return 'win'
    elif check(u, 2, 5, 8, sboard) == 'win':
        return 'win'
    elif check(u, 2, 4, 6, sboard) == 'win':
        return 'win'

def check_row(a, b, c):                           
    for i in range(1):
        if a[i] == a[i + 1] == a[i + 2]:                
            print(f"{a[i]} is Winner")
            return 1
        elif b[i] == b[i + 1] == b[i + 2]:
            print(f"{b[i]} is Winner")
            return 1
        elif c[i] == c[i + 1] == c[i + 2]:             
            print(f"{c[i]} is Winner")
            return 1

def check_diago(a, b, c):
    i = 0
    if a[i] == b[i + 1] == c[i + 2]:
        print(f"{a[i]} is Winner")
        return 1
    elif c[i] == b[i + 1] == a[i + 2]:
        print(f"{c[i]} is Winner")
        return 1

def check_ai_col(a, b, c):
    for i in range(3):
        if a[i] == b[i] == 'O' and c[i] not in ['X', 'O']:
            c[i] = 'X'
            return 1
        elif b[i] == c[i] == 'O' and a[i] not in ['X', 'O']:
            a[i] = 'X'
            return 1
        elif a[i] == c[i] == 'O' and b[i] not in ['X', 'O']:
            b[i] = 'X'
            return 1
    return 0

def check_ai_row(a, b, c):
    k = [a, b, c]
    for i in k:
        if i[1] == i[2] == 'O' and i[0] not in ['X', 'O']:
            i[0] = 'X'
            return 1
        elif i[0] == i[2] == 'O' and i[1] not in ['X', 'O']:
            i[1] = 'X'
            return 1
        elif i[1] == i[0] == 'O' and i[2] not in ['X', 'O']:
            i[2] = 'X'
            return 1
    return 0

def check_ai_cor(a, b, c):
    if a[0] not in ['X', 'O']:
        a[0] = 'X'
        return 1
    elif c[0] not in ['X', 'O']:
        c[0] = 'X'
        return 1
    elif a[2] not in ['X', 'O']:
        a[2] = 'X'
        return 1
    elif c[2] not in ['X', 'O']:
        c[2] = 'X'
        return 1
    else:
        return 0

def ai_win_move(a, b, c):
    k = [a, b, c]
    for i in k:
        if i[1] == i[2] == 'X' and i[0] not in ['X', 'O']:
            i[0] = 'X'
            return 1
        elif i[0] == i[2] == 'X' and i[1] not in ['X', 'O']:
            i[1] = 'X'
            return 1
        elif i[1] == i[0] == 'X' and i[2] not in ['X', 'O']:
            i[2] = 'X'
            return 1
    for i in range(3):
        if a[i] == b[i] == 'O' and c[i] not in ['X', 'O']:
            c[i] = 'X'
            return 1
        elif b[i] == c[i] == 'O' and a[i] not in ['X', 'O']:
            a[i] = 'X'
            return 1
        elif a[i] == c[i] == 'O' and b[i] not in ['X', 'O']:
            b[i] = 'X'
            return 1
    if a[0] == b[1] and c[2] not in ['X', 'O']:
        c[2] = 'X'
        return 1
    elif c[0] == b[1] and a[2] not in ['X', 'O']:
        a[2] = 'X'
        return 1
    elif c[2] == b[1] and a[0] not in ['X', 'O']:
        a[0] = 'X'
        return 1
    elif a[2] == b[1] and c[0] not in ['X', 'O']:
        c[0] = 'X'
        return 1
    return 0
