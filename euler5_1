# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Answer: 232792560

sTime = datetime.datetime.now()
trueSet = [11, 12, 13, 14, 15, 16, 17, 18, 19]
k = math.factorial(20)
for i in range(20, k, 20):
    solved = True
    for x in trueSet:
        if i % x != 0:
            solved = False
            break
    if solved is True:
        break
 print(i)
 
 # Unfortunately here, the brute force takes time.  We may decrease the set we're looking at by recognizing that, for instance, any
 # number divisible by 18 will be divisible by 9.  We may also increase the step of the for loop to 20, which ensures that we do not need
 # to look at 20 in our trueSet either.
 
 # Computation Time: 0:00:04.590282
