def is_prime(number):
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def primes_up_to(limit):
    return [number for number in range(2, limit + 1) if is_prime(number)]


if __name__ == "__main__":
    try:
        limit = int(input("Show prime numbers up to: "))
    except ValueError:
        print("Please enter a whole number.")
    else:
        primes = primes_up_to(limit)
        if primes:
            print("Prime numbers:", ", ".join(map(str, primes)))
        else:
            print("There are no prime numbers up to that limit.")
