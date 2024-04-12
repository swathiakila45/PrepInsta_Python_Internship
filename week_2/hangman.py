import random
word_list=["onepiece","naruto","onepunchman","deathnote","bleach","bluelock","haikyuu","demonslayer","attackontitan","fullmetalalchemist"]

#Choosing a random word 
choice = random.choice(word_list)

#Creating a list with _ for the chosen word 
choice_word = ['_' for letter in choice]

#Start of game
print("Guess the anime HANGMAN Version \n")
 
print(f"The word you need to guess is of length {len(choice)}\n")
print(choice_word)

#Game logic 
lives=6 
while '_' in  choice_word:
    letter_guessed = input("Guess a letter ")
    if(letter_guessed.isalpha() and len(letter_guessed)==1):
        if(letter_guessed not in choice_word):
            letter_guessed.lower()
            if(letter_guessed in choice):
                for position,letters in enumerate(choice):
                    if letters==letter_guessed:
                        choice_word[position]=letter_guessed  
                print(choice_word)       
            else:
                lives-=1
                print(f"Wrong Guess!! You have {lives} lives remaining. Guess Again\n")   
        else:
            lives-=1
            print(f"Already guessed that Letter!!You have {lives} lives remaining. Try another one\n")
    else:
        lives-=1
        print(f"Wrong Guess!! You have {lives} lives remaining. Guess Again\n")
    if(lives==0):
        break 

#Result
if('_' not in choice_word):
    print(f"\nYou have guessed the Anime {choice.upper()}")
else:
    print("\nYou lose!!")



