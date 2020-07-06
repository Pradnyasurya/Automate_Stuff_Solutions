
# The simplest impossible math problem


def collatz(n):
    if n % 2 == 0:
        n=n//2
        # print(n)
        return n

    elif n % 2 == 1:
        n = 3 * n + 1
        # print(n)
        return n

try:
    number = int(input("Enter the number :"))

    while number != 1:
        number = collatz(number)
        print(number)

except ValueError:
    print("Enter a valid number!")


# No matter what the number is, the answer will evantually be 1.
