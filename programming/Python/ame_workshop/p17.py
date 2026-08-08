#find the smallest number in the list
numbers = [1, 2, 3, 4, 5, 23334, 2342, 2233, 2837637829, 20398]
smallest = numbers[0]
if len(numbers) == 0:
    print("The list is empty.")
else:
    for number in numbers:
        if number < smallest:
            smallest = number
    print("The smallest number in the list is:", smallest)