'''
    Note : This code does not contain the logic to refill the insufficient resources 
'''

import functions 
coffee_machine="on"

while coffee_machine=="on":
    choice = int(input("What would you like\n 1.Espresso \n 2.Latte \n 3.Cappuccino\n (Enter the choice number )\n"))
    if(choice==1):
        item="espresso"
    elif(choice==2):
        item="latte"
    elif(choice==3):
        item="cappuccino"
    menu= functions.get_menu()
    resources = functions.get_resources()
    water = menu[item]["ingredients"]["water"]
    coffee = menu[item]["ingredients"]["coffee"]
    milk = menu[item]["ingredients"]["milk"]

    if(water>resources["water"]):
        print("Not enough water needs refill !! Sorry for the inconvenience, please try again later")
        break
    elif(coffee>resources["coffee"]):
        print("Not enough coffee needs refill !! Sorry for the inconvenience, please try again later")
        break
    elif(milk>resources["milk"]):
        print("Not enough milk needs refill !! Sorry for the inconvenience, please try again later")
        break

    else:

        cost = menu[item]["cost"]
        print(f"It costs {cost}\n")
        coins_string=(input("Please insert the coins !! (Enter in format 1 2 3 4)"))
        coins=coins_string.split(" ")
        print(coins)
        # coins=[int(x) for x in coins]
        balance = functions.calculate_balance(coins,cost)
        balance = float(balance)
        if(balance>0):
            balance = "{:0.2f}".format(round(balance,2))
            print(f"Here's is your change {balance}\n")
        elif(balance<0):
            while(balance<0):
                print(f"Not enough coins are inserted !! Need {-1*balance}\n Coins returned. ")
                coins_string=(input("Please insert the coins !! (Enter in format 1 2 3 4)"))
                coins=coins_string.split(" ")
                # coins=[int(x) for x in coins]
                balance = functions.calculate_balance(coins,cost)
                if(balance >=0):
                    break
        
        print(f"Please wait while the {item} is brewing \n")
        resources["water"]= resources["water"]-water 
        resources["coffee"]= resources["coffee"]-coffee
        resources["milk"]=resources["milk"]-milk
        resources["cost"]=resources["cost"]+cost

        functions.update_resources(resources)
        print(f"Here is your {item}. Enjoy !! ")

        coffee_machine=input("Next Please. (For maintenance type 'off') or for reports type 'report' \n")
        if(coffee_machine.lower()=="report"):
            resources_check = functions.get_resources()
            print(f"Water: {resources_check['water']}ml")
            print(f"Milk: {resources_check['milk']}ml")
            print(f"Coffee: {resources_check['coffee']}g")
            print(f"Cost: ${resources['cost']}")
            coffee_machine="on"
        elif(coffee_machine.lower()=="off"):
            print("Closing Coffee Machine")
            break
        else:
            coffee_machine="on"

