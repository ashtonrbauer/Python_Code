#!/bin/python

def main():
	userin = raw_input("Enter an expression : ")
	if userin[0].isalpha(): translation = "true"
	else: translation = "false"
	if "plus" in userin:
		operator = '+'
		userin = userin.split("plus")
	elif "minus" in userin:
		operator = '-'
		userin = userin.split("minus")
	elif "times" in userin:
		operator = '*'
		userin = userin.split("times")
	elif "*" in userin:
		operator = "*"
		userin = userin.split("*")
	elif "-" in userin:
		operator = '-'
		userin = userin.split("-")
	else:
		operator = "+"
		userin = userin.split("+")
	left = userin[0].replace(" ","")
	right = userin[1].replace(" ","")
	if left.isdigit(): left = int(left) 
	else: left = int(unSay(left))
	if right.isdigit(): right = int(right)
	else: right = int(unSay(right))
	if operator == '+': answer = left + right
	elif operator == '-': answer = left - right
	else: answer = left * right
	if translation == "true": print Say(str(answer))
	else: print answer

def Say(myNum):
	ones = ['','one','two','three','four','five','six','seven','eight','nine']
	teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
	tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
	myNum = myNum.zfill(4)
	translation = "";
	if int(myNum) == 0 : print "zero"	
	else:
		thous,huns,ts,os = int(myNum[0]),int(myNum[1]),int(myNum[2]),int(myNum[3])
		if thous ==1:
			translation += "one thousand "
		if huns >=1:
			translation += ones[huns] + " hundred "
		if ts > 1:
			translation += tens[ts] + " "
			if os >= 1:
				translation += ones[os] + " "
		elif ts == 1:
			if os >=1:
				translation += teens[os] + " "	
			else:
				translation += tens[ts] + " "
		else:
			if os >= 1:
				translation += ones[os]
		return translation

def unSay(myWord):
	numDict = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,
		'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,
		'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90}
	if "-" in myWord:
		myWord = myWord.replace("-", " ")	
	num = len(myWord.split())
	thousands = ['zero']
	hundreds = ['zero']
	ones = ['zero']
	if "thousand" in myWord:
		thousands = myWord[:myWord.find("thousand")+8].split()
		myWord = myWord[myWord.find("thousand")+8:]
	if "hundred" in myWord:
		hundreds = myWord[:myWord.find("hundred")+7].split()
		myWord = myWord[myWord.find("hundred")+7:]
	ones = myWord.split()
	digit = (numDict[thousands[0]] * 1000) + (numDict[hundreds[0]] * 100) + (numDict[ones[0]])
	if len(ones) > 1: digit += numDict[ones[1]]
	return digit 


if __name__ == "__main__": main()
