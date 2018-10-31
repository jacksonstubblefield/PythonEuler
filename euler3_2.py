# What is the largest prime factor of the number 600851475143 ?
# Answer: 6857

z = 600851475143
i = 2
k = 2
while i <= z / k:
    while z % i == 0:
        z /= i
        k = i
    i += 1
print(z)

# As opposed to euler3_1 (look at first) we don't keep track of primes here.  We assume that composites will be ignored;
# if a composite figure were to initially play some part in the dissemintation of z into its prime components, the components
# which make up the composite in question will have already played the part in place of their composite product.  As such, we
# loop through i as many times as it fits until we get z's largest prime component.

# Calculation time (on my PC): 0 Microseconds (!)
