import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class Library:
    def __init__(self):
        # Load the inventory CSV file from user input
        self.inventory_path = input("Enter the path to the inventory CSV file: ")
        df = pd.read_csv(self.inventory_path)
        df.columns = df.columns.str.strip()  # Remove extra spaces in column names
        self.books = df.to_dict(orient='records')  # Convert CSV data to dictionary format using by the argument
        self.sales = {book['Title']: 0 for book in self.books}  # Har book ka sales count initialize karna

    def display_books(self):
        # Display available books in the library
        if not self.books:
            print("No books available in the library.")
            return
        df = pd.DataFrame(self.books)
        print("\nAvailable Books:\n", df, "\n")

    def borrow_books(self, user_name, user_mobile, titles, date_borrowed):
         # User se books borrow karne ka function
        titles = [title.strip().lower() for title in titles]  # User input normalize karna
        borrowed_books = []
        for title in titles:
            for book in self.books:
                book_title = book['Title'].strip().lower() # Stored title normalize karna
                if book_title == title:
                    if book['Quantity'] > 0:
                        book['Quantity'] -= 1  # Reduce stock quantity
                        self.sales[book['Title']] += 1  # Increase sales count
                        borrowed_books.append(f"{book['Title']} (Borrowed on {date_borrowed})")
                    else:
                        print(f'Sorry, "{book["Title"]}" is out of stock.\n')
                    break
            else:
                print(f'Book "{title}" not found in the library.\n')
        if borrowed_books:
            print(f'{user_name} ({user_mobile}) has borrowed {", ".join(borrowed_books)}.\n')
        self.display_books()  # Show remaining stock

    def trending_books(self):
        # Show trending books based on 5-star ratings
        trending = [book for book in self.books if str(book.get('Star_rating', '')).strip().lower() == 'five']
        if not trending:
            print("No trending books available yet. Only books with a 5-star rating are shown.")
            return
        print("Trending Books:")
        for book in trending:
            print(f"{book['Title']} - {book['Star_rating']} Stars")

    def load_new_data(self):
      # Naye books ka data user se input lena aur CSV me save karna
        print("Enter new book details:")
        title = input("Title: ")
        book_category = input("Category: ")
        star_rating = input("Star Rating (One to Five): ")
        price = float(input("Price: "))
        stock = input("Stock status (In stock/Out of stock): ")
        quantity = int(input("Quantity: "))
        category = input("Category: ")
        new_book = {
            "Title": title,
            "Book_cate": book_category,
            "Star_rating": star_rating,
            "Price": price,
            "Stock": stock,
            "Quantity": quantity,
            "Category": category
        }
        self.books.append(new_book)
        df = pd.DataFrame(self.books)
        df.to_csv(self.inventory_path, index=False)  # Save updated data back to CSV
        print("New book added successfully!")

    def plot_sales(self, plot_type):
        # Generate different types of sales plots
        if not any(self.sales.values()):
            print("No sales data available for plotting.")
            return
        df_sales = pd.DataFrame(list(self.sales.items()), columns=['Title', 'Sales'])
        df_sales_sorted = df_sales.sort_values(by='Sales', ascending=False)
        
        plt.figure(figsize=(14, 7))  # Increase plot size
        sns.set_style("whitegrid")
        x = np.arange(len(df_sales_sorted['Title']))

        if plot_type == "pie":
            plt.pie(df_sales_sorted['Sales'], labels=df_sales_sorted['Title'], autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black'})
            plt.title("Book Sales Distribution")
            plt.legend(title="Books")
        elif plot_type == "bar":
            sns.barplot(x=df_sales_sorted['Title'], y=df_sales_sorted['Sales'], palette='viridis')
            plt.xticks(rotation=45, ha='right', fontsize=10)
            plt.xlabel("Book Title")
            plt.ylabel("Number of Sales")
            plt.title("Book Sales Bar Chart")
            plt.legend(["Sales"], loc="best")
        elif plot_type == "line":
            sns.lineplot(x=x, y=df_sales_sorted['Sales'], marker='o', linestyle='-', color='b', label="Sales")
            plt.xticks(x, df_sales_sorted['Title'], rotation=45, ha='right', fontsize=10)
            plt.xlabel("Book Title")
            plt.ylabel("Number of Sales")
            plt.title("Book Sales Trend")
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.legend(title="Books")
        elif plot_type == "scatter":
            sns.scatterplot(x=x, y=df_sales_sorted['Sales'], color='r', label="Sales")
            plt.xticks(x, df_sales_sorted['Title'], rotation=45, ha='right', fontsize=10)
            plt.xlabel("Book Title")
            plt.ylabel("Number of Sales")
            plt.title("Book Sales Scatter Plot")
            plt.legend(title="Books")
        elif plot_type == "heatmap":
            df_correlation = pd.DataFrame(self.sales.items(), columns=['Title', 'Sales'])
            df_correlation['Price'] = [book['Price'] for book in self.books]
            correlation = df_correlation[['Price', 'Sales']].corr()
            sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f')
            plt.title("Heatmap of Correlation Between Book Prices and Sales Volumes")
        plt.show()

# Example usage
library = Library()

while True:
    print("1. Display Books")
    print("2. Borrow Books")
    print("3. Show Trending Books")
    print("4. Bar Plot")
    print("5. Line Plot")
    print("6. Scatter Plot")
    print("7. Heatmap: Correlation Between Book Prices and Sales Volumes")
    print("8. Load New Data")
    print("9. Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        library.display_books()
    elif choice == "2":
        user_name = input("Enter your name: ")
        user_mobile = input("Enter your mobile number: ")
        book_titles = input("Enter book titles to borrow (comma-separated): ").split(',')
        date_borrowed = input("Enter the date (DD-MM-YYYY): ")
        library.borrow_books(user_name, user_mobile, book_titles, date_borrowed)
    elif choice == "3":
        library.trending_books()
    elif choice == "4":
        library.plot_sales("bar")
    elif choice == "5":
        library.plot_sales("line")
    elif choice == "6":
        library.plot_sales("scatter")
    elif choice == "7":
        library.plot_sales("heatmap")
    elif choice == "8":
        library.load_new_data()
    elif choice == "9":
        print("Exiting... Thank you for visiting the library!")
        break
    else:
        print("Invalid choice! Please try again.\n")