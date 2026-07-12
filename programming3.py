def find_factorial(n):
    if n < 0:
        raise ValueError("Number should not be negative")

    fact = 1
    i = 1

    while i <= n:
        fact *= i
        i += 1

    return fact

n = int(input("Enter number: "))
print(find_factorial(n))

# Output:
# Enter number: 5
# 120
