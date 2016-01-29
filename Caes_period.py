#!/bin/python

file = raw_input("Enter the name of your file: ")
file = open(file, "r").read().lower()
most_occ = sec_most_occ = 0 
most_occ_char = sec_most_occ_char = '*'
for lines in file:
	for char in lines:
		count = file.count(char)
		if char.isalpha() and count > most_occ:
			most_occ_char = char
			most_occ = count
		elif char.isalpha() and count > sec_most_occ and count != most_occ:
			sec_most_occ_char = char
			sec_most_occ = count
key_a = ord('e') - ord(most_occ_char)
key_b = ord('t') - ord(sec_most_occ_char)
if key_a == key_b:
	final_key = 26 + key_a
	if final_key > 26:
		final_key -= 26
	print "Your key:" , final_key
else:
	final_key = 26 + key_a
	if final_key > 26:
		final_key -= 26
	print final_key 
