# Python Program to Find the Sum of the Series: 1 + x^2/2 + x^3/3 + ... x^n/n


print("\n Name : Saachi Kokate \n Batch : S13 \n Roll no. : 50\n")
def sum_of_series(x, n):
    result = 0.0
    for i in range(1, n + 1):
        result += (x ** i) / i
    return result

x_value = float(input("Enter the value of x: "))
N = int(input("Enter the value of N: "))

result = sum_of_series(x_value, N)
print(f"The sum of the series 1 + x^2/2 + x^3/3 + ... + x^{N}/N is: {result}")
