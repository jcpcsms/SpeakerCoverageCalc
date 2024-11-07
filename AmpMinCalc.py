#Written by J.C. Paz, using CTS Standards to calculate minimum wattage from Amp based on ceiling speaker selection
from math import ceil
# Wt = Ws * N * 1.5 

import customtkinter as ctk
import tkinter as tk

# Function to get the input from the entry boxes and display the result
def get_values():
    try:
        # Retrieve the values entered by the user
        W = int(entry_W.get())  # Get the value from the'Wattage tap' entry box
        N = int(entry_N.get())  # Get the value from the 'Number of speakers' entry box
        
        # Calculate or format your result
        
        A = 1.5

        Min_Wattage = W * N * A  
         # Ensure the result is positive and rounded up
        Min_Wattage = abs(Min_Wattage)  # Make the result positive (absolute value)
        Min_Wattage = ceil(Min_Wattage)  # Round the result up
        Results = f"Minimum Wattage from Amp is {Min_Wattage} Watts"
        
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
root.title("Amp Minimum Wattage Calc")

# Set the window size (width x height)
root.geometry("400x400")

# Create a label and input box for Ceiling Height (H1)
label_W = ctk.CTkLabel(root, text="Wattage Tap on Speaker:")
label_W.pack(pady=10)

entry_W = ctk.CTkEntry(root)
entry_W.pack(pady=10)

# Create a label and input box for Degrees Speaker Coverage (CD)
label_N = ctk.CTkLabel(root, text="Number of Speakers:")
label_N.pack(pady=10)

entry_N = ctk.CTkEntry(root)
entry_N.pack(pady=10)

# Create a submit button to get the values
submit_button = ctk.CTkButton(root, text="Submit", command=get_values)
submit_button.pack(pady=20)

# Create a label to display the result
result_label = ctk.CTkLabel(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Function to clear the input fields and result box
def clear_values():
    entry_W.delete(0, "end")  # Clear the Ceiling Height entry
    entry_N.delete(0, "end")  # Clear the Degrees Speaker Coverage entry    
    result_label.configure(text="") # Clear the result label txt

# Create a button to clear the inputs and result box
clear_button = ctk.CTkButton(root, text="Clear", command=clear_values)
clear_button.pack(pady=10)

# Run the main loop
root.mainloop()
