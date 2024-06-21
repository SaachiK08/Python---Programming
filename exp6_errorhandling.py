#exceptional handling in python
print("\n Name : Saachi Kokate \n Batch : S13 \n Roll no : 50")
#system defined error

a = int(input("Enter the value of a : "))
b = input("Enter the value of b : ")
while(1) :
    ch = int(input("Enter your choice : "))
    if ch == 1 :
        try :
            add = a+b
        except TypeError :
            print("error! cannot add an int to str")
    if ch == 2 :
        zero = int(input("Enter a value 0 : "))
        try :
            div = a/zero
        except ZeroDivisionError :
            print("Divide by zero error! ")
    if ch == 3 :
        try :
            new = int(input("enter a value of your choice  : "))
        except ValueError :
            print("Exception : Value error")
    if ch == 4 :
        list = [1,2,3,4]
        c = int(input("Enter a value : "))
        try :
            print(list[a])
        except IndexError : 
            print("Exception : Index error")
    if ch == 5 :
        break;



#user defined exception

class Myexception(Exception):
    pass
num = int(input("Enter a number : "))
try :
    if num<10 :
        raise Myexception
except Myexception as exception :
    print("Num value is invalid!!")
else :
    print("The number is : ",num)


