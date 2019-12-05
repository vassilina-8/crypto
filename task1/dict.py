from os import listdir

dictionary = {chr(a): 0 for a in range(97, 123 ,1 )}

for filename in listdir():
	if '.txt' in filename:
		file = open(filename, 'r')
		letter = file.read(1)
		while letter:
			if letter.isalpha():
				if ord(letter) < 91:
					dictionary[chr(ord(letter)+32)] +=1
				else:
					dictionary[letter] +=1
			letter = file.read(1)
		file.close()

print(dictionary)
