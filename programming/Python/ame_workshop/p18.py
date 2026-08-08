#count even numbers in the list
numbers = input("Enter a list of numbers separated by spaces: ").split()
even_count = 0
for number in numbers:
    if int(number) % 2 == 0:
        even_count += 1
print("The count of even numbers in the list is:", even_count)