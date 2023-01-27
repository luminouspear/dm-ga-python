<<<<<<< HEAD

import tkinter as tk
from TkinterDnD2 import DND_FILES, TkinterDnD
from pptx import Presentation

dst_dir = "/Users/quentinmacbook/Library/Mobile Documents/com~apple~Keynote/Documents/_output/UXDI 34"
=======
import os
import sys
import tkinter as tk
from tkinter import filedialog

import pptx
from pptx import Presentation
>>>>>>> refs/remotes/origin/main

def convert_file(filepath):
    # open the keynote file using keynote-parser
    presentation = Presentation(filepath)
<<<<<<< HEAD
    base = dst_dir + filepath.split("/")[-1]

    # save the file as a keynote
    keynote_name = base + ".key"
    presentation.save(keynote_name)

    # save the file as a powerpoint
    pptx_name = base + ".pptx"
    presentation.save(pptx_name)

    # save the file as a pdf
    pdf_file = (base + ".pdf")

=======

    # save the file as a keynote
    presentation.save(f"{dst_dir}/{filepath.split('/')[-1]}.key")

    # save the file as a powerpoint
    presentation.save(f"{dst_dir}/{filepath.split('/')[-1]}.pptx")

    # save the file as a pdf
    pdf_file = (f"{dst_dir}/{filepath.split('/')[-1]}.pdf")
>>>>>>> refs/remotes/origin/main

    for slide in presentation.slides:
        pdf_file.write(slide.image)

    pdf_file.close()

def drop_file_callback(event):
    #get the filepath from the event data
    filepath = event.data
<<<<<<< HEAD
    label["text"] = "Converting file: " + filepath
    convert_file(filepath)
    label["text"] = "Conversion complete"

# create the Tkinter root window
root = TkinterDnD.Tk()
=======
    label["text"] = f"Converting file: {filepath}"
    convert_file(filepath)
    label["text"] = "✅ Conversion complete"

# create the Tkinter root window
root = tk.Tk()
>>>>>>> refs/remotes/origin/main

# set the window title and size
root.title("Keynote Converter")
root.geometry("600x400")

# create a Tkinter label to display the drop zone message
label = tk.Label(root, text="Drop Keynote File Here", font=("sans serif", 24))
label.pack()

# bind the "Drop" event to teh drop_file_callbal function
root.bind("<<Drop>>", drop_file_callback)

# enable file dropping on the Tkinter window
<<<<<<< HEAD
root.drop_target_register(DND_FILES)
=======
root.drop_target_register(tk.DND_FILES)
>>>>>>> refs/remotes/origin/main

# start the Tkinter main event loop
root.mainloop()

<<<<<<< HEAD
# # create the Tkinter root window
# root = tk.Tk()

# # set the window title and size
# root.title("Keynote Converter")
# root.geometry("600x400")

# # create a Tkinter label to display the drop zone message
# label = tk.Label(root, text="Drop Keynote File Here", font=("sans serif", 24))
# label.pack()

# # bind the "Drop" event to the drop_file_callback function
# root.bind("<<Drop>>", drop_file_callback)

# # enable file dropping on the Tkinter window
# root.drop_target_register(DND_FILES)

# # start the Tkinter main event loop
# root.mainloop()
=======
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
>>>>>>> refs/remotes/origin/main
