"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""

x = 0
for num in range(0, 1000):
    if num % 3 == 0:
        x += num
    elif num % 5 == 0:
        x += num

print(x)

# another approach
target = 1000
sum = 0
for i in range(0, target):
    if (i % 3 == 0) or (i % 5 == 0):
        sum += i

print(sum)
