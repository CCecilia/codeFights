statues = [6, 2, 3, 8]
def makeArrayConsecutive2(statues):
		start = sorted(statues)[0]
		end = sorted(statues)[-1]
		new = list(range(start, end + 1))
		dif = (len(new))  - len(statues)
		return dif


makeArrayConsecutive2(statues)