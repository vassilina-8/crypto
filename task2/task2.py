import random
import argparse
import json

def count(filename):
	file = open(filename, 'r')	
	dict= {i: 0 for i in range(256)}
	count = 0
	letter = file.read(1)
	while letter :
		count += 1
		dict[ord(letter)] += 1
		letter = file.read(1)
	for i in range(256):
		dict[i] = dict[i] / count
	file.close()
	return dict
	
def encode(list, filename, file_en = 'encoded_text.txt'):
	file = open(filename, 'r')	
	file1 = open(file_en, 'w')
	letter = file.read(1)
	while letter:
		file1.write(chr(list[ord(letter)]))
		letter = file.read(1)
	file1.close()
	file.close()
	
def decode(list, file_en = 'encoded_text.txt', file_dec = 'decoded_text.txt'):
	file1 = open(file_en, 'r')
	file2 = open(file_dec, 'w')
	letter = file1.read(1)
	while letter:
		file2.write(chr(list.index(ord(letter))))
		letter = file1.read(1)
	file1.close()
	file2.close()
	
def match(list_en, list_dec):
	listen = list(list_en.items())
	listen.sort(key = lambda i : i[1], reverse = True)
	listdec = list(list_dec.items())
	listdec.sort(key = lambda i : i[1], reverse = True)	
	key_match = {listen[i][0] : listdec[i][0] for i in  range(len(listen))}
	list_keys = list(key_match.items())
	list_keys.sort()
	keys = []
	for i in range(256):
		keys.append(int(list_keys[i][1]))
	key_to_file(keys, 'possible_key.json')
	return keys
	
def key_to_file(key, filename):
	file = open(filename, 'w')
	file.write(json.dumps(key))
	file.close()
		
def key_gen():
	key_list = [i for i in range(256)]
	random.shuffle(key_list)
	key_to_file(key_list, 'key.json')
	return key_list
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('mode', help = 'keygen/encode/decode/break')
	parser.add_argument('-p', '-possible')
	parser.add_argument('-c', '-count')
	args = parser.parse_args()
	if args.mode == 'keygen':
		key_list = key_gen()
		print("Key was generated in key.json")
	if args.mode == 'encode':
		key_list = key_gen()
		encode(key_list, 'original.txt')
		print("Encoded text is in encoded_text.txt")
	if args.mode == 'decode':
		key_list = key_gen()
		encode(key_list, 'original.txt')
		decode(key_list)
		print("Decoded text is in decoded_text.txt")
	if args.mode == 'break':	
		if args.p:
			file = open(args.p, 'r')
			count_p = json.loads(str(file.read()))
			file.close()
			count_dict = count('original.txt')
			key_poss = match(count_dict, count_p)
			decode(key_poss, file_dec = 'possible_decoded_text.txt')
			print("Possible key is in possible_key.json")			
		if args.c:
			count_dict = count(args.c)
			key_to_file(count_dict, 'frequency.json')
			print("Frequencies is in frequency.json")
