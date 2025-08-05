import random as r
print("-"*100)
print("Random Number Generator")
print("-"*100)
while(True):
    print("Enter any key to randomly generate a number")
    print("Enter 0 to exit")
    i=input()
    if(i=='0'):
        break
    else:
        ra=r.randint(1,100)
        print("Random Number Generated : ",ra)
        if(ra>90):
            print("Yayyy!!\nThats a high number!!!\nLuckyyy!!!!!")
    print("\n")
    print("*"*100)
    print("\n")