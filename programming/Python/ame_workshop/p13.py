print("this scripts check wheather n is prime or not")
n = int(input("Enter a number: "))
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print("The number is a prime")
else:
    print("The number is not a prime")