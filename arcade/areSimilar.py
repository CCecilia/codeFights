a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b =  [832, 998, 148, 570, 533, 561, 455, 147, 894, 279]

def areSimilar(a, b):
	e1, e2 = [], []
	if str(a) == str(b):
		return True

	for i in range(len(a)):
		if a[i] != b[i]:
			e1.append(a[i])
			e2.append(b[i])
	e2 = reversed(e2)
	if len(e1) == 2 and str(e1) == str([i for i in e2]):
		return True

	return False

areSimilar(a, b)
