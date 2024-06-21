#Python Program to Search the Number of Times a Particular Number Occurs in a List

print("\n Name : Saachi Kokate \n Batch : S13 \n Roll no. : 50\n")

def count_occurrences(numbers, target):
    count = numbers.count(target)
    return count

numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

target_number = int(input("Enter the number to search for: "))

occurrence_count = count_occurrences(numbers, target_number)

print(f"The number {target_number} occurs {occurrence_count} times in the list.")
