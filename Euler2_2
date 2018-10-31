# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# Answer: 4613732

x, y, s = [1, 1, 0]
while x + y < 4000000:
    s += x + y
    x, y = x + 2 * y, 2* x + 3 * y
print (s)

# This requires one to note that an even is the sum of two odd numbers.  An odd plus an even must be odd.  Insinuating even numbers
# come along every third term.  This can be manipulated.
# The sequence goes as follows: x, y, x+y, x+2y, 2x+3y  ...  The last two terms are defined in terms of the first two terms.
# Thanks to PE user Begoner for the explanation of symmetry.
