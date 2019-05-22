# Find the first 10 digits of the sum of the following 100 50-digit numbers:
# (see numbers here: https://projecteuler.net/problem=13)
# Answer: 5537376230


# Here I wanted to build something robust - the site gives us uniformity but here we build for a sum of any possible numbers.

import sys

# truecount here will help us deal with the Python 'with open' file I'll use to import our numbers
def truecount(s):
    return len(s)-s.count('\n')

# We'll define some bases for what I'll call on later
numberFile = "solve13_numberfile.txt"
numberFileLines = 0
maxLen = 0
bigSumCarry = 0
numbersArray = []
numbersLenArray = []
finalSum = ''

# Reads our numbers
with open(numberFile) as f:
    numbers = f.readlines()

# Sends our numbers to internal memory for calculation, as well as gives us the largest number we'll be working with
for line in numbers:
    numberFileLines += 1
    numbersArray.append(line)
    if truecount(line) > maxLen:
        maxLen = truecount(line)
        
# These variables will give us the numbers we'll run with for our While loop
summingSize = len(str(sys.maxsize)) - len(str(9*numberFileLines))
summingRun = summingSize
summingRunL = 0

# This is the main function - it essentially teaches us how we deal with numbers in primary school
# We do addition in columns here - but we allow Python to use as many numbers as it possibly can
# For the problem we work with 7 columns at a time - and bigSum is the sum of those 7 columns
# We then teach it to carry the remainder on to the next 9 columns, and repeat until we have our finalSum
# We switch strings and integers here as we progress, so that we can make sure we only use the numbers we need
while (maxLen + summingSize) > summingRun:
    bigSum = int(bigSumCarry)
    for line in numbersArray:
        if truecount(line) >= summingRunL:
            endPosition = truecount(line)-summingRunL
            startPosition = endPosition - summingSize
            if startPosition < 0:
                startPosition = 0
            bigSum += int(line[startPosition:endPosition])
    bigSumLen = len(str(bigSum))
    bigSumCarry = str(bigSum)[:bigSumLen-summingSize]
    finalSum = str(bigSum)[len(bigSumCarry):] + finalSum
    summingRun += summingSize
    summingRunL += summingSize

print(finalSum)


