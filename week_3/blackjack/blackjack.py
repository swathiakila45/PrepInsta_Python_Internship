import random

def deal_card():
    cards =[11,2,3,4,5,6,7,8,9,10,10,10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) ==21 and len(cards)==2:
        return 0
    elif sum(cards)>21 and 11 in  cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(user_score,comp_score):
    if user_score==comp_score:
        return "Draw"
    elif comp_score == 0:
        return "Computer has  Blackjack! You loose"
    elif user_score==0:
        return "You win the game with the BlackJack!"
    elif user_score>21 and comp_score>21:
        return "Bummer you busted  ! You Loose"
    elif user_score > 21:
        return "Bummer you busted ! You Lose"
    elif comp_score > 21:
        return  "Opponent Bust ! You Win!"
    elif user_score>comp_score:
        return "You win !"
    else:
        return "Computer wins !"
        

user_cards=[]
computer_cards=[]

for  x in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


while True:
    user_score=calculate_score(user_cards)
    comp_score=calculate_score(computer_cards)

    print(f"Your cards are {user_cards}, Score: {user_score} ")
    print(f"Computer's first card {computer_cards[0]}")

    if user_score>21 or comp_score==0 or user_score==0:
        break

    else:
        choice=input("Do you want to hit or stand? Enter 'h' for hit or 's' for stand :").lower()
        while choice!='h'and choice !='s':
            choice=input("Invalid input please enter again . Do you want to hit or stand? Enter 'h' for hit or 's' for stand").lower()
        if choice=='h':
            user_cards.append(deal_card())
        else:
            break
    
while comp_score!=0 and comp_score<17:
    computer_cards.append(deal_card())
    comp_score=calculate_score(computer_cards)

print(f"Your  final hand is {user_cards}, your score is {user_score}\n")
print(f"The computers final hand is {computer_cards}, the computers score is {comp_score}\n")
print(compare_score(user_score,comp_score))



