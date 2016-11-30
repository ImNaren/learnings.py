""" Given Two strings , write a method to decide if one is permutation of the other or not """


def ispermutation(str1, str2):
	str1 
	x = sorted(str1)
	y = sorted(str2)
	if len(x) != len(y):
		return False
	for i in range(len(x)):
		if x[i] != y[i]:
			return False
	return True


z = ispermutation('John', 'nohJ')

print z
