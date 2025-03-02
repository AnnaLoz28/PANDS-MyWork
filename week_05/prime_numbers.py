# generates primes

primes = []

for candidate in range (2,101):
    isPrime = True
    for divisor in range(2, candidate):
        # if divisable by an int it is not a prime
        if (candidate % divisor ==  0):
            isPrime = False
            break
    if isPrime:
        primes.append(candidate)

print(primes)


