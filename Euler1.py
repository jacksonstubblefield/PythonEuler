# Find the sum of all the multiples of 3 or 5 below 1000.
# Answer: 233168

f = 0
for i in range(1000):
    if i % 3 == 0:
        f = f + i
    elif i % 5 == 0:
        f = f + i
print(f)

# In Python we practice brevity - no object identification, no hassle
# We count up from 0 to 1000 and chuck the int in the sum if it meets either of the following criteria:
# the integer divides 3 cleanly or the integer divides 5 cleanly
