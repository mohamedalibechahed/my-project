database=[]
def register():
    username=input("enter your name:")
    passwd=input("enter your password:")

    database.append(username)
    database.append(passwd)
    print("regisster succesfuly")
register()
def login():
    print("page login")
    username=input('enter your user name:')
    passwd=input('enter your user password:')

    if database[0]==username and database[1]==passwd:
         print('welcom')
    elif database[0]!=username and database[1]==passwd:
        print("erreur check your user name!")
    elif database[0]==username and database[1]!=passwd:
        print('erreur check your password !')  
    else:
        print("erruer")    
login()