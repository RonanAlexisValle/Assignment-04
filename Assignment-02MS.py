#This asks the user on how many apples and oranges they want to buy
def userInput():
    boughtapple_func = int(input("How many apples you want to buy: "))
    boughtorange_func = int(input("How many oranges you want to buy: "))
    totalprice_func = ((boughtapple_func*20) + (boughtorange_func*25))
    return boughtapple_func, boughtorange_func, totalprice_func

#This shows the total amount of the user needed to pay
def displayOutput(boughtapple_func, boughtorange_func, totalprice_func):
    print(f"Total amount is {totalprice_func}")

boughtapple_func, boughtorange_func, totalprice_func = userInput()

displayOutput(boughtapple_func, boughtorange_func, totalprice_func)
