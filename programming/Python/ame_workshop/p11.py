print("this script does counting of digits in a number n")
n = int(input("Enter a number: "))
count = 0
while n > 0:
    n = n // 10
    count += 1
print("The number of digits is:", count)