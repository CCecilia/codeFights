inputArrays = [
	[3, 6, -2, -5, 7, 3]
]

def adjacentElementsProduct(inputArray):
	products = []
	for i in range(len(inputArray)):
		next = i + 1
		if next < len(inputArray):
			num1 = inputArray[i]
			num2 = inputArray[next]
			products.append(num1 * num2)

	# products = []

	# for i in range(len(inputArray)):
	# 	for x in range(len(inputArray)):
	# 		if i != x:
	# 			products.append(inputArray[i]*inputArray[x])

	largest = max(products)
	print(largest)
	return largest


def test():
	for i in inputArrays:
		adjacentElementsProduct(i)
	print('test completed')
	return 

test()