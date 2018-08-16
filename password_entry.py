"""Christopher Ordorica"""

MIN_LENGTH = 6

password_length = len(input("Please enter a password that is {} characters long.".format(MIN_LENGTH)))
while password_length < MIN_LENGTH:
    password_length = len(input("Invalid Password. \nPlease enter a valid password"))
print("*" * password_length)
