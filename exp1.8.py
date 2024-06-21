#Python Program to Compute the Value of Euler's Number e. Use the Formula: e = 1 + 1/1! + 1/2! + ...... 1/n!

print("\n Name : Saachi Kokate \n Batch : S13 \n Roll no. : 50\n")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def compute_euler_number(n):
    e = 1.0
    for i in range(1, n + 1):
        e += 1 / factorial(i)
    return e

n_value = 10
result = compute_euler_number(n_value)
print(f"The value of Euler's number (e) with n={n_value} is: {result}")
