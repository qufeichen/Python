# multi-part program that manipulates cubes/cube roots

 # calculates the power of 3 and the remainder such that b=(x^3)+r
def cubeless(x, b):
	return (b - (x**3));

# test print(cubeless(2,10))


# finds all numbers with a cube smaller that the given limit
def smallerCube(b):
	x = 1
	r = x**3
	lst = []

	while (r < b):
		r = cubeless(x,b)
		entry = [x,r]
		lst.append(entry)
		x = x + 1
		r = x**3
	return lst

#test
# print(smallerCube (130))


# adds up all the remainders from finding all the cubes up to an upper limit
def restSum(s):
	e = [entry[1] for entry in s]
	return sum(e)

# test
# print( restSum(smallerCube(130)) )


# print all rest sums that are multiples of 3 within a range
def showAllRestSum(minNum,maxNum):
	# if restSum(smallerCube(n)) is multiple of 3
	# add [n, restSum(smallerCube(n))] to list
	lst = []
	for n in range(1,21):
		if (restSum(smallerCube(n)) % 3) == 0:
			elem = [n,restSum(smallerCube(n))]
			lst.append(elem)
	return lst

#test
# print(showAllRestSum(1,20))
