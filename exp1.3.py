# Python Program to print following patterns with cases
# a)
height = int(input("Enter the height of the pyramid : "))
print("\n Name : Saachi Kokate \n Batch : S13 \n Roll no. : 50\n")
for i in range(1, height + 1):
    print(' ' * (height - i) + '1 ' * i)
print(" ")

# Python Program to print following patterns with cases
# b)
pattern=int(input("Enter a number : "))
print("\n Name : Saachi Kokate \n Batch : S13 \n Roll no. : 50\n")
for j in range(1,pattern+1):
    for k in range(1,j+1):
        print(k,end='')
    print(" ")

# Python Program to print following patterns with cases
# c)
pattern = int(input("\nEnter a number : "))
print("\n Name : Saachi Kokate \n Batch : S13 \n Roll no. : 50\n")
for j in range(1,pattern+1,1):
    for k in range(1,pattern+1,1):
        print("1",end='')
    print("")

# Python Program to print following patterns with cases
# d)
pattern=int(input("\nEnter a number : "))
print("\n Name : Saachi Kokate \n Batch : S13 \n Roll no. : 50\n")
for j in range(1,pattern + 1):
    for k in range(1,pattern + 1):
        print(k,end='')
    print("")
