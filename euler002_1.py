# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# Answer: 4613732

x, y, z, s = [1, 2, 0, 2]
while z < 4000000:
    z = x + y
    x = y
    y = z
    if z % 2 == 0:
        s += z
print(s)

# Here we slide the values back one position each iteration of the While loop - saving the even values as we go.
# Ideally we wouldn't have to be so explicit with our redefinitions - if you can generalize this, get in touch.
