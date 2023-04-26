import streamlit as st
from tkinter import filedialog
import tkinter as tk

# Define the function that will use the selected directory
def my_function(directory):
    # Do something with the selected directory
    st.write(f"You selected the directory: {directory}")

# Define a function to select a directory
def select_directory():
    # Create a Tk object to open the file dialog box
    root = tk.Tk()
    root.withdraw()

    # Show the file dialog box and get the selected directory
    directory = filedialog.askdirectory()

    # Call the function with the selected directory
    my_function(directory)

# Create a button to select the directory
if st.sidebar.button('Select Directory'):
    select_directory()