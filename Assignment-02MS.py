#This asks the user the amount of money they have and how much the apple costs
def userInput():
    Money = int(input("Amount of money you have: "))
    applePrice = int(input("How much does apple cost?: "))
    applesinTotal = Money//applePrice
    change = Money%applePrice
    return Money, applePrice, applesinTotal, change
    
#This displays how many apples the user can buy and its change if there is any
def letuserKnow(Money, applePrice, applesinTotal, change):
    print(f"You can buy {applesinTotal} apples and your change is {change} pesos.")

Money, applePrice, applesinTotal, change = userInput()

letuserKnow(Money, applePrice, applesinTotal, change)
