def count_digits(number):
    """Return how many digits the number has."""
    return len(str(number))


def disarium_sum(number):
    """Return the sum of each digit raised to the power of its position."""
    total = 0
    position = 1
    for digit in str(number):
        total += int(digit) ** position
        position += 1
    return total


def is_disarium(number):
    """Return True if the number is a Disarium number, otherwise False."""
    return disarium_sum(number) == number


def main():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid whole number.")
        return

    if num < 0:
        print("Please enter a positive number.")
        return

    if is_disarium(num):
        print(f"{num} is a Disarium number.")
    else:
        print(f"{num} is not a Disarium number.")


main()