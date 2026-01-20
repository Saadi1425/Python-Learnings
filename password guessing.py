password=1234
tries=0
while True:
    guess=int(input("Enter The Password"))
    tries+=1
    if guess==password:
        print("Correct Password")
        print("You've tried password",tries,"Time")
        break
    else:
        print("Wrong Try Again")
        print("You Have Tried password",tries,"Times")