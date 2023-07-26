# bounce.py
#
# Exercise 1.5

# Dropped from 100 m
# Each bounce is 3/5 of the height it fell
height = 100
counter = 1

while counter <= 10:
    height = height * (3/5)
    print(counter, height)

    counter += 1