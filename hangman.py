from random_word import RandomWords
r = RandomWords()

class Hangman():

    def __init__():
        pass

    # play function that actually handles the game

    def play():

        # defining some variables to be used later
        guesses = []
        guesses_remaining = 7

        while True:
            print('Please select a category using a number:')
            print('1. Verbs')
            print('2. Nouns')
            print('3. Adjectives')
            print('4. Random')

            category = int(input())
            word = ""

            if category == 1:
                word = r.get_random_word(includePartOfSpeech='verb')
                break

            elif category == 2:
                word = r.get_random_word(includePartOfSpeech='noun')
                break

            elif category == 3:
                word = r.get_random_word(includePartOfSpeech='adjective')
                break

            elif category == 4:
                word = r.get_random_word()
                break

            else:
                print('Please select an option from the menu by entering a number')

        while True:
            for letter in word:
                if letter in guesses:
                    print(f'{letter} ', end ='')
                else:
                    print('_ ', end = '')
            print(f'\nYou have {guesses_remaining} remaining')
            print(f'Your guesses so far: {guesses}')

            if guesses_remaining > 0:
                current_guess = input(f'You have {guesses_remaining} guesses left. Guess again!: ')

                if (len(current_guess) > 1) or !current_guess.isalpha():
                    print('Please only guess single letters')
                    continue

                elif current_guess in guesses:
                    print(f"You've already guessed '{current_guess}'!")
                    continue

                else:
                    guesses.append(current_guess)
                    guesses_remaining -= 1

            else:
                print('Out of guesses! Better luck next time!')
                break

    # menu function that starts the game

    def menu():
        while True:
            print("\n\nWELCOME TO HANGMAN")
            print("-------------------")
            ans = input('Play a game? (Y/N): ')

            if ans.lower() == 'y':
                play()

            elif ans.lower() == 'n':
                print('Thanks for playing!')
                break

            else:
                print('Please enter "Y" or "N"')
