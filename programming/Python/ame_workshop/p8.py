print("this script adds natural numbers from 1 to n")
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print(f"Sum of first {n} natural numbers is: {sum}")