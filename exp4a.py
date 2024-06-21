#python program to count number of line, words and characters in a file.
print("Name: Saachi Kokate \n Div: S13 \nRoll no. 50")

words = 0
lines = 0
characters = 0

with open("second.txt", 'r') as file:
    for l in file:
      words += len(l.split())
      lines += 1
      characters += len(l)
print("No of words: ", words)
print("No of lines: ", lines)
print("No of characters: ", characters)
