t = [
	[-1, 150, 190, 170, -1, -1, 160, 180],
	[-1, -1, -1, -1, -1],
	[4, 2, 9, 11, 2, 16]
]

def sortByHeight(a):
	# get trees and orig indexs
	trees = []
	[trees.append((i, a[i])) for i in range(len(a)) if a[i] == -1]
	# drop all trees and sort
	for i in reversed(trees):
		del a[i[0]]
	a = sorted(a)
	# put trees back
	[a.insert(i[0], i[1]) for i in trees]
	return a


def test():
	for a in t:
		sortByHeight(a)
	return


test()