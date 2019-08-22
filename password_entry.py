"""
Louis Bortolotto
"""
MIN_LENGTH = 10
password = str(input("What is your password?"))
while len(password) < 10:
    password = str(input("password must be 10 characters or more"))
for i in range(len(password)):
    print("*", end='')
