
years = [
	102,
	200,
	1985,
	1776,
	464,
	500,
	1664,
	10,
	1700
]

def centuryFromYear(year):
	if year < 100:
		century = 1
	elif year < 1000 and year % 100 == 0:
		century = int(str(year)[0])
	elif year < 1000 and year % 100 != 0:
		century = int(str(year)[0]) + 1
	elif year > 1000 and year % 100 == 0:
		century = int(str(year)[:2])
	else:
		century = int(str(year)[:2]) + 1
	return century


def test():
	for i in years:
		centuryFromYear(i)
	print('test completed')
	return 

test()
