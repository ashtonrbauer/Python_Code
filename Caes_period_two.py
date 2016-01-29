#!/bin/python
print "Your decoded file will be saved to \"new_file.txt\"."
file_origin = raw_input("Enter the name of your file: ")
file = open(file_origin, "r").read().lower()
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
else:
	final_key = 26 + key_a
	if final_key > 26:
		final_key -= 26


f = open("new_file.txt", "w")
f_t_r = open(file_origin, "r")
reader = list(f_t_r.read())
for char in reader:
        if char.isalpha():
                new_char = ord(char.lower()) + final_key
                if new_char > 122:
                        new_char = new_char - 26
                new_char = chr(new_char)
                f.write(new_char)
        else:
                f.write(char)
print "Your original: "
f_t_r = open(file_origin, "r")
for line in f_t_r:
        print line
print "Your new file: "
f = open("new_file.txt", "r")
for line in f:
        print line
