print('HELLOO AND WELCOME TO OUR NEW REGISTRING SYSTEM');
print('')
print('IF YOU HAVE ALREADY REGISTRED YOU CAN LOGIN');
print('');
print('WE ARE HAPPY TO BE HERE WELCOM AND USE THIS SYSTEM');

ans = input('HAVE YOU ALREADY ACCOUTN ? (YES) OR (NO): ');
allNames = [];

def reg(name, email, username, password):
    name = input('ENTER YOUR NAME: (at least 6 charecter)  ');
    
    while len(name) >= 6:
        email = input('ENTER YOU EMAIL ACCOUNT: (most include @gmail.com)  ');
        while email.upper().endswith('@gmail.com'.upper()) == True:
            username = input('ENTER A USERNAME: (this name the people sees) ');
            while len(username) >= 4:
                password = input('ENTER YOUR PASSWORD (atleast 6 character)');
                
            if len(password) >= 6:
                 print('nooo')
    
            
    

name = '';
email = '';
username = '';
password = '';
reg(name, email, username, password);
