# 1. Countdown - Returns a list counting down from the number given.
def countdown(number):
    countdown = []
    while number >= 0:
        countdown.append(number)
        number = number-1
    return countdown
print(countdown(5))

# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def printAndReturn(list):
    print(list[0])
    return list[1]
print(printAndReturn([1,2]))

# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_plus_len(list):
    sum = list[0] + len(list)
    return sum
print(first_plus_len([1,2,3,4,5]))

# 4. Values Greater than Second
def vals_greaterthan_second(list):
    if len(list) < 2:
        return False
    output = []
    for num in range(len(list)):
        if list[num] > list[1]:
            output.append(list[num])
    print(len(output))
    return output
print(vals_greaterthan_second([5,2,3,2,1,4]))
print(vals_greaterthan_second([3]))

# 5. This Length, That Value - 
# Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def len_that_val(size, value):
    list = []
    for num in range(0, size):
        list.append(value)
    return list
print(len_that_val(4,7))
print(len_that_val(6,2))