#python program to display files available in the current directory
print("Name: Saachi Kokate \n Div: S13 \nRoll no. 50")


import os
files = os.listdir()
print("Files in the current directory are:")
for i in range(len(files)):
    print(files[i])
print("")
    
#for printing files from other directory
path="C:\\Users\\Saachi\\Documents\\SEM 4 SE\\PYTHON Lab"
files2 = os.listdir(path)
print("Files in the other directory are:")
for i in range(len(files2)):
    print(files2[i])
