# Find the largest palindrome made from the product of two 3-digit numbers.
# Answer: 906609

done = False
for i in reversed(range(1, 1000000)):
    n = str(i)
    if n[0] == n[len(n) - 1]:
        nLen = len(n)
        pal = True
        t = 1
        for t in range(int(nLen / 2)):
            if n[t] != n[nLen - t - 1]:
                pal = False
                break
        if pal is True:
            for j in reversed(range(100, 1000)):
                if i % j == 0:
                    a = str(int(i / j))
                    if len(a) == 3:
                        done = True
                        break
    if done is True:
        break
print(i)

# We achieve a quicker time by first looking for qualifying palindromes.  We know that the highest possible number of digits in the
# product is 6, so we begin by iterating downwards from 999999 looking for palindromes.  Once found, we see if it's the first we're 
# able to break up into two three-digit factors.  
# This ensures we find the largest palindrome that fits the bill in as fewest iterations as possible.

# Calculation time (on my PC): 62484 Microseconds
