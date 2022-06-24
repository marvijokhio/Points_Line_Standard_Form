from xml.etree.ElementTree import Comment

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def myFunc(limit):
    sum = 0
    i = 1
    while i<=limit:
        if i%3==0 or i%5==0:
            sum=sum+i
        i+=1
    return sum

print(myFunc(1000))