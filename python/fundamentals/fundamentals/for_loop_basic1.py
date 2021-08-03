# 1. Basic - Print all integers from 0 to 150
for num in range(0,151):
    print(num)

# 2. Multiples of Five - print 5 to 1,000 by 5s
for num in range(5, 1000, 5):
    print(num)

# 3. Counting, the Dojo Way - 
for num in range(1, 100):
    if num % 10 == 0:
        print("Coding Dojo.")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

# 4. Whoa. That Sucker's Huge -Add odd integers from 0 to 500,000, and print the final sum.
sum = 0 
for num in range(0, 500000):
    if num % 2 != 0:
        sum += num
    else:
        continue
print(sum)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for num in range(2018, 0, -4):
    print(num)

# 6. Flexible Counter -
lowNum = 2
highNum = 9
mult = 3
for num in range(lowNum, highNum+1):
    if num % mult == 0:
        print(num)