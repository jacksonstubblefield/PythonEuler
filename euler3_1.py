# What is the largest prime factor of the number 600851475143 ?
# Answer: 6857

primes = [2]
z = 600851475143
i = 1
while i < z:
    if i > primes[len(primes)-1]:
        isPrime = True
        for p in primes:
            if i % p == 0:
                isPrime = False
        if isPrime == True:
            primes.append(i)
            if z % i == 0:
                z /= i
                i = 1
    else:
        for p in primes:
            if i == p:
                if z % i == 0:
                    z /= i
                    i = 1
    i += 1
print(z)

# The objective is to strip prime factors from z in order to find the largest irreducible factor of z as quickly as we can.
# The idea behind this is to teach the program how to identify and keep track of prime numbers as we iterate upwards.
# z is large and to keep it from taking too much time, we want to only deal with small iterations.
# Therefore the strategy is to strip away the lowest prime factors we're able to find until we're left with the largest prime factor -
# for which any i, it's unable to divide fully.
# We split it up into two forms to minimize time taken: whether we need to treat it as potential addition to our prime list or whether
# to identify whether or not i is already listed and whether it's able to be stripped from z.

# Calculation time (on my PC): 0.3124
