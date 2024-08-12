USERNAME = input("Username > ")
PASSWORD = input("Password > ")
with open(USERNAME, 'w') as f:
    f.write(f'{USERNAME} {PASSWORD}')
