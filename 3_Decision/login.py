user_name_default = 'admin'
password_default = "123456"

user_given_name = input("Enter your Username: ")
user_given_password = input("Enter your Password: ")

if user_given_name == user_name_default and user_given_password == password_default:
    print("Login successful.")
else:
    print("Invalid Credentials. Please try again")