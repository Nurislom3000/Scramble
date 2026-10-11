# Scramble

from random_word import RandomWords

rand = RandomWords()

random_word = rand.get_random_word().lower();

while not random_word.isascii() or not random_word.isalpha():
	random_word = rand.get_random_word().lower()

random_word = list(random_word)

print(f'Word length is: {len(random_word)}. \nYou have to guess the word');
user_word = None;

while user_word != random_word:
	user_word = list(input('Write your guess: ').lower());

	if len(user_word) != len(random_word):
		print(f'Man it has to be exactly {len(random_word)} letters');

	else: 
		letters_left = list(random_word)

		for letter_index in range(len(user_word)):
			if user_word[letter_index] == random_word[letter_index]:
		 		letters_left.remove(user_word[letter_index]);


		for letter_index in range(len(user_word)):
		 	if user_word[letter_index] == random_word[letter_index]:
		 		print(f'{user_word[letter_index]} -- YES');

		 	elif user_word[letter_index] != random_word[letter_index]:
		 		if user_word[letter_index] in letters_left:
		 			print(f'{user_word[letter_index]} -- YES but wrong position');
		 			letters_left.remove(user_word[letter_index]);
		 		else: 
		 			print(f'{user_word[letter_index]} -- NO');
		 	
		 	else:
		 		print('Internal error');

print('you won')