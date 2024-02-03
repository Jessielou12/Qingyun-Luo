print("hello world!")

print(u"You can see this quote")

print(2 + 3)
print(3 < 5)

name = u"name=ABC" 
age = u"age=15"
print("name+age: ", name+age)

print("Say a number!")
number = 100
print("The number is %d" % number)
print("Tell me some somthing important!")
important_things = "I will go to the University"
print("Just say it : %s " % important_things)

first_name = 'Mike'
second_name = ' Jodan'
your_name = first_name + second_name
print("What your name %r ?" % your_name)
print(your_name)

tip = "Congratulation You get:"
money_type = '$'
money = 100
print(("%s %s%d\n" % (tip, money_type, money))*10,)
print("Now you have :", money_type, money*10)

formatter = "%s %s %s"
print(formatter % (u'Who', u'am', u'I'))

print()

print("\n \\  \a\a")

print("Before: ", your_name)
your_nme = raw_input("Input a new name.")
print("Now :", your_name)

# 12. Import module to receive
#from sys import argv
#script, frist_name, second_name= argv
#print script + frist_name+ second_name

# 13. Read the file
from sys import argv

script, file_name = argv
# This function is the output of the implementation file
def file_output(file_name):
    file_data = open(file_name)
    indata = file_data.read()
    print(indata)
  
# Function implementation: Go back to the beginning of the file
def rewind(file_object):
    file_object.seek(0)
    
# The function implements arbitrary output lines in the file  
def file_return(readline,file_object):
    rewind(file_object)
    print(readline, file_object.readline())
    
file_object = open(file_name, 'a+')   # Note here: Write mode cannot be read
# 14. Read and write files
file_object.write(your_name)
file_output(file_name)
line = 4  
file_return(line, file_object)
file_object.close()
# The idea here is that functions should only do one thing at a time
#print file_object.read()



