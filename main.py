#Written by J.C. Paz, using CTS Standards to calculate speaker coverage diameter at seated standard height
from math import tan
from math import ceil
# d =  2 * (H1-H2) * [tan(CD)/2]

#Results = f"Speaker Coverage is {Speaker_Coverage}"

#print(Results)

import customtkinter as ctk
import tkinter as tk

# Function to get the input from the entry boxes and display the result
def get_values():
    try:
        # Retrieve the values entered by the user
        H1 = int(entry_H1.get())  # Get the value from the 'Ceiling Height' entry box
        CD = int(entry_CD.get())  # Get the value from the 'Degrees Speaker Coverage' entry box
        
        # Calculate or format your result
        
        H2 = 48

        H3 = 60

        A = tan(CD)/2

        B = H1 - H2

        Speaker_Coverage = 2 * B * A  
         # Ensure the result is positive and rounded up
        Speaker_Coverage = abs(Speaker_Coverage)  # Make the result positive (absolute value)
        Speaker_Coverage = ceil(Speaker_Coverage)  # Round the result up
        Results = f"Speaker Coverage is {Speaker_Coverage} inches"
        
        # Update the result label to display the output
        result_label.configure(text=Results)
        
        
        # Optionally print to the console as well
        print(Results)
        
    except ValueError:
        # Handle the case where input is not a valid integer
        result_label.config(text="Please enter valid integers.")
        print("Please enter valid integers.")

# Initialize the root window
root = ctk.CTk()

# Set the title of the window
root.title("Speaker Coverage calculator")

# Set the window size (width x height)
root.geometry("400x400")

# Create a label and input box for Ceiling Height (H1)
label_H1 = ctk.CTkLabel(root, text="Ceiling Height in Inches:")
label_H1.pack(pady=10)

entry_H1 = ctk.CTkEntry(root)
entry_H1.pack(pady=10)

# Create a label and input box for Degrees Speaker Coverage (CD)
label_CD = ctk.CTkLabel(root, text="Enter Degrees Speaker Coverage:")
label_CD.pack(pady=10)

entry_CD = ctk.CTkEntry(root)
entry_CD.pack(pady=10)

# Create a submit button to get the values
submit_button = ctk.CTkButton(root, text="Submit", command=get_values)
submit_button.pack(pady=20)

# Create a label to display the result
result_label = ctk.CTkLabel(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Function to clear the input fields and result box
def clear_values():
    entry_H1.delete(0, "end")  # Clear the Ceiling Height entry
    entry_CD.delete(0, "end")  # Clear the Degrees Speaker Coverage entry    
    result_label.configure(text="") # Clear the result label txt

# Create a button to clear the inputs and result box
clear_button = ctk.CTkButton(root, text="Clear", command=clear_values)
clear_button.pack(pady=10)

# Run the main loop
root.mainloop()
