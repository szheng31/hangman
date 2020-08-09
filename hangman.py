from random_words import RandomWords
rw = RandomWords()
word = rw.random_word()
hangman_word = rw.random_word()
print(hangman_word)
the_blanks = '_' * len(hangman_word)
the_blanks = list(the_blanks)

index = 0
index_deaths = 0

while index_deaths < 6:
		the_blanks_string = ''
		for i in the_blanks:
			the_blanks_string += i
		if the_blanks_string == hangman_word:
				break
		user_ask = input("""Guess a letter or the word.
		""")
		if str(user_ask) == hangman_word:
				break

		elif user_ask in hangman_word:
			print('Yes you got one character.')
			while(index < len(hangman_word)):
				if hangman_word[index] == user_ask:
					the_blanks[index] = hangman_word[index]
					index += 1
				else:
					index += 1
			index = 0
			the_blanks_copy = ''
			for b in the_blanks:
				the_blanks_copy += b
			print(the_blanks_copy)

		elif the_blanks_string == hangman_word:
				break
		else:
				print('Nope, not a character.')
				index_deaths += 1

if index_deaths < 6:
		print("YOU GOT THE WORD!!")

else:
		print('try again?')
