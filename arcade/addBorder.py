picture = [
	"abc",
    "ded"
]


def addBorder(picture):
	s = ''	
	for i in range(len(picture)):
		picture[i] = '*{}*'.format(picture[i])

	for i in range(len(picture[0])):
		s += '*'
		
	picture.insert(0, s)
	picture.append(s)
	return picture


addBorder(picture)
