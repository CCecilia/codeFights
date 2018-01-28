from collections import Counter
# message = "Uijt jt  sfbebcmf tusjoh jo Fohmjti!"
# message = "Jveu lezk B9 kf kyv ivri fw kyv tzkp, givgriv wfi srtblg."
message = "Arire tbaan tvir lbh hc, arire tbaan yrg lbh qbja, arire tbaan eha nebhaq naq qrfreg lbh."

def privateEyesOnly(message):
	most_common_letters = Counter(message.replace(' ', '')).most_common(1)
	print(most_common_letters)
	for i in range(len(most_common_letters)):
		most_common_letters[i] = most_common_letters[i][0]
	message = message.split()
	alphabet = []
	count = 1
	offset = None

	for letter in range(97, 123):
		alphabet.append((chr(letter), count))
		count += 1
	print(alphabet)
	def getNum(letter):
		return [index for index in alphabet if index[0] == letter.lower()][0][1]

	def getAl(number):
		# print(number)
		return [index for index in alphabet if index[1] == number][0][0]

	def decrypt(offset, message):
		message = list(' '.join(message))
		for i in range(len(message)):
			if message[i].isalnum():
				if not message[i].isdigit():
					num = getNum(message[i])
					num = num - offset
					if num < 0:
						num = 26 + num
					
					if message[i].istitle():
						message[i] = getAl(num).upper()
					else:
						message[i] = getAl(num)
		
		return ''.join(message)

	# temp = []
	# [temp.append((i, len(i))) for i in message]

	for i in message:
		if len(i) == 1:
			if i.istitle():
				num = getNum(i)
				offset = num - 9
				break
			else:
				num = getNum(i)
				offset = num - 1
				break
		elif len(i) == 2:
			if i[1] in most_common_letters:
				print('using o', i[1])
				num = getNum(i[1])
				offset = num - 15
				break
			elif i[0] in most_common_letters:
				print('using i', i[0])
				num = getNum(i[0])
				offset = num - 9
				break
		elif len(i) == 3:
			if i[1] in most_common_letters:
				print('using o', i[1])
				num = getNum(i[1])
				offset = num - 15
				break
			elif i[2] in most_common_letters:
				print('using e', i[2])
				num = getNum(i[2])
				offset = num - 5
				break
	
	
	print(decrypt(offset, message))

	return decrypt(offset, message)

	# print(Counter(message.replace(' ', '')).most_common())


# def privateEyesOnly(message):
# 	alphabet = []
# 	count = 1
# 	for letter in range(97, 123):
# 		alphabet.append((chr(letter), count))
# 		count += 1

# 	word = list(max(message.split(), key=len))
# 	# print(word)
# 	print(alphabet)

# 	for i in range(len(word)):
# 		word[i] = [index for index in alphabet if index[0] == word[i]][0][1]


# 	for y in range(26):
# 		# del temp[:]
# 		temp = map(lambda x: x + y, word)
# 		temp = [i for i in temp]
# 		# print(temp)
# 		for i in range(len(temp)):
# 			if temp[i] < len(alphabet):
# 				temp[i] = str([index for index in alphabet if index[1] == temp[i]][0][0])
# 			elif temp[i] - len(alphabet) != 0:
# 				temp[i] = temp[i] - len(alphabet)
# 				temp[i] = str([index for index in alphabet if index[1] == temp[i]][0][0])
# 			else:
# 				temp[i] = 'z'

# 		temp = ''.join(temp)
# 		print(y, temp)
# 	return




privateEyesOnly(message)
