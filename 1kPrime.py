# Written by Sebastian Ikin, 16/19-2019
import math


# Our function, based on the "Sieve of Eratosthenes"
def print_primes(n):
    # The amount tells us how many primes we have.
    amount = 0
    current_number = 2
    # The upper bound is based on a variant of the pi(x) equation
    # (which gives us the highest prime within the range of x), in our case we have
    # tweaked the equation to give us the upper bound of an n amount of primes.
    # Source: https://primes.utm.edu/howmany.html
    # n (log n + log log n - 1) is the equation used, we also add a slight
    # constant at the end to make sure we have an equal or more amount of primes than we want.
    upper_bound = round(n*(math.log(n)+math.log(math.log(n))-1)) + round(n * 0.5)
    # An array of true boolean values representing our "sieve".
    sieve = [True for i in range(upper_bound+1)]

    # While the square of the current prime is lower than our upper bound
    # we "sieve" it based on whether or not it is a prime.
    while current_number * current_number <= upper_bound:
        if sieve[current_number]:
            for i in range(current_number * 2, upper_bound + 1, current_number):
                sieve[i] = False

        current_number += 1
    # Set the to remaining numbers to their corresponding "sieve-value".
    sieve[0] = False
    sieve[1] = True

    # Print our primes until we have passed our n, the reason we count our primes
    # is because we don't know how accurate our approximation of the upper bound was.
    for prime in range(upper_bound+1):
        if amount >= n:
            return
        if sieve[prime]:
            amount += 1
            print("Prime: {}, Nr: {}".format(prime, amount))


print_primes(1000)
