# Project Euler - Problem 3: Largest Prime Factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143?
# Answer: 6857
#
# --- Notes ---
# - Key insight: you don't need a precomputed list of primes. Just iterate
#   through natural numbers starting at 2. Composite numbers (4, 6, 8, ...)
#   will never divide in because their prime factors have already been
#   divided out.
# - Bug to fix: only increment test when it DOESN'T divide q. Otherwise
#   repeated prime factors (e.g. 8 = 2*2*2) get missed and composites
#   like 4 sneak in as "largest prime."
# - Use // (integer division) instead of / (float division) in Python 3.


def solve():
    number = 600851475143
    q = number
    test = 2
    l_prime = 2
    while test <= q:
        if (q % test == 0):
            q = q//test
            l_prime = test
        else:
            test += 1

    return l_prime
    


if __name__ == '__main__':
    print(solve())
