
""" replace the space in the string with %20"""

def string_spaces_replace(str1):
	strlist = []
	for i in range(len(str1)):
		if str1[i] == " ":
			strlist.append("%20")
		else:
			strlist.append(str1[i])

	FinalStr = ''.join(strlist)
	return FinalStr

x = string_spaces_replace("Mr John Smith")

print x


