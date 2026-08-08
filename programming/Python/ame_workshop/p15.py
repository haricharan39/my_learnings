print("this scripts check weather the nth element of the string is a or not")
s = input("Enter a string: ")
n = int(input("Enter the position of the element to check: "))
if 1 <= n <= len(s) and s[n-1] == 'a':
    print(f"The {n}th element of the string is 'a'")
else:
    print(f"The {n}th element of the string is not 'a'")