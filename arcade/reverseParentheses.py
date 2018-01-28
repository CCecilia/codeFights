import re
s = [
	# "a(bc)de",
	# 'co(de(fight)s)',
	'a(bcdefghijkl(mno)p)q',
	# "abc(cba)ab(bac)c"
]

def reverseParentheses(s):
	print(re.search(r'\((.*?)\)',s).group(0))

# def reverseParentheses(s):
# 	s = list(s)
# 	s_r = reversed(s)

# 	parentheses_indexes = zip(
# 		[i + 1 for i in range(len(s)) if s[i] == '('],
# 		reversed([i for i in range(len(s)) if s[i] == ')'])
# 	)

# 	for i in reversed(parentheses_indexes):
# 		s[i[0]:i[1]] = reversed(s[i[0]:i[1]])

# 	s = [i for i in s if i != '(' and i != ')']

# 	# print(''.join(s))
# 	return ''.join(s)


def test():
	for i in s:
		reverseParentheses(i)
	return

test()
