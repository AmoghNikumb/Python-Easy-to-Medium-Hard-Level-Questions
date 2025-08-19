email = input("Enter your email address: ")
if '@' in email:
    username, domain = email.split('@', 1)
    print("User Name:", username)
    print("Email:", domain)
else:
    print("Invalid email format.")
