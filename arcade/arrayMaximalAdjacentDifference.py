inputArray = [2, 4, 5, 1]

def arrayMaximalAdjacentDifference(inputArray):
	difs = []

	def checkNeighborDif(value, index):
		if index + 1 < len(inputArray):
			x = value - inputArray[index + 1]
			if x < 0:
				x *= -1
			difs.append(x)


	[checkNeighborDif(inputArray[i], i) for i in range(len(inputArray))]
	# print( max(difs) )
	return max(difs)

arrayMaximalAdjacentDifference(inputArray)