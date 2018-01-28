shapes = [
	1,
	2,
	3,
	4,
	5
]



def shapeArea(n):
	if n == 1:
		return n
	else:
		row = n * n
		alt_row = (n - 1) * (n - 1)

	return row + alt_row
	
	

def test():
	for i in shapes:
		shapeArea(i)
	print('test completed')
	return 

test()