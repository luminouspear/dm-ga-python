import os
import sys
import tkinter as tk
from tkinter import filedialog

import pptx
from pptx import Presentation

def convert_file(filepath):
    # open the keynote file using keynote-parser
    presentation = Presentation(filepath)

    # save the file as a keynote
    presentation.save(f"{dst_dir}/{filepath.split('/')[-1]}.key")

    # save the file as a powerpoint
    presentation.save(f"{dst_dir}/{filepath.split('/')[-1]}.pptx")

    # save the file as a pdf
    pdf_file = (f"{dst_dir}/{filepath.split('/')[-1]}.pdf")

    for slide in presentation.slides:
        pdf_file.write(slide.image)

    pdf_file.close()

def drop_file_callback(event):
    #get the filepath from the event data
    filepath = event.data
    label["text"] = f"Converting file: {filepath}"
    convert_file(filepath)
    label["text"] = "✅ Conversion complete"

# create the Tkinter root window
root = tk.Tk()

# set the window title and size
root.title("Keynote Converter")
root.geometry("600x400")

# create a Tkinter label to display the drop zone message
label = tk.Label(root, text="Drop Keynote File Here", font=("sans serif", 24))
label.pack()

# bind the "Drop" event to teh drop_file_callbal function
root.bind("<<Drop>>", drop_file_callback)

# enable file dropping on the Tkinter window
root.drop_target_register(tk.DND_FILES)

# start the Tkinter main event loop
root.mainloop()

# create the Tkinter root window
root = tk.Tk()

# set the window title and size
root.title("Keynote Converter")
root.geometry("600x400")

# create a Tkinter label to display the drop zone message
label = tk.Label(root, text="Drop Keynote File Here", font=("sans serif", 24))
label.pack()

# bind the "Drop" event to the drop_file_callback function
root.bind("<<Drop>>", drop_file_callback)

# enable file dropping on the Tkinter window
root.drop_target_register(tk.DND_FILES)

# start the Tkinter main event loop
root.mainloop()
