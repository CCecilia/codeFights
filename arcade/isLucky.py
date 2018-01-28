numbers = [
	1230,
	239017,
	134008
]

def isLucky(n):
	n = list(str(n))
	n = [int(s) for s in n]
	i = int(len(n)/2)
	first = sum(n[i:])
	second = sum(n[:i])
	return first == second



def test():
	for n in numbers:
		isLucky(n)
	return


test()
