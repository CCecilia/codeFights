yourLeft = 10 
yourRight = 15
friendsLeft = 15
friendsRight = 10

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
	y = [yourLeft, yourRight]
	f = [friendsLeft, friendsRight]

	if sum(y) == sum(f) and max(y) == max(f):
		return True

	return False