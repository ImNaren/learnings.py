""" string reversal"""


def string_reversal(str1):
	
	
	a = list(str1)
	str_len = len(a)
	for i in range(str_len/2):
		temp = a[i]
		a[i] = a[str_len-1-i]
		a[str_len-1-i] = temp

	b = ''.join(a)
	return b

str3 = string_reversal("naren")

print str3