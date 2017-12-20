"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

baseMultiple3 = 3
baseMultiple5 = 5
target = int(input("What is the target value? "))
countOf3 = target//baseMultiple3
countOf5 = target//baseMultiple5
addition=[]
sumFinal = 0

# Create the list of multiples of 3
for count in range(countOf3):
    count += 1
    addition.append(count*baseMultiple3)

# Create the list of multiples of 5
for count in range(countOf5):
    count += 1
    # Remove duplicated entries of 3*5
    Check15 = count*baseMultiple5
    if Check15%15 != 0:
        addition.append(Check15)

print(addition)

addition = [i for i in addition if i < target]
for i in addition:
    sumFinal+=i

print("The sum of multiples of %s and %s below %s is %s"%(baseMultiple3,baseMultiple5,target,sumFinal))