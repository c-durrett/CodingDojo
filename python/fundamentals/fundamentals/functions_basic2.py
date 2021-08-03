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
