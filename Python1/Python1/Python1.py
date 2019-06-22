with open('T.txt',mode = 'r') as myfile:# No need to close the file. the mode function allows us to limit what the program can do with the file, either 'r' for read or 'w' for write.op
	print(myfile.read())
	myfile.seek(0)
	print(myfile.read())
	myfile.seek(0)
	print()
	print(myfile.readline())
#myfile.close()

