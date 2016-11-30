""" Input = aabcccccaaa, 
	compress like  a2b1c5a3
	if original string lengh is less than compressed one return Original String:
	else return compressed string"""

def strcompression(str1):
	counter = 1
	list1 = []
	for i in range(len(str1)-1):
		if str1[i] == str1[i+1]:
			counter += 1

		else:
			list1.append(str1[i])
			list1.append(str(counter))
			counter = 1
	list1.append(str1[i+1])
	list1.append(str(counter))
	a = ''.join(list1)

	return a

Teststring = "aabcccccaaaz"
x = strcompression(Teststring)
if len(x) > len(Teststring):
	print Teststring
else:
	print x