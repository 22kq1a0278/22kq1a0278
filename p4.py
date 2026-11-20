def check_prime(n):
    if n <= 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True
num = int(input("Enter a number: "))
if check_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")