from math import log, ceil

def sieve_n_primes(n):
    if n < 6:
        upper = 15
    else:
        upper = ceil(n * (log(n) + log(log(n))))

    sieve = [True] * (upper + 1)
    sieve[0:2] = [False, False]

    for i in range(2, int(upper ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i:upper+1:i] = [False] * len(range(i*i, upper+1, i))

    primes = [i for i, is_p in enumerate(sieve) if is_p]
    return primes[:n]

# Ask user for input
try:
    n = int(input("Enter the value of n to find the nth prime number: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        nth_prime = sieve_n_primes(n)[-1]
        print(f"The {n}th prime number is: {nth_prime}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
