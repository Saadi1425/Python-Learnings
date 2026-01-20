sec_num= 7
i=0
while True:
    i=int(input("Enter The Secret Number"))
    if i==sec_num:
        print("You Guess Right")
        break
    elif i>sec_num:
        print("Too High Guess")
    else: 
        print("Too Low")