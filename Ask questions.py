print("How old are you?",)
age = input()
print("How tall are you?",)
height = input()
print("How much do you weigh?",)
weight = input()
# Note that a comma is added after each line of print, so that print will not output a new line character and end the line and go to the next line.

print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))