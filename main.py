import re


answer = "Whats up, Doc?"

answer = answer.upper()

#Pre-game setup
answer_letters = list()
guessed_letters = list()

for current_awnser_character in answer
    if re.search("[^A-Z$]", current_awnser_character):
        answer_letters.append(False)
    else:
        answer_letters.append(True)

# Game logic.
number_of_incorrect_guesses = 0
TOTAL_INCORRECT_GUESSES_ALLOWED = 5

while number_of_incorrect_guesses < TOTAL_INCORRECT_GUESSES_ALLOWED and False in answer_letters:
   print(f"Number of Incorrect Guesses Left: {TOTAL_INCORRECT_GUESSES_ALLOWED - number_of_incorrect_guesses}")
   print()
   
   print("Guessed Letters: ", end = "")

   for current_guessed_letter in guessed_letters:
        print(current_guessed_letter, end = " ")

        print()
        print()

    #puzzle board logic
   for current_answer_index in range(len(answer)):
        if answer_letters[current_answer_index ]:
            print(answer[current_answer_index], end ="")
        else:
            print("_", end = "")

print()
print()

   #let user guess a letter
letter = input("Enter a letter: ")

letter = letter.upper()

if re.search("^[A-Z]$", letter) and len(letter) == 1 and letter not in guessed_letters:
    # Process Letter
    letter_insert_index = 0

    for current_guessed_letter in guessed_letters:
        if current_guessed_letter > letter:
        break

    letter_insert_index += 1 

    guessed_letters.insert(letter_insert_index, letter)

    #see if letter is in puzzle
    if letter in answer:
        for current_answer_index in range(len(answer)):
            if answer[current_answer_index]== letter:
                answer_letters[current_answer_index] = True
    else:
        number_of_incorrect_guesses += 1
print()
print()
# POST-GAME SUMMARY
if number_of_incorrect_guesses < TOTAL_INCORRECT_GUESSES_ALLOWED:
    print("Congratulations! You solved the puzzle.")
else:
    print("sorry! You ran out of guesses.")

    print()
    print(f"The anser was {answer}")

        

        
