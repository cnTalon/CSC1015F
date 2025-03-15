# vending machine simulator
# 15 March 2022

cost = eval(input("Enter the cost (in cents):\n"))
dep =0
while cost != 0:                           # condition 
    dep += eval(input("Deposit a coin or note (in cents):\n"))                             # adds up values
    if dep > cost:
        change = dep - cost
        print("Your change is:")
        if change >= 500:
            r5="R5"
            amt = int(change/500)               # convers cents into coin
            change = change - amt*500           # left over after conversion
            print(amt*1,"x",r5)
        if change >= 200:
            r2="R2"
            amt = int(change/200)
            change = change - amt*200
            print(amt*1,"x",r2)
        if change >= 100:
            r1="R1"
            amt = int(change/100)
            change = change - amt*100
            print(amt*1,"x",r1)
        if change >= 50:
            c50="50c"
            amt = int(change/50)
            change = change - amt*50
            print(amt*1,"x",c50)
        if (change >= 20 and change < 50):
            c20 = "20c"
            amt = int(change/20)
            change = change -amt*20
            print(amt*1,"x",c20)
        if (change >= 10 and change < 20):
            c10 = "10c"
            amt = int(change/10)
            change = change -amt*10
            print(amt*1,"x",c10)
        if (change >= 5 and change < 10):
            c5 = "5c"
            amt = int(change/5)
            change = change - amt*5
            print(amt*1,"x",c5)
        if change == 0 or dep == 0:
            break                 
    if dep == cost:
        break                        # prevents infinite loop