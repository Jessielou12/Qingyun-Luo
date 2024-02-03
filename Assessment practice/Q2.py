"""Project 2: Customer Order Management System
You must develop a Customer Order Management System using Python to streamline and automate customer order processes within an e-commerce framework. The key objectives involve creating a robust customer and product database, implementing order processing functions, and establishing a user-friendly interface. The system allows users to add products to orders, calculate total order costs, and display order histories. This system allows businesses to efficiently manage customer orders, track product sales, and gain insights into customer purchasing behavior.
For this purpose, the system must contain the following:
1.Key features:
Customer Database: Implement a customer database using dictionaries to store information such as customer name, contact details, and order history.
Product Database: Create a product database to store information about available products provided by the user. Each product should include details like name, price, and quantity in stock.
Functionality: Create functions to perform operations, including:
order Processing Functions: Adding products to a customer's order history.Calculating the total cost of an order. Updating product quantities after an order is placed.
Customer Management Functions: Adding new customers to the database and updating their data, suchas contact details.Displaying customer details and order history.▪Removing customers from the database.
Reporting System: Create a reporting system that provides insights into the business, including the total sales, the most popular products, and the customer order history.

2.Minimum requirements:
·Python Functions: the project must rely on the use of functions to modularise code
and enhance reusability.
Dictionaries: utilise dictionaries as the primary data structure for representing the customer and product database.
User Interface: Develop a simple text-based user interface that allows users to interact with the system. This includes adding products to orders, processing orders, managing customers, and accessing reports.
Error Handling: Implement error handling mechanisms to handle cases such as ordering out-of-stock products, updating quantities beyond available stock, or accessing information for non-existent customers.
"""
# Adapted from Chatgpt
# Customer Database
customers = {
    # Each customer is represented by a unique customer_id
    'customer_id1': {
        'name': 'John Doe',
        'contact': 'johndoe@example.com',
        'orders': []  # This will be a list of order dictionaries
    },
    # ... additional customers
}

# Product Database
products = {
    # Each product is represented by a unique product_id
    'product_id1': {
        'name': 'Widget',
        'price': 19.99,
        'stock': 100  # Current inventory level
    },
    # ... additional products
}

# Function to add product to a customer's order
def add_product_to_order(customer_id, product_id, quantity):
    if customer_id not in customers:
        return "Customer not found."
    if product_id not in products:
        return "Product not found."
    if quantity > products[product_id]['stock']:
        return "Insufficient stock."
    
    # Update the product stock
    products[product_id]['stock'] -= quantity
    
    # Update customer's order history
    order = {'product_id': product_id, 'quantity': quantity}
    customers[customer_id]['orders'].append(order)
    return "Product added to order."

# Function to calculate the total cost of a customer's order
def calculate_total_cost(customer_id):
    if customer_id not in customers:
        return "Customer not found."
    
    total_cost = 0
    for order in customers[customer_id]['orders']:
        product_id = order['product_id']
        quantity = order['quantity']
        total_cost += products[product_id]['price'] * quantity
    return total_cost

# Function to update product quantity after an order is placed
def update_product_quantity(product_id, sold_quantity):
    if product_id not in products:
        return "Product not found."
    if sold_quantity > products[product_id]['stock']:
        return "Insufficient stock to update."
    
    products[product_id]['stock'] -= sold_quantity
    return "Product stock updated."

# Function to add a new customer to the database
def add_new_customer(customer_id, customer_info):
    if customer_id in customers:
        return "Customer already exists."
    customers[customer_id] = customer_info
    return "New customer added."

# Function to update an existing customer's information
def update_customer_info(customer_id, updated_info):
    if customer_id not in customers:
        return "Customer not found."
    customers[customer_id].update(updated_info)
    return "Customer information updated."

# Function to display a customer's details and order history
def display_customer_details(customer_id):
    if customer_id not in customers:
        return "Customer not found."
    customer = customers[customer_id]
    print(f"Customer Name: {customer['name']}")
    print(f"Contact Details: {customer['contact']}")
    print("Order History:")
    for order in customer['orders']:
        print(order)

