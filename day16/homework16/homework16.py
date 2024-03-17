def ask_(): #im not writing black guy, sounds weird af
    print("Black raven: What kind of a man are you?")
    response = int(input("1) fight\n2)FRIENDSHIP IS MAGIC\n3)take money\n"))
    return response


def decide_fate(response):
    if response ==1:
        return "Black Raven: Your freaking dead kid!"
    elif response == 2:
        return "Black Raven: Maybe yur not so bad?"
    elif response == 3: 
        return "Black Raven: Give me back my money bastard!"
    else:
        return "Try again later dimwit"
    
while True:
    response = ask_()
    print(decide_fate(response))
    cont = input("wanna continue? (Y/N): ")
    if cont == "N":
        break