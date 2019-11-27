print("Введите текст:")
text = input()
print("Введите целое число:")
key = int(input())
print("Зашифрованный текст:")
for char in text:
	if (char == ' '):
		print(' ', end="")
	else:
		print(chr((ord(char) - ord('a') + key) % 26 + ord('a')), end="")
print()
