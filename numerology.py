#!/usr/bin/python
# -*- coding: utf-8 -*-

# calculates the numerological number (pytagoras) from words in a wordlist

#creae a dictionary with name and value
name_value = {}

letter_numbers = {  'A': 1, 'J': 1, 'S': 1,
					'B': 2, 'K': 2, 'T': 2,
					'C': 3, 'L': 3, 'U': 3,
					'D': 4, 'M': 4, 'V': 4,
					'E': 5, 'N': 5, 'W': 5,
					'F': 6, 'O': 6, 'X': 6,
					'G': 7, 'P': 7, 'Y': 7,
					'H': 8, 'Q': 8, 'Z': 8,
					'I': 9, 'R': 9, }

#read words as a list
input_file = 'words.txt'
words = open(input_file)
wordlist = words.read().splitlines()
words.close()

# value of word
wordvalue = 0

#loop trough wordlist
for word in wordlist:

	#reset value
	wordvalue = 0

	#loop trough each character from word
	for i in range(0,len(word)):
		#print word[i]
		wordupper = letter_numbers.get(word[i].upper())
		
		#ignore the blanks
		if wordupper != None:
			wordvalue += int(wordupper)

	#sort out 11 and 22 as they're a special number
	if wordvalue != 11 and wordvalue != 22:
		#do as long as bigger as 9
		while wordvalue > 9:
			wordvalue = sum(int(digit) for digit in str(wordvalue))
			#if you want to see the calculation steps, uncomment the next line
			#print wordvalue
			if wordvalue == 11 or wordvalue == 22:
				break

	name_value[word] = wordvalue

#count for every word the value (together)
for x in (1,2,3,4,5,6,7,8,9,11,22):
	print str(x) + " : " + str(sum( y == x for y in name_value.values() ))

#ignore the words if a specific char is in it
chars = set('yzqj')

number=input('Choose Number to show words: ')

#show word and value based on the input number, filters out the words based on chars set
for word, value in name_value.items():
	if not any((c in chars) for c in word) and value == number:
		print word + " : " + str(value)
