#.Python Program to Find the Sum of Sine and Cosine Series
print("\n Name : Saachi Kokate \n Batch : S13 \n Roll no. : 50\n")
def sum_of_series(n):
    result = 0
    for i in range(1, n + 1):
        result += 1/i
    return result


N = int(input("Enter the value of N: "))

result = sum_of_series(N)
print(f"The sum of the series 1 + 1/2 + 1/3 + ... + 1/{N} is: {result}")
