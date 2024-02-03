Documentation for Customer Order Management System
1. System Overview
The Customer Order Management System streamlines order processing and customer management within an e-commerce framework. Key features include customer and product databases, order processing, and sales reporting.

2. Database Structure
•	Customers: {customer_id: {"name": str, "contact": str, "orders": list}}
•	Products: {product_id: {"name": str, "price": float, "stock": int}}

3. Function Descriptions
•	add_new_customer(customer_id, customer_info): Adds a new customer to the database.
•	add_product_to_order(customer_id, product_id, quantity): Adds a product to a customer's order.
•	update_customer_info(customer_id, updated_info): Updates customer's information.
•	remove_customer(customer_id): Removes a customer.
•	calculate_total_cost(customer_id): Calculates the total cost of a customer's order.
•	generate_sales_report(): Generates a sales report.

4. User Interface Guide
•	Text-based menu-driven interface.
•	Options for managing customers, processing orders, and viewing reports.

5. Development Notes
•	Python is used for its versatility and ease of use.
•	Dictionaries for data storage due to their efficiency in look-up operations.

Testing
Test Case 1: Add New Customer
•	Input: add_new_customer("001", {"name": "John Doe", "contact": "john@example.com", "orders": []})
•	Expected Output: "New customer added."
•	Result: Pass
Test Case 2: Add Product to Order
•	Precondition: Customer "001" and Product "A1" must exist.
•	Input: add_product_to_order("001", "A1", 2)
•	Expected Output: "Product added to order."
•	Result: Pass
Test Case 3: Calculate Total Cost
•	Precondition: Customer "001" has Product "A1" x 2 in order.
•	Input: calculate_total_cost("001")
•	Expected Output: Total cost based on product prices.
•	Result: Pass
Test Case 4: Generate Sales Report
•	Input: generate_sales_report()
•	Expected Output: Report displaying total sales and popular products.
•	Result: Pass
Each test case should be documented with the exact input, expected output, and test results. Testing should cover all functionalities and include edge cases to ensure robustness of the system.

