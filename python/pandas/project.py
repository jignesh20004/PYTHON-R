import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SupermarketDataAnalyzer:
    # Constructor to initialize the class and load the data if file_path is provided
     # Agar file_path diya gaya hai to data load karega, nahi to empty DataFrame bana dega
    def __init__(self, file_path=None): 
        self.data = pd.DataFrame() # Empty DataFrame initialize karte hai
        if file_path:   
            self.load_data(file_path)

    # Function to load CSV file into DataFrame
    # CSV file ko DataFrame mein load karne ke liye yeh function hai
    def load_data(self, file_path):
        try: # for error handle
            # CSV file ko pandas ke read_csv function se load karte hai
            self.data = pd.read_csv(file_path)
            print("Data Loaded Successfully!")
           # Jab try block me koi error aata hai, to except block us error ko handle karta hai.
        except FileNotFoundError:
            # Handle the case when file is not found
            print("File not found. Please enter a valid file path.")

    # Function to explore data with different options
    def explore_data(self):
        while True:
            print("\n== Explore Data ==")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Go back to main menu")
            choice = input("Enter your choice: ")

            # Handle user choices
            if choice == '1':
                print(self.data.head()) # Display first 5 rows
            elif choice == '2':
                print(self.data.tail()) # Display last 5 rows
            elif choice == '3':
                print(self.data.columns) # Display column names
            elif choice == '4':
                print(self.data.dtypes) # Display data types of each column
            elif choice == '5':
                print(self.data.info()) # Display basic info of dataset
            elif choice == '6':
                break # Exit the loop
            else:
                print("Invalid choice. Please try again.")
          # finction to perform dataframe operations      
    def perform_dataframe_operations(self):
        while True:
            print("\n== Perform DataFrame Operations ==")
            print("1. Add a new column")
            print("2. Delete a column")
            print("3. Sort DataFrame")
            print("4. Rename columns")
            print("5. Filter data")
            print("6. Go back to main menu")

            choice = input("Enter your choice: ")

            if choice == '1': # new column
                col_name = input("Enter new column name: ")
                self.data[col_name] = input(f"Enter values for {col_name} separated by commas: ").split(',')
                print("Column added successfully!")
            elif choice == '2': # delete column
                col_name = input("Enter column name to delete: ")
                self.data.drop(columns=[col_name], inplace=True)
                print("Column deleted successfully!")
            elif choice == '3': # Sort the data basis of column
                col_name = input("Enter column name to sort: ")
                self.data.sort_values(by=col_name, inplace=True)
                print("Data sorted successfully!")
            elif choice == '4': # name change
                old_name = input("Enter old column name: ")
                new_name = input("Enter new column name: ")
                self.data.rename(columns={old_name: new_name}, inplace=True)
                print("Column renamed successfully!")
            elif choice == '5': # filter the data
                condition = input("Enter condition (e.g., Age>30): ")
                filtered_data = self.data.query(condition)
                print(filtered_data)
            elif choice == '6': # main menu return
                break
            else:
                print("Invalid choice. Please try again.")            

    # Function to handle missing data in the DataFrame
    def handle_missing_data(self):
        while True:
            print("\n== Handle Missing Data ==")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            print("5. Go back to main menu")
            choice = input("Enter your choice: ")

            # Display rows with missing values
            if choice == '1':
                missing = self.data[self.data.isnull().any(axis=1)]
                if missing.empty:
                    print("No missing values found in the dataset!")
                else:
                    print(missing)
            # Fill missing values with column mean
            elif choice == '2':
                self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
                print("Missing values filled with mean.")
            # Drop rows that contain missing values
            elif choice == '3':
                self.data.dropna(inplace=True)
                print("Rows with missing values dropped.")
            # Replace missing values with a specific value
            elif choice == '4':
                value = input("Enter the value to replace missing values: ")
                self.data.fillna(value, inplace=True)
                print("Missing values replaced with", value)
            # Exit the loop
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    # Function to generate descriptive statistics of the data 
    def generate_descriptive(self):
        if not self.data.empty:
            # Display statistical description of the data
            print(self.data.describe())
        else:
            print("No data found")

    # Function to visualize data using different types of plots
    def visualize_data(self):
        if self.data.empty:
            print("No dataset loaded.")
            return

        print("\nSelect visualization type:")
        print("1. Histogram")
        print("2. Bar Chart")
        print("3. Line Chart")
        print("4. Scatter Plot")
        print("5. Box Plot")
        print("6. Pie Chart")

        choice = input("Enter choice: ").strip()
        column = input("Enter column name for visualization: ").strip()

        # Check if column exists in the DataFrame
        if column not in self.data.columns:
            print("Invalid column name.")
            return

        plt.figure(figsize=(10, 6))

        # Handle different types of visualizations
        if choice == '1':
            self.data[column].hist()
        elif choice == '2':
            self.data[column].value_counts().plot(kind='bar',legend=True)
        elif choice == '3':
            self.data[column].plot(kind='line',legend=True)
        elif choice == '4':
            x_col = input("Enter X-axis column: ").strip()
            if x_col in self.data.columns:
                self.data.plot(kind='scatter', x=x_col, y=column,legend=True)
            else:
                print("Invalid X-axis column.")
                return
        elif choice == '5':
            self.data[column].plot(kind='box',legend=True)
        elif choice == '6':
            self.data[column].value_counts().plot(kind='pie', autopct='%1.1f%%',legend=True)
        else:
            print("Invalid choice.")
            return

        plt.title(f"{column} Visualization")
        plt.show()

    # Function to save visualizations as PNG files
    def save_visualization(self):
        if self.data.empty:
            print("No dataset loaded.")
            return

        column = input("Enter column name to save visualization: ").strip()
        if column not in self.data.columns:
            print("Invalid column name.")
            return

        # Generate and save the plot as PNG
        plt.figure(figsize=(10, 6))
        self.data[column].value_counts().plot(kind='bar')
        plt.title(f"{column} Visualization")

        file_name = input("Enter file name to save (without extension): ").strip()
        plt.savefig(f"{file_name}.png")
        print(f"Visualization saved as {file_name}.png")

# Main function to drive the menu-based interface
if __name__ == "__main__":
    analyzer = SupermarketDataAnalyzer()
    while True:
        print("""
        =========== Data Analysis & Visualization Program ==========
        Please select an option:
        1. Load Dataset
        2. Explore Data
        3. Perform dataframe operations     
        4. Handle Missing Data
        5. Generate Descriptive Statistics
        6. Data Visualization
        7. Save Visualization
        8. Exit
        ============================================================
        """)
        choice = input("Enter your choice: ")
        # Handle user choices
        if choice == '1':
            file_path = input("Enter the path of the dataset (CSV file): ")
            analyzer.load_data(file_path)
        elif choice == '2':
            analyzer.explore_data()
        elif choice == '3':
             analyzer.perform_dataframe_operations()    
        elif choice == '4':
            analyzer.handle_missing_data()
        elif choice == '5':
            analyzer.generate_descriptive()
        elif choice == '6':
            analyzer.visualize_data()
        elif choice == '7':
            analyzer.save_visualization()
        elif choice == '8':
            print("Exiting the program.Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")