strings = [
	["aabcc", "adcaa"],
	["abca", "xyzbac"],
	["assssbs", "aasaaaa"],
	["zzzzzz", "zzz"],
	["abcdefghxyzttw", "hgfedcbaabcwwt"] #<-- the list failing with one iteration
]


def commonCharacterCount(s1, s2):
	s1, s2 = sorted(list(s1)), sorted(list(s2))
	matchs=[i for i in s1 if i in s2]
	# matches = []
	
	# def matched(i):
	# 	matches.append(i)
	# 	s1.remove(i)
	# 	s2.remove(i)

	# [matched(i) for i in s1 if i in s2]
	# [matched(i) for i in s2 if i in s1]
	# [matched(i) for i in s1 if i in s2] #<-- Second for loop to find f

	print(matchs)
	return len(matchs)


def test():
	for i in strings:
		commonCharacterCount(i[0], i[1])
	return


test()
