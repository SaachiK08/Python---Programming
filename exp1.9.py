#Python Program to Determine all Pythagorean Triplets in the Range

print("\n Name : Saachi Kokate \n Batch : S13 \n Roll no. : 50\n")

def find_pythagorean_triplets(start, end):
    triplets = []
    for a in range(start, end + 1):
        for b in range(a, end + 1):
            c = (a**2 + b**2)**0.5
            if c.is_integer() and c <= end:
                triplets.append((a, b, int(c)))
    return triplets


start_range = int(input("Enter the start range : "))
end_range = int(input("Enter the end range : "))

result = find_pythagorean_triplets(start_range, end_range)
print(f"Pythagorean Triplets in the range ({start_range}, {end_range}): {result}")
