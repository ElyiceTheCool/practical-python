# bounce.py
#
# Exercise 1.5

height = 100
counter = 1

while counter <= 10:
    height = round((height * (3/5)), 4)
    print(counter, height)

    counter += 1