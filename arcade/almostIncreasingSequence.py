sequences = [
	[1, 3, 2, 1],
	[10, 1, 2, 3, 4, 5],
	[1, 3, 2],
	# [1, 2, 1, 2],
	# [1, 4, 10, 4, 2],
	# [1, 1],
	# [10, 1, 2, 3, 4, 5, 6, 1],
	# [1, 2, 5, 3, 5]
]

def almostIncreasingSequence(sequence):
	decreases = 0
	for i in range(len(sequence)):
		print(i)
		# check beginning
		if i == 0:
			print(sequence[i], sequence[i + 1])
			if sequence[i] > sequence[i + 1]:
				decreases += 1
				print('decreased')
			else:
				print('increased')
		# check middle
		else:
			print(sequence[i], sequence[i - 1])
			if sequence[i] > sequence[i - 1]:
				decreases += 1
				print('decreased')
				if sequence[i] > sequence[i - 2] and sequence[i + 1]:
					print('decreased 2')
					return False
			else:
				print('increased')

	result = decreases <= 1
	print(sequence, result)
	return result

# def almostIncreasingSequence(sequence):
# 	decreases = 0
# 	for i in range(len(sequence)):
# 		if i != 0:
# 			print(sequence[i], sequence[i - 1])
# 			if sequence[i] < sequence[i - 1]:
# 				decreases += 1
# 				print('decreased', sequence[i], sequence[i - 1])
# 			else:
# 				print('increased', sequence[i], sequence[i - 1])
# 		else:
# 			print(sequence[i], sequence[i + 1])
# 			if sequence[i] < sequence[i + 1]:
# 				print('increased')
# 			else:
# 				decreases += 1
# 				print('decreased')
# 	result = decreases <= 1
# 	print(sequence, result)
# 	return result





# def almostIncreasingSequence(sequence):
# 	seq_len = len(sequence)
# 	skipped_used = False
# 	result = True
# 	for i in range(seq_len):
# 		if i + 1 < seq_len:
# 			if sequence[i] < sequence[i + 1]:
# 				continue
# 			elif sequence[i] > sequence[i + 1] and i == 0:
# 				skipped_used = True
# 				continue
# 			else:
# 				if i + 2 < seq_len:
# 					if sequence[i] < sequence[i + 2] and not skipped_used:
# 						skipped_used = True
# 						continue
# 					elif sequence[i - 1] < sequence[i + 2] and not skipped_used:
# 						skipped_used = True
# 						continue
# 					else:
# 						result = False


	# print(sequence, result)
	# return result

def test():
	for i in sequences:
		almostIncreasingSequence(i)
	print('test completed')
	return


test()
