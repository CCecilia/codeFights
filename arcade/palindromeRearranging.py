inputString = [
	"aabb", #pass
	"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc", #fail
	"aazah", #pass
	"zyyzzzzz" #pass
]


def palindromeRearranging(inputString):
	a = sorted(list(inputString))
	s1, s2 = [i for i in a[::2]], [i for i in a[1::2]]
	

	if len(inputString) % 2 == 0:
		check = zip(s1, s2)
		for i in check:
			if i[0] != i[1]:
				return False
	else:
		for i in s2:
			if i not in s1:
				return False

	return True

	
for i in inputString:
	palindromeRearranging(i)
