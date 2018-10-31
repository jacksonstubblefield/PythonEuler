# Find the largest palindrome made from the product of two 3-digit numbers.
# Answer: 906609

t = 0
l = 0
for j in reversed(range(1, 1000)):
    for i in reversed(range(1, 1000)):
        pal = False
        n = str(i * j)
        if n[0] == n[len(n)-1]:
            nLen = len(n)
            pal = True
            for t in range(int(nLen / 2)):
                if n[t] != n[nLen - t - 1]:
                    pal = False
                    break
        if pal is True:
            if i * j > l:
                l = i * j
print(l)

# This is a brute force method of a problem which forces us to deal with large calculations.
# We try to break off the most time intensive comparison methods by locking it behind a check to see if the first digit is
# equivalent to the last digit, which should block off almost all of the uninteresting products.  Unfortunately, it's not enough to stop
# it from being over 500 milliseconds of computation.

# Calculation time (on my PC): 714250 Microseconds
