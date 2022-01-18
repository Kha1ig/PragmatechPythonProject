def users():
    user = input(' istifadeci adinizi daxil edin: ')

    usernames = ['Ali', 'Murad', 'ADMIN',]

    if user in usernames:
        if user == ('ADMIN'):
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'''Hello {user}, thank you for logging in again.''')
        
    else:
        print('siz login olmamisiniz')
        
users()