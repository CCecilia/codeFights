inputStrings = [
	'aabaa',
	'david',
	'bab',
	'zzzzoooopqqqqpoooozzzz'
	'test'
]

def checkPalindrome(inputString):
	rev = ''.join(reversed(list(inputString)))
	print(inputString, rev)
	if inputString == rev:
		print('matched')
	else:
		print('No')	
	return



def test():
	for i in inputStrings:
		checkPalindrome(i)
	print('test completed')
	return 

test()