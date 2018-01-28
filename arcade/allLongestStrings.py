from operator import itemgetter
inputArray = ["aba", "aa", "ad", "vcd", "aba"]

def allLongestStrings(inputArray):
	temp = []
	[temp.append((i, len(i))) for i in inputArray]
	max_len = max(temp, key=itemgetter(1))[1]
	[inputArray.remove(i[0]) for i in temp if i[1] != max_len]
	
	return inputArray

allLongestStrings(inputArray)