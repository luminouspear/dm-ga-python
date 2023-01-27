# Import the necessary libraries
import os
from datetime import datetime
from tkinter import  Canvas, Label, filedialog
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
window.configure(bg="white")
file_path_var = tk.StringVar(value=DEFAULT_FILE_PATH)

# Set the window title
window.title("Keynote File Converter")

#create a canvas for the drop area
canvas = tk.Canvas(window, width = 400, height = 300, bg="white", bd=3, highlightthickness=0)

#create a rectangle with rounded corners
arc1 = canvas.create_arc(20, 20, 40, 40, start=90, extent=90, fill='white')
arc2 = canvas.create_arc(360, 20, 380, 40, start=0, extent=90, fill='white')
arc3 = canvas.create_arc(360, 280, 380, 300, start=270, extent=90, fill='white')
arc4 = canvas.create_arc(20, 280, 40, 300, start=180, extent=90, fill='white')
rect = canvas.create_polygon([20, 20, 360, 20, 380, 40, 380, 280, 360, 300, 20, 300, 20, 280],
                             fill='', outline='#ccc', width=4)





# create a label for the drop area
drop_label = Label(canvas, text="Drop Keynote File Here", font=("Helvetica", 16), bg="white")
drop_label.pack(side="top", fill="both", expand=1)

canvas.pack(expand=1)

# Create a button to allow the user to select a different file path
def select_file_path():
    file_path = filedialog.askdirectory()
    file_path_var.set(file_path)


#create a label for the success message
success_label = Label(window, font=("Helvetica", 12), fg="green")
success_label.pack(expand=1)

#create a label for the error message
error_label = Label(window, font=("Helvetica", 12), fg="red")
error_label.pack(expand=1)

# Create a combobox for the file path
file_path_combobox = Combobox(window, values=[DEFAULT_FILE_PATH], state="readonly")
file_path_combobox.pack(side="bottom", ipady=10, expand=1)

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
def on_drop(event):
  # Get the file path of the dropped file
  file_path = event.data

  canvas.itemconfig(rect, outline="#333", dash=(5,5))

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
window.bind("<<Drop>>", on_drop)

# Give window focus
window.focus_force()

# # enable file dropping on the Tkinter window
# window.drop_target_register(tk.DND_FILES)
# canvas.

#start the Tkinter main event loop
window.mainloop()
