# inputArray = [5, 3, 6, 7, 9]
inputArray = [2, 3]

# def avoidObstacles(inputArray):
# 	temp = [i for i in range(1, max(inputArray)+2)]
# 	count = 0
		
# 	for i in range(len(temp)):
# 		if temp[i] in inputArray:
# 			temp[i] = 'x'
	
# 	for i in range(len(temp)):
# 		if i + 1 < len(temp):
# 			if temp[i + 1] == 'x' and temp[i] != 'x':
# 				count += 1
# 	print(temp)
# 	print(count)
# avoidObstacles(inputArray)


def avoidObstacles(inputArray):
	inputArray = sorted(inputArray)
	for jump in range(2, inputArray[-1] + 2): 
		jumpPoint = 0
		while jumpPoint <= inputArray[-1]:
			isPassAll = True
			jumpPoint += jump
			if jumpPoint in inputArray:
				isPassAll = False
				break

			if isPassAll:
				return jump
	return False


avoidObstacles(inputArray)
