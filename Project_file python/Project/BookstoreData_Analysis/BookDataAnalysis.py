import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class SupermarketDataAnalyzer:
   
    def __init__(self, file_path=None): 
        self.data = pd.DataFrame() # Empty DataFrame initialize karte hai
        if file_path:   
            self.load_data(file_path)

    def load_data(self, file_path):
        try: # for error handle
            # CSV file ko pandas ke read_csv function se load karte hai
            self.data = pd.read_csv(file_path)
            print("Data Loaded Successfully!")
           # Jab try block me koi error aata hai, to except block us error ko handle karta hai.
        except FileNotFoundError:
            # Handle the case when file is not found
            print("File not found. Please enter a valid file path.")
