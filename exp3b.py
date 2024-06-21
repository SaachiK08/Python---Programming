#program to implement tell, seek, read, readline, readlines
print("Name: Saachi Kokate \n Div: S13 \nRoll no. 50")

file = open("second.txt", "r")
data = file.read()
print(data)
file.close()

#read(n): to read n bytes from a file
file1 = open("second.txt", "r")
data1 = file1.read(10)
print("read(10):\n", data1)
file1.close()

#readlines(): to read all lines from a file
file2 = open("second.txt", "r")
data2 = file2.readlines()
print("readlines():")
for i in range(len(data2)):
    print(data2[i])   
print("\n")
file2.close()

#readline(n):  Reads a line of the file and returns in form of a string.For specified n, reads at most n bytes.
file3 = open("second.txt", "r")
data3 = file3.readline(5)
print("readline(5):\n", data3)
print("\n")
file3.close()

#tell(): returns the current file position in a file stream.
file4 = open("second.txt", "r")
print("tell():", file4.tell())
print("\n")
file4.close()

#seek():  to change the position of the File Handle to a given specific position. 
file5 = open("second.txt", "r")
file5.seek(0)
print("seek():", file5.tell())
print("\n")
file5.close()

