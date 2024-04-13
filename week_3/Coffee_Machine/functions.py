import json 

#Get the menu 
get_menu = lambda:json.load(open('menu.json', 'r'))

#Get the resources 
get_resources= lambda:json.load(open('resources.json', 'r'))

#Update the resources 
update_resources = lambda data:json.dump(data,open('resources.json','w'))

#To calculate the change 

def calculate_balance(coins,cost):
    (quarters, dimes, nickles, pennies) = [int(x) for x in coins[:4]]
    quarters = 0.25 * quarters
    dimes = 0.10 * dimes
    nickles=0.05 * nickles
    pennies = 0.01 * pennies
  
    total = quarters+dimes+nickles+pennies
    if(total==cost):
        return 0
    elif(total<cost) : 
        return total-cost
    elif(total>cost):
        return total-cost  