# Function to remove a customer from the database
def remove_customer(customer_id):
    if customer_id not in customers:
        return "Customer not found."
    del customers[customer_id]
    return "Customer removed."

# Function to calculate total sales revenue
def calculate_total_sales():
    total_sales = 0
    for product_id, product_info in products.items():
        # Multiply the product price by the number of units sold
        total_sales += product_info['price'] * (product_info['initial_stock'] - product_info['stock'])
    return total_sales

# Function to determine the most popular products
def get_most_popular_products():
    # Sort products by the number of units sold, in descending order
    sorted_products = sorted(products.items(), key=lambda item: item[1]['initial_stock'] - item[1]['stock'], reverse=True)
    # Return the sorted list or just the top product(s)
    return sorted_products

# Function to print the customer order history
def print_customer_order_history(customer_id):
    if customer_id not in customers:
        return "Customer not found."
    
    print(f"Order history for {customers[customer_id]['name']}:")
    for order in customers[customer_id]['orders']:
        product = products[order['product_id']]
        print(f"{product['name']}: {order['quantity']} unit(s)")

# Function to generate and print the overall sales report
def generate_sales_report():
    print(f"Total Sales Revenue: ${calculate_total_sales():.2f}")
    print("Most Popular Products:")
    for product_id, product_info in get_most_popular_products():
        print(f"{product_info['name']} - Units Sold: {product_info['initial_stock'] - product_info['stock']}")

# Assume we add an 'initial_stock' key to each product to keep track of the original stock level.

def user_interface():
    while True:
        # Display the main menu options
        print("\nMain Menu:")
        print("1 - Add a New Customer")
        print("2 - Add a Product to Order")
        print("3 - Update Customer Information")
        print("4 - Remove Customer")
        print("5 - Display Customer Details")
        print("6 - Generate Sales Report")
        print("7 - Exit")

        # Get user's choice
        choice = input("Please select an option: ")

        # Execute the chosen functionality
        if choice == '1':
            customer_id = input("Enter customer ID: ")
            name = input("Enter customer name: ")
            contact = input("Enter contact details: ")
            add_new_customer(customer_id, {'name': name, 'contact': contact, 'orders': []})
        elif choice == '2':
            customer_id = input("Enter customer ID: ")
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity: "))
            add_product_to_order(customer_id, product_id, quantity)
        elif choice == '3':
            customer_id = input("Enter customer ID: ")
            name = input("Enter new name (or leave blank to keep current): ")
            contact = input("Enter new contact details (or leave blank to keep current): ")
            update_customer_info(customer_id, {'name': name, 'contact': contact})
        elif choice == '4':
            customer_id = input("Enter customer ID to remove: ")
            remove_customer(customer_id)
        elif choice == '5':
            customer_id = input("Enter customer ID to display details: ")
            display_customer_details(customer_id)
        elif choice == '6':
            generate_sales_report()
        elif choice == '7':
            break
        else:
            print("Invalid option. Please try again.")

# Run the user interface
user_interface()

# Example of adding error handling to the add_new_customer function
def add_new_customer(customer_id, customer_info):
    try:
        # Check if the customer_id is already in use
        if customer_id in customers:
            raise ValueError("A customer with this ID already exists.")
        # Validate that customer_info contains all necessary keys
        if not all(key in customer_info for key in ['name', 'contact', 'orders']):
            raise ValueError("Customer information is incomplete.")
        # Add the new customer to the database
        customers[customer_id] = customer_info
        print("New customer added successfully.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # You might load existing data from a file or a database here
    # For now, let's assume we're starting with empty databases
    global customers
    global products
    customers = {}
    products = {}

    # Initialize the user interface loop
    user_interface()

    # Before exiting, you might save data back to a file or database
    # This is where you'd typically perform any cleanup operations as well

if __name__ == "__main__":
    main()