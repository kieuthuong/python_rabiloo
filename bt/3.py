def matrix(file):
	contents = open(file).read()
	return [item.split() for item in contents.split('\n')[:-1]]

print(matrix('myfile.txt'))