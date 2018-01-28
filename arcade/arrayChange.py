inputArray = [1, 1, 1]


def arrayChange(inputArray):
	count = 0
	for i in range(len(inputArray) - 1):
		# if i + 1 <= len(inputArray):
		if inputArray[i] >= inputArray[i + 1]:
			d = (inputArray[i] + 1) - inputArray[i + 1]
			count += d
			inputArray[i + 1] += d
	return count
	print(inputArray)

# def arrayChange(inputArray):
# 	count = 0
# 	for i in range(len(inputArray)):
# 		if i != len(inputArray) - 1:
# 			if inputArray[i] >= inputArray[i + 1]:
# 				print(range(inputArray[i], inputArray[i + 1] + 1))
# 				while inputArray[i] >= inputArray[i + 1]:
# 					inputArray[i + 1] += 1
# 					count += 1
# 		else:
# 			if inputArray[i] <= inputArray[i - 1]:
# 				print(range(inputArray[i - 1], inputArray[i] + 1))
# 				while inputArray[i] <= inputArray[i - 1]:
# 					inputArray[i] += 1
# 					count += 1
	return count


arrayChange(inputArray)