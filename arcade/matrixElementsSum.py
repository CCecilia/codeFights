# matrix = [
# 	[0, 1, 1, 2], 
# 	[0, 5, 0, 0], 
# 	[2, 0, 3, 3]
# ]

matrix = [
	[0,1,1,2],
	[0,5,0,0],
	[2,0,3,3]
]

def matrixElementsSum(matrix):
	coords = []
	height = len(matrix)
	width = len(matrix[0])
	total = 0

	# gen possible indexes
	for x in range(height):
		for y in range(width):
			coords.append((x, y))

	# remove unwanted coords
	for i in coords:
		x = i[1]
		y = i[0]
		value = matrix[y][x]

		# if zero found remove all along x-axis
		if value == 0:
			for pair in coords:
				if pair[1] == x:
					if pair[0] > y:
						coords.remove(pair)
						
	# iter remiaining cords for total
	for i in coords:
		x = i[1]
		y = i[0]
		value = matrix[y][x]
		total += value


	print(total)
	return total

matrixElementsSum(matrix)