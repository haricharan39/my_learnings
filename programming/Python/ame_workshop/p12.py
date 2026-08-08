print("this script checks whether a number n is palindrome or not")
#inly for numbers with more than 1 digit
n = int(input("Enter a number: "))
rev = 0
temp = n
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig        # Reverse the number
    n = n // 10
if temp == rev:            # Check if the original number is equal to the reversed number
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")


#uses length of number and checks the digits from both ends of the number to see if they are equal. If they are not equal, then the number is not a palindrome. If all the digits are equal, then the number is a palindrome.
#this method is more efficient than the first method as it does not require reversing the number and comparing it with the original number. Instead, it only requires checking the digits from both ends of the number.
n1 = str(input("Enter a number: "))
if len(str(temp)) == 1:
    print("The number is a palindrome")
else:
    num_str = str(temp)
    is_palindrome = True
    for i in range(len(num_str) // 2):
        if num_str[i] != num_str[-(i + 1)]:
            is_palindrome = False
            break
    if is_palindrome:
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")