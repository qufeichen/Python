# program that reads an input file with list of cars with imperial units of measurment
# and generates a new output file with the same cars but with the information in metric units of meausurement

# i.e. if input file contains:
# 2007, Chevrolet, Impala, 22 mpg, 19 ft^3
# the output file will becomes:
# 2007, Chevrolet, Impala, 10.7 litre/100 km, 0.538 m^3

# test file with data: car_imperial.txt 

fi = open('car_imperial.txt', 'r')

fm = open('car_metric.txt','w')

for l in range(0,4):
	content = fi.readline()
	lst = content.split(',')

	newLst = [lst[0], lst[1], lst[2]]

	# get mpg and convert to litre/100km
	speed = lst[3].split()
	newSpeed = "{0:.1f}".format((100*3.785411784)/(int(speed[0])*1.609344))
	newLst.append(' ' + str(newSpeed) + ' litre/100km')

	# get ft^3 and convert to m^3
	ft = lst[4].split()
	m = "{0:.3f}".format(int(ft[0])/35.315)
	newLst.append(' ' + str(m) + ' m^3')

	newStr = ','.join(newLst)

	fm.write(newStr)
	fm.write("\n")

fi.close()
fm.close()