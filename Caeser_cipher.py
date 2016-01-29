#!/bin/python

print "Key can be between 0 and 26."
key = raw_input('Enter your key: ')
while key.isdigit() != True and (key < 0 or key > 26):
	key = raw_input("Out of bounds, enter your key: ")
key = int(key)
file_to_read = raw_input("Enter file name you wish to encode: ")
file_to_write = raw_input("Enter name of file you wish to create: ")
f = open(file_to_write, "w")
f_t_r = open(file_to_read, "r")
reader = list(f_t_r.read())
for char in reader:
	if char.isalpha():
		new_char = ord(char.lower()) + key
		if new_char > 122:
			new_char = new_char - 26
		new_char = chr(new_char)
		f.write(new_char)
	else:
		f.write(char)
print "Your original: "
f_t_r = open(file_to_read, "r")
for line in f_t_r:
	print line
print "Your new file: "
f = open(file_to_write, "r")
for line in f:
	print line
