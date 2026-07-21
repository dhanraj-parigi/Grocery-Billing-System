
"""
Grocery Billing System
Demonstrates:
- Class & Object
- Constructor
- Instance Variables
- Class Variables
- Instance Methods
- Class Methods
- Static Methods
- Magic Method (__str__)
- File Handling
- Exception Handling
"""

from datetime import datetime


class GroceryBillingSystem:

    # ---------- Class Variables ----------
    STORE_NAME = "ABC Super Market"
    GST_RATE = 0.05

    def __init__(self):
        self.products = {
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
        self.cart = {}

    def __str__(self):
        return f"Welcome to {self.STORE_NAME}"

    @classmethod
    def change_store_name(cls, name):
        cls.STORE_NAME = name
        print("Store name updated successfully.")

    @classmethod
    def change_gst_rate(cls, rate):
        if 0 <= rate <= 1:
            cls.GST_RATE = rate
            print("GST updated successfully.")
        else:
            print("Invalid GST.")

    @staticmethod
    def calculate_discount(total):
        if total > 1000:
            return total * 0.10, "10%"
        elif total > 500:
            return total * 0.05, "5%"
        return 0, "0%"

    @staticmethod
    def validate_quantity(qty):
        return qty > 0

    @staticmethod
    def current_time():
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def display_products(self):
        print("\n========== PRODUCTS ==========")
        print(f"{'Product':<10}{'Price'}")
        print("-" * 25)
        for item, price in self.products.items():
            print(f"{item:<10} ₹{price}")

    def add_to_cart(self):
        self.display_products()
        item = input("\nEnter Product Name : ").title()

        if item not in self.products:
            print("Product not available.")
            return

        try:
            qty = int(input("Enter Quantity : "))
            if not self.validate_quantity(qty):
                print("Invalid Quantity.")
                return

            self.cart[item] = self.cart.get(item, 0) + qty
            print("Item added successfully.")

        except ValueError:
            print("Please enter a valid number.")

    def remove_item(self):
        if not self.cart:
            print("Cart is empty.")
            return

        self.show_cart()

        item = input("\nEnter Product Name to Remove : ").title()

        if item in self.cart:
            del self.cart[item]
            print("Item removed.")
        else:
            print("Item not found.")

    def update_quantity(self):
        if not self.cart:
            print("Cart is empty.")
            return

        self.show_cart()

        item = input("Enter Product Name : ").title()

        if item not in self.cart:
            print("Item not found.")
            return

        try:
            qty = int(input("Enter New Quantity : "))

            if qty <= 0:
                del self.cart[item]
                print("Item removed because quantity is 0.")
            else:
                self.cart[item] = qty
                print("Quantity updated.")

        except ValueError:
            print("Invalid Quantity.")

    def show_cart(self):
        if not self.cart:
            print("\nCart is empty.")
            return

        print("\n========== CART ==========")

        subtotal = 0

        for item, qty in self.cart.items():
            price = self.products[item]
            amount = price * qty
            subtotal += amount
            print(f"{item:<10} Qty:{qty:<3} Price:₹{price:<4} Amount:₹{amount}")

        print("-" * 40)
        print("Subtotal :", subtotal)

    def save_bill(self, bill):
        with open("purchase_history.txt", "a", encoding="utf-8") as file:
            file.write(bill)
            file.write("\n" + "=" * 60 + "\n")

    def purchase_history(self):
        try:
            with open("purchase_history.txt", "r", encoding="utf-8") as file:
                data = file.read()
                if data.strip():
                    print(data)
                else:
                    print("No purchase history found.")
        except FileNotFoundError:
            print("No purchase history found.")

    def generate_bill(self):
        if not self.cart:
            print("Cart is empty.")
            return

        print("\n========== FINAL BILL ==========")
        print(self)

        bill = []
        bill.append("=" * 60)
        bill.append(self.STORE_NAME)
        bill.append("Date : " + self.current_time())
        bill.append("=" * 60)

        subtotal = 0

        for item, qty in self.cart.items():
            price = self.products[item]
            amount = price * qty
            subtotal += amount

            line = f"{item:<10} Qty:{qty:<3} Price:₹{price:<4} Amount:₹{amount}"
            print(line)
            bill.append(line)

        discount, discount_text = self.calculate_discount(subtotal)

        taxable = subtotal - discount
        gst = taxable * self.GST_RATE
        final = taxable + gst

        print("-" * 40)
        print("Subtotal :", subtotal)
        print(f"Discount ({discount_text}) :", round(discount, 2))
        print(f"GST ({int(self.GST_RATE*100)}%) :", round(gst, 2))
        print("Final Amount :", round(final, 2))

        bill.append("-" * 40)
        bill.append(f"Subtotal : {subtotal}")
        bill.append(f"Discount ({discount_text}) : {discount:.2f}")
        bill.append(f"GST : {gst:.2f}")
        bill.append(f"Final Amount : {final:.2f}")

        self.save_bill("\n".join(bill))
        print("\nBill saved successfully.")
        self.cart.clear()

    def admin_menu(self):
        while True:
            print("\n----- ADMIN MENU -----")
            print("1. Change Store Name")
            print("2. Change GST")
            print("3. Back")

            ch = input("Choice : ")

            if ch == "1":
                name = input("Enter New Store Name : ")
                GroceryBillingSystem.change_store_name(name)

            elif ch == "2":
                try:
                    gst = float(input("Enter GST Percentage (Example 18 for 18%) : "))
                    GroceryBillingSystem.change_gst_rate(gst / 100)
                except ValueError:
                    print("Invalid GST.")

            elif ch == "3":
                break

            else:
                print("Invalid choice.")

    def menu(self):
        while True:
            print("\n" + "=" * 50)
            print(self.STORE_NAME)
            print("=" * 50)
            print("1. Display Products")
            print("2. Add To Cart")
            print("3. Remove Item")
            print("4. Update Quantity")
            print("5. Show Cart")
            print("6. Generate Bill")
            print("7. Purchase History")
            print("8. Admin Settings")
            print("9. Exit")

            choice = input("Enter Choice : ")

            if choice == "1":
                self.display_products()
            elif choice == "2":
                self.add_to_cart()
            elif choice == "3":
                self.remove_item()
            elif choice == "4":
                self.update_quantity()
            elif choice == "5":
                self.show_cart()
            elif choice == "6":
                self.generate_bill()
            elif choice == "7":
                self.purchase_history()
            elif choice == "8":
                self.admin_menu()
            elif choice == "9":
                print("Thank You for Shopping!")
                break
            else:
                print("Invalid Choice.")


if __name__ == "__main__":
    billing = GroceryBillingSystem()
    billing.menu()