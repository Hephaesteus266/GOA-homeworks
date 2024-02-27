registered_password = "DragonHyde1234"
authorized = False

while authorized != True:
    user_input = input("Please input your password")

    if user_input == registered_password:
        print("Access Granted")
        authorized = True
    else:
        print("password is incorrect")