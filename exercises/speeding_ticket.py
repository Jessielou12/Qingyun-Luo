"""
Write a Python function named speeding_ticket that evaluates whether a driver should receive a speeding ticket based on their driving speed and a special condition (their birthday).

The function should return one of three strings based on the driver's speed: "No Ticket", "Small Ticket", or "Big Ticket".
If the driver's speed is 60 mph or less, they should receive "No Ticket".
If the driver's speed is between 61 and 80 mph inclusive, they should receive a "Small Ticket".
If the driver's speed is 81 mph or more, they should receive a "Big Ticket".
On the driver's birthday, the speed limits for each ticket category are increased by 5 mph. For example, they can go up to 65 mph and still receive "No Ticket" if it is their birthday.
"""


def speeding_ticket(speed, is_birthday):
    # Your code goes here
    no_ticket_limit = 60
    small_ticket_limit = 80

    if is_birthday:
        no_ticket_limit += 5
        small_ticket_limit += 5

    if speed <= no_ticket_limit:
       print("No Ticket")
    elif speed <= small_ticket_limit:
        print("Small Ticket")
    else:
        print("Big Ticket")

# <! - - Adapted from Chatgpt - - >
def main():
    while True:
        speed_input = input("Enter the driver's speed: ")

        if not speed_input.isdigit() or int(speed_input) <= 0:
            print("Invalid input. Please enter a valid positive integer for speed.")
            continue

        speed = int(speed_input)

        birthday_input = input("Is it the driver's birthday? (yes/no): ").lower()
        is_birthday = birthday_input == "yes"

        result = speeding_ticket(speed, is_birthday)
        print(f"The result is: {result}")

        another_input = input("Do you want to check another speeding ticket? (yes/no): ").lower()

        if another_input != "yes":
            break

if __name__ == "__main__":
    main()


# Test cases
print(speeding_ticket(60, False))  # Expected output: "No Ticket"
print(speeding_ticket(75, False))  # Expected output: "Small Ticket"
print(speeding_ticket(85, False))  # Expected output: "Big Ticket"
print(speeding_ticket(65, True))  # Expected output: "No Ticket"
print(speeding_ticket(85, True))  # Expected output: "Small Ticket"
