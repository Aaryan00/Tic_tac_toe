from ff import *
number = 1
print('\tThis game is 1 vs computer game as well as multiplayer game\n\t\t DEVELOPER IS ARYAN AGRAWAL\n')
try:
    number = input(' press 1 for vs computer and any other number Multiplayer: ')
except NameError:
    print('Multiplayer game is ready')
if(number == 1):
    name1=raw_input("Enter user1 name: ")
    name2=raw_input("Enter user2 name: ")
    sboard=[0,1,2,3,4,5,6,7,8]
    board(sboard)
    flag=3
    run =1

    while True:
         if(flag!=0):
            u1=int(input("enter the no. u wanna place x: "))
            fla=0
            if u1>8:
                    fla=20
                    flag=1
                    print ('INDEX OUT OF RANGE, VALUE MUST BE LESS THAN 9')
            if(fla!=20):
                    if sboard[u1]!='x' and sboard[u1]!='o':
                         sboard[u1]='x' 
                         board(sboard)
                         flag=3
                         if rcheck('x',sboard)=='win':
                              print("CONGRATULATIONS!!!!" + name1+ " you win")
                              break
                    else:
                        print("THE SPACE IS ALREADY OCCUPIED , TRY AGAIN")
                        flag=1

            if (sboard[0]=='x' or sboard[0]=='o') and (sboard[1]=='x' or sboard[1]=='o') and (sboard[2]=='x' or sboard[2]=='o') and (sboard[3]=='x' or sboard[3]=='o') and (sboard[4]=='x' or sboard[4]=='o') and (sboard[5]=='x' or sboard[5]=='o') and (sboard[6]=='x' or sboard[6]=='o') and (sboard[7]=='x' or sboard[7]=='o') and (sboard[8]=='x' or sboard[8]=='o') :
                 print("SORRY, BUT THE GAME IS TIE")
                 break



         if(flag!=1):
            if(run ==1):
                    u1=int(input("enter the no. u wanna place 0: "))
                    fla=0
                    if u1>8:
                        fla=20
                        flag=0
                        print ('INDEX OUT OF RANGE, VALUE MUST BE LESS THAN 9')
                    if(fla!=20):
                        if sboard[u1]!='x' and sboard[u1]!='o':
                             sboard[u1]='0' 
                             board(sboard)
                             flag=3
                             if rcheck('0',sboard)=='win':
                                  print("CONGRATULATIONS!!!!" + name2+ " you win")
                                  break
                        else:
                            print("THE SPACE IS ALREADY OCCUPIED , TRY AGAIN")
                            run=1
                            flag = 0

                    if (sboard[0]=='x' or sboard[0]=='o') and (sboard[1]=='x' or sboard[1]=='o') and (sboard[2]=='x' or sboard[2]=='o') and (sboard[3]=='x' or sboard[3]=='o') and (sboard[4]=='x' or sboard[4]=='o') and (sboard[5]=='x' or sboard[5]=='o') and (sboard[6]=='x' or sboard[6]=='o') and (sboard[7]=='x' or sboard[7]=='o') and (sboard[8]=='x' or sboard[8]=='o') :
                     print("SORRY, BUT THE GAME IS TIE")
                     break
if(number != 1):
        
    name1=raw_input("Enter user name: ")
    print("\n The Game has 2 levels: ")
    print("\n1. EASY\n2.HARD\n")
    fk=int(input("ENTER YOUR LEVEL: "))

    if fk==1:
        sboard=[0,1,2,3,4,5,6,7,8]
        board(sboard)
        flag=3
        while True:
             #if(flag!=0):
            u1=int(input("enter the no. u wanna place x: "))
            fla=0
            if u1>8:
                    fla=20
                    flag=1
                    print ('INDEX OUT OF RANGE, VALUE MUST BE LESS THAN 9')
            if(fla!=20):
                    if sboard[u1]!='x' and sboard[u1]!='o':
                         sboard[u1]='x' 
                         board(sboard)
                         flag=3
                         if rcheck('x',sboard)=='win':
                              print("CONGRATULATIONS!!!!" + name1+ " you win")
                              break
                    else:
                        print("THE SPACE IS ALREADY OCCUPIED , TRY AGAIN")
                        flag=1

            if (sboard[0]=='x' or sboard[0]=='o') and (sboard[1]=='x' or sboard[1]=='o') and (sboard[2]=='x' or sboard[2]=='o') and (sboard[3]=='x' or sboard[3]=='o') and (sboard[4]=='x' or sboard[4]=='o') and (sboard[5]=='x' or sboard[5]=='o') and (sboard[6]=='x' or sboard[6]=='o') and (sboard[7]=='x' or sboard[7]=='o') and (sboard[8]=='x' or sboard[8]=='o') :
                 print("SORRY, BUT THE GAME IS TIE")
                 break

            if(flag!=1):
                  for i in range (8):
                     if(sboard[i]=='x' or sboard[i]=='o'):
                         i+=1
                          
                     else:
                          sboard[i]='o'
                          print("Computer chance")
                          board(sboard)
                          break
                           
                  if rcheck('o',sboard)=='win':
                      print("COMPUTER WINS!!! ")
                      break

                  if (sboard[0]=='x' or sboard[0]=='o') and (sboard[1]=='x' or sboard[1]=='o') and (sboard[2]=='x' or sboard[2]=='o') and (sboard[3]=='x' or sboard[3]=='o') and (sboard[4]=='x' or sboard[4]=='o') and (sboard[5]=='x' or sboard[5]=='o') and (sboard[6]=='x' or sboard[6]=='o') and (sboard[7]=='x' or sboard[7]=='o') and (sboard[8]=='x' or sboard[8]=='o') :
                       print("SORRY, BUT THE GAME IS TIE")
                       break

    if fk==2:
        a=['1','2','3']         
        b=['4','X','6']         
        c=['7','8','9']         

        print '\n',a,'\n',b,'\n',c,'\n'

        t=0
        while True:                                                             
            if t%2==0:
                print "USER TURN"
            else:
                print "Computer had played \n"                                                
            
            
        #Human section
            if t%2==0:
                x=input("\nEnter location: ")

                if x in range(1,10):
                    if x<=3:
                        if a[x-1]=='X' or a[x-1]=='O':
                            print "Invalid Choice"
                            continue
                        a[x-1]='O'
                    elif x<=6:
                        if b[x-4]=='X' or b[x-4]=='O':
                            print "Invalid Choice"
                            continue
                        b[x-4]='O'
                    elif x<=9:
                        if c[x-7]=='X' or c[x-7]=='O':
                            print "Invalid Choice"
                            continue
                        c[x-7]='O'
                    print '\n',a,'\n',b,'\n',c,'\n'
                    t+=1
                    if check_colu(a,b,c) or check_row(a,b,c) or check_diago(a,b,c):         
                        break
                else:
                    print "!!! Invalid Location Choosen !!!"


        #Computer Section
            else:
                if ai_win_move(a,b,c):
                    pass
                elif check_ai_col(a,b,c) or check_ai_row(a,b,c):
                    pass
                elif check_ai_cor(a,b,c):
                    pass
                else:
                    print "!!! \tWell Played\t !!!\n\tMatch Drawn "
                    break
                    
                print '\n',a,'\n',b,'\n',c,'\n'
                t+=1
                if check_colu(a,b,c) or check_row(a,b,c) or check_diago(a,b,c):          
                    break



            if t==9:                                                                     
                print "!!! \tWell Played\t !!!\n\tMatch Drawn "
                break
