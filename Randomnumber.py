import random

flag=True
while flag:
    
    while flag:
        num=input("Type a number for an limit")
        if num.isdigit():
            print("Let'start the game")
            num=int(num)
            flag=False

        else:
            print("Enter a valid number again!!")

    snumber=random.randint(1,num)
    guess=None
    count=1

    while guess != snumber:
        guess=input("Type a number between 1 and"+str(num)+":")
        if guess.isdigit():
            guess=int(guess)

        if guess==snumber:
            print("You found it")
        else:
            print("please try again")
            count+=1

    print("It took you",count,"guesses!")
        
    
    
                  
