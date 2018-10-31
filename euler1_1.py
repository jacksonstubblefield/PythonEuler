# Find the sum of all the multiples of 3 or 5 below 1000.
# Answer: 233168

f = 0
for i in range(1000):
    if i % 3 == 0:
        f =+ i
    elif i % 5 == 0:
        f =+ i
print(f)
