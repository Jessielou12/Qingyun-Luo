"""
Project 3: Product Sales Analysis System
You must develop a Product Sales Analysis System using Python to analyse and report product sales within an e-commerce business. The primary objectives include creating and maintaining a product database, tracking sales transactions, and generating insightful reports. The system should allow users to record sales, capture customer feedback, analyse product performance, and facilitate the extraction of valuable insights such as total revenue, best- selling products, and average product ratings to aid businesses in making informed decisions.
For this purpose, the system must contain the following key features:
1. Key features:
• Product Database: Implement a product database using dictionaries to store information such as product name, price, and sales history.
• Functionality: Create functions to perform operations, including: o Sales Tracking Functions:
▪ Recording sales transactions, i.e., the number of product sales. ▪ Calculating total sales for each product.
▪ Identifying the best-selling product.
o CustomerManagementFunctions:
▪ Recording customer feedback or ratings for products. ▪ Displaying product average rating.
• Sales Reporting System: Create a reporting system that provides insights into product sales, including total sales revenue, best-selling products, and product sales history.
2. Minimum requirements:
• Python Functions: the project must rely on the use of functions to modularise code and enhance reusability.
• Dictionaries: utilise dictionaries as the primary data structure for representing the product database and storing sales and customer feedback information.
• User Interface: create a simple text-based user interface to interact with the system. This includes recording sales transactions, managing customer interactions, and accessing sales reports.
• Error Handling: implement error-handling mechanisms to deal with invalid inputs. For example, recording sales for non-existent products, displaying ratings for products without feedback, etc.
"""


# Adapted from Chatgpt
# Product Database
products = {
    "ProductA": {"price": 10.0, "sales": 0, "feedback": []},
    "ProductB": {"price": 15.0, "sales": 0, "feedback": []},
    # Additional products...
}

# Sales Tracking Functions
def record_sale(product, quantity):
    if product in products:
        products[product]["sales"] += quantity
    else:
        print("Product not found.")

def calculate_total_sales():
    return sum(product["price"] * product["sales"] for product in products.values())

def best_selling_product():
    return max(products, key=lambda x: products[x]["sales"])

# Customer Management Functions
def record_feedback(product, rating):
    if product in products and 0 <= rating <= 5:
        products[product]["feedback"].append(rating)
    else:
        print("Invalid product or rating.")

def average_rating(product):
    if product in products and products[product]["feedback"]:
        return sum(products[product]["feedback"]) / len(products[product]["feedback"])
    else:
        return "No feedback available."

# Sales Reporting System (Example)
def generate_report():
    print(f"Total Sales Revenue: {calculate_total_sales()}")
    print(f"Best Selling Product: {best_selling_product()}")
    # Additional reporting features...

# User Interface (Example)
def main_menu():
    while True:
        print("\n1. Record Sale\n2. Record Feedback\n3. Sales Report\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Record sale
            pass
        elif choice == '2':
            # Record feedback
            pass
        elif choice == '3':
            # Generate sales report
            pass
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

main_menu()

