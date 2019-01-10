def play_game(secret_phrase, num_guesses):
    total_guesses = ""
    incorrect_guesses = 0
    letters_guessed = ""
    letters_guessed_lower = letters_guessed
    total_guesses = ""
    correct_guesses = 0
    not_valid_list = ""
    while True:
        # calls draw_scoreboard
        draw_scoreboard(num_guesses, incorrect_guesses)
        end = "\"!\""
        print("Secret Phrase:   " + \
                  get_display_secret_phrase(secret_phrase, total_guesses))
        # calls display_secret_phrase

        display_guessed_letters(total_guesses.lower())
        # calls display_guessed_letters with all the total guesses made so far

        #prompts user to input a letter or ! to end game
        letters_guessed = input("Enter a letter to guess or {} to end the game\n".format(end))

        #finds if a letter has already been guessed and if so doesn't add to total_guesses and re iterates loop
        if letters_guessed.lower() in total_guesses.lower():
            print("You already guessed {}".format(letters_guessed))
            continue

        #ends game if ! is entered
        elif letters_guessed == "!":
            print("=======================================")
            print("Game ended early")
            print("=======================================")
            break

        #prints not valid if anything other than a letter or ! is inserted
        if letters_guessed.isalpha() != True:
            print("Not a valid guess!")
            continue

        #ends game if ! is entered
        #prompts input

        total_guesses += letters_guessed

        #appends each guessed letter to the variable total guesses

        if letters_guessed.isalpha() == True:
            for i in letters_guessed:
                if letters_guessed.lower() not in secret_phrase.lower():
                    print("No, {} is not in the phrase\n".format(letters_guessed))
                    incorrect_guesses += 1
                    #turns += 1
                elif letters_guessed.lower() in secret_phrase.lower():
                    correct_guesses += 1


        if num_guesses == incorrect_guesses:
            # prints all incorrect guesses of draw_scoreboard
            draw_scoreboard(incorrect_guesses, incorrect_guesses)
            #ends game when all incorrect guesses have been used
            print("=======================================")
            print("No more guesses left. Game over!\nThe phrase was \"{}\"".format(secret_phrase))
            print("=======================================")
            break

        #if the amount of correct guesses equals the length of secret phrase then the game is won
        if correct_guesses == length_guessed_letter(secret_phrase):
            print("=======================================")
            print("You won!\nThe phrase was \"{}\"".format(secret_phrase))
            print("=======================================")
            break

#method for the length of secret_phrase
def length_guessed_letter(secret_phrase):
    length = len(secret_phrase)
    if secret_phrase.find("'") != -1:
        length -= 1
    elif secret_phrase.find(" ") != -1:
        length -= 1
    return length



def get_display_secret_phrase(secret_phrase, guessed_letters):
    secret_phrase_lower = secret_phrase.lower()
    guessed_letters_lower = guessed_letters.lower()
    result = ""
    for i in range(0, len(secret_phrase)):
        if secret_phrase[i] == "'":
            result += secret_phrase[i]
        elif secret_phrase[i] == " ":
            result += secret_phrase[i]
        else:
            if guessed_letters_lower.find(secret_phrase_lower[i]) != -1:
                result += secret_phrase[i]
            #current letter in secret phrase is guessed
            elif guessed_letters_lower.find(secret_phrase_lower[i]) == -1:
                result += "-"
    return result


def display_guessed_letters(guessed_letters):
    total_guesses = ""
    total_guesses += guessed_letters
    print("Guessed Letters: ", end="")
    if len(guessed_letters) == 0:
      print()
    else:
      for total_guesses in guessed_letters[0:-1]:
            print(total_guesses.lower(), end = ", ")
      print(guessed_letters[-1])
    # return total_guesses

def draw_scoreboard(total_guesses, incorrect_guesses):
    not_correct = 0

    for i in range(total_guesses):
        print('+-----', end="")
    print("+")

    print("|", end="")
    for i in range(total_guesses):
        if not_correct < incorrect_guesses:
            print('\\\\ //|', end="")
            not_correct += 1
        else:
            print('     |', end="")

    print("")
    print("|", end="")
    not_correct = 0
    for i in range(total_guesses):
        if not_correct < incorrect_guesses:
            print(' \\V/ |', end="")
            not_correct += 1
        else:
            print('     |', end="")

    print("")
    print("|", end="")
    not_correct = 0
    for i in range(total_guesses):
        if not_correct < incorrect_guesses:
            print(' /.\\ |', end="")
            not_correct += 1
        else:
            print('     |', end="")

    print("")
    print("|", end="")
    not_correct = 0
    for i in range(total_guesses):
        if not_correct < incorrect_guesses:
            print('// \\\\|', end="")
            not_correct += 1
        else:
            print('     |', end="")

    print("")
    for i in range(total_guesses):
        print('+-----', end="")
    print("+")


if __name__ == '__main__':
    guess_secret = input()
    guess_num = int(input())
    play_game(guess_secret, guess_num)
