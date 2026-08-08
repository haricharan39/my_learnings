numbers = [1, 2, 3, 4, 5, 23334, 2342, 2233, 2837637829, 20398, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000]
# using a loop finds the largest number in the list
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print("The largest number in the list is:", largest)