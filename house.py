# class House, contains a name, and a string array of rooms
# contains method to enter the size of each room in ft
# contains method to print the size of each room in meters

class House:

	def __init__(self, extraRooms = None):
		self.rooms = ['kitchen', 'living', 'dining', 'main']
		self.name = "House"
		if extraRooms is not None:
			self.rooms = self.rooms + extraRooms

	def inputSqft(self):
		self.sizeft = []
		for x in range(0,len(self.rooms)):
			s = input(self.rooms[x] + " : width x length: ")
			l = s.split('x')
			self.sizeft.append(l)

	def printMetric(self):
		print(self.name)
		for x in range(0,len(self.sizeft)):
			l = "{0:.2f}".format(float(self.sizeft[x][0])/3.2808)
			w = "{0:.2f}".format(float(self.sizeft[x][1])/3.2808)  
			print("{} : {} x {} m".format(self.rooms[x], l, w))

# Testing:
# h1 = House()
# print(h1.rooms)
# h2 = House(['bedroom1', 'bedroom2'])
# print(h2.rooms)
# h2.inputSqft()
# h2.printMetric()


# class Semi is a subclass of House
class Semi(House):

	def __init__(self):
		House.__init__(self)
		self.name = "Semi"

# Testing:
# h3 = Semi()
# h3.inputSqft()
# h3.printMetric()