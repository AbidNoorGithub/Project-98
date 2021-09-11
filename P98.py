file1input = str(input("Which is file 1? "))

file2input = str(input("Which is file 2? "))

def swap():
	with open(file1input, "r" ) as f1:
		file1 = f1.read()
		f1.close()

	with open(file2input, "r" ) as f2:
		file2 = f2.read()
		f1.close()

	with open(file1input, "w" ) as f1:
		f1.write(file2)

	with open(file2input, "w" ) as f2:
		f2.write(file1)

swap()
