'''

1- random

2- random.choice

3- display _

4 - Func()



'''





import random

words = [
    "APPLE",
    "BANANA",
    "ICECUDE",
    "SWIM",
    "DIVE"
]

# Choose a random secret word
secret = random.choice(words)

# Convert secret word to uppercase
secret = secret.upper()

print(type(secret))

# secret = "HELLO"

# for _ in secret:
#     print('_')


# Create a display list like _ _ _
display = ['_' for _ in secret]   #list comprehension


print("\n HANGMAN GAME STARTS \n")
def game():

    '''
    Inside it we will check  a secret value in a var simple...
    
    '''


    # Set number of lives
    lives = 5
    while lives > 0 and '_' in display:
        print("Word: ", ' '.join(display))
        print("Lives left:", lives)

        guess = input("Guess a letter: ").upper()







        if guess in secret:
            for i in range(len(secret)):
                if secret[i] == guess:
                    display[i] = guess
            print("Correct!\n")
        else:
            lives -= 1
            print(" Wrong!\n")





game()    #We can call this func multiple times too if u wanna play again and again
# Final Result
if '_' not in display:
    print("You guessed it! The word was:", secret)
else:
    print("💀 Game over! The word was:", secret)
