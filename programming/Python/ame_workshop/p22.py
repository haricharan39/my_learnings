#sorting a list of numbers in ascending order
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print("The sorted list in ascending order is:", sorted_numbers)

#without using the sorted() function
numbers = [5, 2, 9, 1, 5, 6]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print("The sorted list in ascending order without using sorted() is:", numbers)