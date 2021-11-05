mail = input("please enter your mail:")
def check  (mail):
    if "@"in mail:
        if "." in mail:
            print("it is a valid e mail")
        else:
            print("it isn't a valid e mail")
    else:
        print("it isn't a valid e mail")
print(check(mail))

