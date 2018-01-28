x = 4

def invertPictureFrame(x):
	n = x
	m, c, t = [], [], []
	[m.append([i]) for i in range(1, x + 1)]

	for i in range(len(m)):
		for s in range(len(m[i])):
			for n in range(1, x):
				m[i].append(m[i][s - 1] + x)

	h, w = len(m), len(m[0])

	for x in range(h):
		for y in range(w):
			if x != 0 and x != h - 1:
				if y != 0 and y != w - 1:
					c.append((x, y))
	
	for i in c:
		t.append(m[i[0]][i[1]])

	t = sorted(t)
	for i in range(len(c)):
		m[c[i][0]][c[i][1]] = t[i]

	return m

invertPictureFrame(x)


