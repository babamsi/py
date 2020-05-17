
name = 'jacir'


def Into():
    print("my name is ", name)
    print("my other name is ibraahim")

#Into()

#def add(x, y):
    #print(x + y)

#add(7,5)

# def power(base, exponent):
#     result = 1

#list = [2,5,62,6]
#for num in list:
 #   print('jaciir')

#for name in range(1,5):
#    print("jaciir")




#def sub (k,s):
 #   print(k - s)
#sub(8,4)

#kali = [7, 8, 9, 4, 2, 5]
#for noun in kali:
 #   print(noun + 2)









#for aljaca in range(1,20):
 #    print('shariif')


#print() 

# count = 0

# while count != 3:
#     print('jaciir')
#     count = count + 1

# userPass = input("what is paas? ")
# password = '12345';

# while userPass != password:
#     userPass = input("what is paas? ")











# mom = {
#     "username":"suhayb",
#     "password":"12354"
# }
# kali = input("what is username? ");
# ilak = input("what is password ? ");


# def cheking(username,passwor):
#     if mom["username"] == username and mom["password"] == passwor:
#         print("waa mahadsan thy ")
#     else:
#         print(" waa qaldan danthy ")

# cheking(kali, ilak)





database = [
    {"username": 'suhayb Abdalla',
    "password": "616989940"} , {"username": "jorah qaldan",
    "password": "616484913"} , {"username": "ibraahim jaciir",
    "password": "616460814"}
]

mom = input(" horay miyaad u lahayb acount ? (yes) or (no) ")

def main ():
    if mom.upper() == "yes".upper():
        username = input(" what is username ? ")
        password = input(" what is password ? ")
        for nuon in database:
            if nuon["username"] == username and nuon["password"] == password:
                print('thank for using my project')
                break;
            else:
                print(" please check your username or password")
    elif mom.upper() == "no".upper():
        print(" create new acount ")
        new_username = input(" enter your new username ? ")
        new_password = input(" enter your new password ? ")
        database.append({"username": new_username, "password": new_password});
    else:
        print(" I don't recognize you answer")

main()







passwor " shariifcade1436"