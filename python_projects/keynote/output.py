# Import the necessary libraries
import os
from datetime import datetime
from tkinter import BOTH, SUNKEN, TOP, Canvas, Label, filedialog
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox
import pptx
from pptx import Presentation

# Define the default file path
DEFAULT_FILE_PATH = "/Users/quentinmacbook/Library/Mobile Documents/com~apple~Keynote/Documents/_output/UXDI 34"

# Define the function that converts the keynote file to powerpoint and PDF

# Create the main window
window = tk.Tk()
window.geometry("400x300")
file_path_var = tk.StringVar(value=DEFAULT_FILE_PATH)

# Set the window title
window.title("Keynote File Converter")

#create a canvas for the drop area
canvas = Canvas(window, width = 400, height = 300, bg="white", relief=SUNKEN, bd=3, highlightthickness=0)
canvas.pack()

# create a label for the drop area
drop_label = Label(canvas, text="Drop Keynote File Here", font=("Helvetica", 16), bg="white")
drop_label.pack(side=TOP, fill=BOTH, expand=True)

# Create a button to allow the user to select a different file path
def select_file_path():
    file_path = filedialog.askdirectory()
    file_path_var.set(file_path)

file_path_button = tk.Button(window, text="Select File Path", command=select_file_path)
file_path_button.pack()

#create a label for the success message
success_label = Label(window, font=("Helvetica", 12), fg="green")
success_label.pack()

#create a label for the error message
error_label = Label(window, font=("Helvetica", 12), fg="red")
error_label.pack()

# Create a combobox for the file path
file_path_combobox = Combobox(window, values=[DEFAULT_FILE_PATH], state="readonly")
file_path_combobox.pack()

def convert_file(file_path):
    # Check if the file exists and is a keynote file
    if not os.path.exists(file_path) or not file_path.endswith(".key"):
        return False

    presentation = Presentation(file_path)

    # Generate the date string in the format YYYYMMDD
    date_str = datetime.now().strftime("%Y%m%d")

    # Generate the new file names
    keynote_file = date_str + " " + os.path.basename(file_path)
    powerpoint_file = date_str + " " + os.path.splitext(os.path.basename(file_path))[0] + ".pptx"
    pdf_file = date_str + " " + os.path.splitext(os.path.basename(file_path))[0] + ".pdf"

    # Convert the keynote file to powerpoint and PDF
    # The code for the conversion goes here
    presentation.save(keynote_file)
    presentation.save(powerpoint_file)

    #save pdf
    for slide in presentation.slides:
        pdf_file.write(slide.image)

    pdf_file.close()

    # Return the new file names

    return keynote_file, powerpoint_file, pdf_file

# Define the function that handles the drop event
def drop(event):
  # Get the file path of the dropped file
  file_path = event.data

  # Convert the file
  new_file_names = convert_file(file_path)

  # Check if the conversion was successful
  if new_file_names:
    # Update the UI to show the success message
    success_label.config(text=f"✅ Successfully converted file to {', '.join(new_file_names)}")
  else:
    # Update the UI to show the error message
    error_label.config(text="❌ Invalid file or error occurred during conversion")

# bind the "Drop" event to the drop function
canvas.bind("<Drop>", drop)

# enable file dropping on the Tkinter window
window.drop_target_register(tk.DND_FILES)

#start the Tkinter main event loop
window.mainloop()
