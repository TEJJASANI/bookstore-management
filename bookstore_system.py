import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

class Bookstore:
    def __init__(self, inventory_file="inventory.csv", sales_file="sales.csv"):
        self.inventory_file = inventory_file
        self.sales_file = sales_file

        # Load inventory
        try:
            self.inventory = pd.read_csv(inventory_file)
        except:
            self.inventory = pd.DataFrame(columns=["Title", "Author", "Genre", "Price", "Quantity"])

        # Load sales
        try:
            self.sales = pd.read_csv(sales_file, parse_dates=["Date"])
        except:
            self.sales = pd.DataFrame(columns=["Date", "Title", "Quantity Sold", "Total Revenue"])

    # Add a new book
    def add_book(self, title, author, genre, price, quantity):
        mask = self.inventory["Title"] == title

        if mask.any():
            # Update existing quantity
            self.inventory.loc[mask, "Quantity"] += quantity
        else:
            new_book = {
                "Title": title,
                "Author": author,
                "Genre": genre,
                "Price": float(price),
                "Quantity": int(quantity),
            }
            self.inventory = pd.concat([self.inventory, pd.DataFrame([new_book])],
                                       ignore_index=True)

        print("Book added successfully!")

    # Update quantity
    def update_inventory(self, title, quantity):
        mask = self.inventory["Title"] == title
        if not mask.any():
            print("Book not found.")
            return

        self.inventory.loc[mask, "Quantity"] = quantity
        print("Inventory updated!")

    # Record sale
    def record_sale(self, date, title, quantity):
        mask = self.inventory["Title"] == title

        if not mask.any():
            print("Book not found.")
            return

        stock = int(self.inventory.loc[mask, "Quantity"].iloc[0])
        price = float(self.inventory.loc[mask, "Price"].iloc[0])

        if quantity > stock:
            print("Not enough stock!")
            return

        revenue = price * quantity

        # reduce stock
        self.inventory.loc[mask, "Quantity"] = stock - quantity

        sale = {
            "Date": pd.to_datetime(date),
            "Title": title,
            "Quantity Sold": quantity,
            "Total Revenue": revenue,
        }

        self.sales = pd.concat([self.sales, pd.DataFrame([sale])],
                               ignore_index=True)

        print("Sale recorded!")

    # Show summary
    def sales_summary(self):
        if self.sales.empty:
            print("No sales yet.")
            return

        total_rev = self.sales["Total Revenue"].sum()
        print("\n=== SALES SUMMARY ===")
        print("Total Revenue:", total_rev)

        print("\nTop Selling Books:")
        print(self.sales.groupby("Title")["Quantity Sold"].sum())

    # Show charts
    def visualize(self):
        if self.sales.empty:
            print("No sales to show.")
            return

        data = self.sales.merge(self.inventory[["Title", "Genre"]], on="Title")

        # Bar chart
        data.groupby("Genre")["Quantity Sold"].sum().plot(kind="bar")
        plt.title("Sales by Genre")
        plt.show()
        #pie chart
        plt.figure(figsize=(5, 5))
        genre_rev = data.groupby("Genre")["Total Revenue"].sum()
        plt.pie(genre_rev.values,
                labels=genre_rev.index,
                autopct="%1.1f%%")
        plt.title("Revenue Share by Genre")
        plt.tight_layout()
        plt.show()

        plt.figure(figsize=(6, 4))
        monthly = (data.set_index("Date").resample("M")["Total Revenue"].sum())
        plt.plot(monthly.index, monthly.values, marker="o")
        plt.title("Monthly Revenue Trend")
        plt.ylabel("Total Revenue")
        plt.xlabel("Month")
        plt.tight_layout()
        plt.show()
                
        
    # Save files
    def save(self):
        self.inventory.to_csv(self.inventory_file, index=False)
        self.sales.to_csv(self.sales_file, index=False)
        print("Data saved!")


# -----------------------------
# Menu System
# -----------------------------
def main():
    store = Bookstore()

    while True:
        print("\n--- Bookstore Menu ---")
        print("1. Add book")
        print("2. Update inventory quantity")
        print("3. Record sale")
        print("4. Show sales summary")
        print("5. Show charts")
        print("6. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            genre = input("Genre: ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
            store.add_book(title, author, genre, price, qty)

        elif choice == "2":
            title = input("Title: ")
            qty = int(input("New quantity: "))
            store.update_inventory(title, qty)

        elif choice == "3":
            date = input("Date (YYYY-MM-DD): ")
            title = input("Title: ")
            qty = int(input("Quantity sold: "))
            store.record_sale(date, title, qty)

        elif choice == "4":
            store.sales_summary()

        elif choice == "5":
            store.visualize()

        elif choice == "6":
            store.save()
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
