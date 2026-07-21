# Grocery Billing System

# Product Catalog
products = {
    "Rice": 60,
    "Sugar": 45,
    "Milk": 30,
    "Bread": 40,
    "Oil": 150,
    "Eggs": 7,
    "Soap": 35,
    "Tea": 120,
    "Coffee": 180,
    "Salt": 20
}

# Empty Cart
cart = {}

# Display Available Products

def display_products():
    print("\n------ PRODUCT LIST ------")

    for item, price in products.items():
        print(f"{item:10} : ₹{price}")

# Add Item into Cart

def add_to_cart():

    display_products()

    item = input("\nEnter product name: ").title()

    if item not in products:
        print("Product not available.")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity should be greater than zero.")
            return

        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity

        print("Item added successfully!")

    except ValueError:
        print("Invalid quantity.")

# Remove Item

def remove_item():

    if not cart:
        print("Cart is empty.")
        return

    show_cart()

    item = input("Enter product to remove: ").title()

    if item in cart:
        del cart[item]
        print("Item removed.")
    else:
        print("Item not found.")

# Display Cart

def show_cart():

    if not cart:
        print("\nCart is Empty.")
        return

    print("\n------ YOUR CART ------")

    total = 0

    for item, qty in cart.items():

        price = products[item]
        amount = qty * price

        total += amount

        print(
            f"{item:10} Qty:{qty:<3} Price:₹{price:<4} Total:₹{amount}"
        )

    print("-------------------------")
    print("Subtotal :", total)

# Calculate Discount

def calculate_discount(total):

    if total > 1000:
        return total * 0.10

    elif total > 500:
        return total * 0.05

    else:
        return 0

# Save Bill

def save_bill(text):

    with open("purchase_history.txt", "a", encoding="utf-8") as file:
        file.write(text)
        file.write("\n")
        file.write("-" * 40)
        file.write("\n")

# Generate Final Bill

def generate_bill():

    if not cart:
        print("Cart Empty.")
        return

    print("\n========== FINAL BILL ==========")

    subtotal = 0

    bill = "\n========== FINAL BILL ==========\n"

    for item, qty in cart.items():

        price = products[item]

        amount = qty * price

        subtotal += amount

        line = f"{item:10} Qty:{qty:<3} Price:Rs.{price:<4} Amount:Rs.{amount}"

        print(line)

        bill += line + "\n"

    discount = calculate_discount(subtotal)

    if subtotal > 1000:
        discount_text = "10%"
    elif subtotal > 500:
        discount_text = "5%"
    else:
        discount_text = "0%"

    gst = (subtotal - discount) * 0.05

    final_amount = subtotal - discount + gst

    print("-------------------------------")
    print("Subtotal :", subtotal)
    print(f"Discount ({discount_text}) :", round(discount, 2))
    print("GST (5%) :", round(gst, 2))
    print("Final Amount :", round(final_amount, 2))

    bill += "\n"
    bill += f"Subtotal : {subtotal}\n"
    bill += f"Discount ({discount_text}) : {discount}\n"
    bill += f"GST : {gst}\n"
    bill += f"Final Amount : {final_amount}\n"

    save_bill(bill)
    print("Bill saved successfully!")

    cart.clear()
    print("Cart cleared for next customer.")
    print("Thank you for shopping with us!")

# View Purchase History
def purchase_history():
    try:
        with open("purchase_history.txt", "r", encoding="utf-8") as file:
            history = file.read()

            if history.strip() == "":
                print("No purchase history found.")
            else:
                print(history)

    except FileNotFoundError:
        print("No purchase history found.")

# Main Menu

def menu():

    while True:

        print("\n==============================")
        print(" Grocery Billing System")
        print("==============================")
        print("1. Display Products")
        print("2. Add to Cart")
        print("3. Remove Item")
        print("4. Show Cart")
        print("5. Generate Bill")
        print("6. Purchase History")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_products()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            remove_item()

        elif choice == "4":
            show_cart()

        elif choice == "5":
            generate_bill()

        elif choice == "6":
            purchase_history()

        elif choice == "7":
            print("Thank You!")
            break

        else:
            print("Invalid Choice")

# Program Starts Here
menu()