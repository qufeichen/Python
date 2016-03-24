# program that prints out a table with integers from decimal 0 to 255, it's hex number, and the character corresponding to the unicode with UTF-8 encoding

# using a loop
for x in range(0, 256):
	print('{0:d} {0:#04x} {0:c}'.format(x))

# using list comprehension
ll = [('{0:d} {0:#04x} {0:c}'.format(x)) for x in range(0, 256)]
print( "\n".join(ll) )
