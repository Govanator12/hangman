import random

class Hangman():

    def __init__(self):
        pass

    # play function that actually handles the game

    def play(self):
        # defining some variables to be used later
        guesses = []
        guesses_remaining = 7

        colors = ['red', 'blue', 'green', 'beige', 'teal', 'black', 'orange', 'purple', 'gold', 'brown', 'yellow']

        animals = ['dog', 'cat', 'bear', 'hawk', 'lion', 'cow', 'horse', 'fish', 'pig', 'alligator']

        video_games = ['halo','starcraft', 'tekken', 'squad', 'skate', 'warcraft', 'spore', 'killzone', 'spyro', 'mario']

        while True:
            print('Please select a category using a number:')
            print('1. Colors')
            print('2. Animals')
            print('3. Video games')

            category = int(input())
            word = ""

            if category == 1:
                word = random.choice(colors)
                break

            elif category == 2:
                word = random.choice(animals)
                break

            elif category == 3:
                word = random.choice(video_games)
                break

            else:
                print('Please select an option from the menu by entering a number')

        characters = list(word)

        while True:
            for letter in word:
                if letter in guesses:
                    print(f'{letter} ', end ='')
                else:
                    print('_ ', end = '')

            if set(characters).issubset(guesses):
                print('Nice work you win!')
                break

            print(f'\nYou have {guesses_remaining} guesses remaining')
            print(f'Your guesses so far: {guesses}')

            if guesses_remaining > 0:
                current_guess = input(f'Guess again!: ')

                if (len(current_guess) > 1) or current_guess.isalpha() == False:
                    print('Please only guess single letters')
                    continue

                elif current_guess.lower() in guesses:
                    print(f"You've already guessed '{current_guess}'!")
                    continue

                else:
                    guesses.append(current_guess.lower())

                    if current_guess in word:
                        print('\nGood guess! \n\n')

                    else:
                        print('\nNo dice :( \n\n')
                        guesses_remaining -= 1

            else:
                print(f'Out of guesses! Your word was {word} Better luck next time!')
                break

    # menu function that starts the game

    def menu(self):
        while True:
            print("\n\nWELCOME TO HANGMAN")
            print("-------------------")
            ans = input('Play a game? (Y/N): ')

            if ans.lower() == 'y':
                Hangman.play(self)

            elif ans.lower() == 'n':
                print('Thanks for playing!')
                break

            else:
                print('Please enter "Y" or "N"')


my_hangman = Hangman()
my_hangman.menu()
