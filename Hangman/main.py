import random
import hangman_words
import hangman_art
#Step 1 

hangman_words.word_list

print(hangman_art.logo)
lives = 6

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word = random.choice(hangman_words.word_list)
print(word)

display = []

for letter in word:
  display+="_"

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

while ("_" in display):
  
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"you have already chosen the word {guess}")
  for position in range(len(word)):
    letter = word[position]
    if letter == guess:
      display[position] = letter

  if letter == guess:
    print(f"{guess} is in the word")
      
  if guess not in word:
    lives -= 1
    print(f"{' '.join(display)}")
    print(f"You guessed {guess}, that's not in the word. You lose a life.")

    print(hangman_art.stages[lives])
    if lives == 0:
      print("You lose")
      break
  print(f"{' '.join(display)}")
