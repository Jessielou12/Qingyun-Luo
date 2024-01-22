from sys import argv

script, first, second, third = argv

additional_input = input("Enter additional input: ")

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Additional input is:", additional_input)

#I didn't run this one correctly, I see that's what it says in the book. I modified it with Chatgpt and it is：
#
script = input("Enter the script name: ")
first = input("Enter your first variable: ")
second = input("Enter your second variable: ")
third = input("Enter your third variable: ")

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
#