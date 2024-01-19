def case_counter(text):
    # Your code goes here
    uppercase_count = 0
    lowercase_count = 0

    for i in text:
        if i.isalpha():
            if i.isupper():
                uppercase_count += 1
            elif i.islower():
                lowercase_count += 1
        
print("uppercase_count","lowercase_count")

# Test cases
print(case_counter("Hello World!"))  # Expected: (2, 8)
print(case_counter("PYTHON"))  # Expected: (6, 0)
print(case_counter("python"))  # Expected: (0, 6)
print(case_counter("1234!@#$"))  # Expected: (0, 0)

# Sorry, I can't solve this problem. T_T