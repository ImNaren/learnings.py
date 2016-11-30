""" Implemet an algorthm to find determine if a string has all unique chareters or not 
   you  cannot use additional data structures"""

def isstring_unique(str1):
	x = str1
	y = {}
	if len(x) > 128 :
		return False


	for i in range(len(x)):
   		if x[i] in y:
   			return False
   		else:
   			y[x[i]] = 1
   	return True

x = isstring_unique("shawshank redemption")
print x

