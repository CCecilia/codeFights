a = [50, 60, 60, 45, 70]

def alternatingSums(a):
	t1 = [i for i in a[::2]]
	t2 = [i for i in a[1::2]]

	print(t1)
	print(t2)

	print([sum([i for i in a[::2]]), sum([i for i in a[1::2]])])


alternatingSums(a)
