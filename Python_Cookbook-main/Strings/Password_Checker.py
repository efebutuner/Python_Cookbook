username = input("Username: ")
password = input("Password: ")

hyphen = len(password) * '*'

print(f'{username}, Your password {hyphen} is {len(password)} letters long!')