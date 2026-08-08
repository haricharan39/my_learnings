#takes an input string and checks total number of vowels in the string
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in s:
    if char in vowels:
        count += 1
print("The total number of vowels in the string is:", count)