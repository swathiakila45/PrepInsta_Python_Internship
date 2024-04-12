import random 

#Generating random number to guess
number= random.randint(1,100)

# Getting player name 
playerName = input("Enter your name !!\n")
print(f"Hello {playerName}")

#Choosing the difficulty level 
difficulty_level = input("Choose a difficulty level EASY or HARD !\n")
attempts = 0
while True: 
    if(difficulty_level.lower()=="easy" or difficulty_level.lower()=="hard"):
        break
    else: 
        print("You have given a wrong choice. Choose the difficulty level between Easy or Hard !!\n")
        difficulty_level = input("Choose a difficulty level EASY or HARD !\n")  

if(difficulty_level.lower()=="easy"):
    attempts=10
elif(difficulty_level.lower()=="hard"):
    attempts=5

print(f"You have selected {difficulty_level}. You have {attempts} attempts\n")

#Game logic

guesses=1
guessed=0
while(guesses<=attempts):
    guess= int(input("Make a guess between 1 and 100 !!\n"))
    if(guess>=1 and guess<=100):
        if(guess>=number-10 and guess<=number-1):
            print("Close enough ! Just a few numbers less")
        elif(guess<number):
            print("Your guess is too low than the number. Guess Again ")
        elif(guess<=number+10 and guess>=number+1):
            print("Close enough ! Just a few numbers high")
        elif(guess>number):
            print("Your guess is too high than the number. Guess Again ")
        else: 
            print(f"You guess it right in {guesses} attempt(s)")
            guessed=1
            break
    else:
        print("Guess only between 1 to 100 !!")
    guesses = guesses+1

#Checking if the player guessed the number 
if(guessed==0):
    print("Exceeded the number of attempts. Game Over !!")


