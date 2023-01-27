import tkinter as tk

# create the main window
root = tk.Tk()

# set the window title and size
root.title("File Converter")
root.geometry("400x300")

#create a canvas widget to display the status of the application
canvas = tk.Canvas(root,width=360, height=220,bg="white")
canvas.pack(ipadx=20,ipady=20)

#set the initial state of the application
canvas.configure(bg="lightgray",border=2)
canvas.create_oval(8,8,352,212,activewidth=2)

#create a label to display the initial message
label = tk.Label(root, text="Drop a .key file here", font=("Helvetica", 24))
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def func():
    print(f'button pressed')

# create a button to convert the file
buttonConvert = tk.Button(root, text="Convert", font=("Helvetica", 24), bg="blue", fg="white", command=func)
buttonConvert.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

# set the original background color of the button
original_bg = buttonConvert['bg']


def on_enter(event):
    # set the background color of the button to a brigher color
    buttonConvert.configure(bg="lightblue")

def on_leave(event):
    #set the color back to the original on exit
    buttonConvert.configure(bg=original_bg)

# bind the callback functions to the Enter and Leave events
buttonConvert.bind("<Enter>", on_enter)
buttonConvert.bind("<Leave>", on_leave)
# Create a button to choose the output directory
output_button = tk.Button(root, text="Choose Output Directory", font=("Helventica", 12))
output_button.pack(side=tk.BOTTOM, fill=tk.X)

# Load the last saved directory, if any, and save the current directory when the window is closed
LAST_SAVED_DIRECTORY_FILENAME = "save_location.txt"
last_saved_directory = ""

def on_closing():
    global last_saved_directory

    # save the current output directory to the file
    with open(LAST_SAVED_DIRECTORY_FILENAME, "w") as f:
        f.write(last_saved_directory)

    # close the window
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)


def handle_drop(event, data):
    print(f'a file was dropped event:{event} data:{data}')
    canvas.configure(bg="white")
    canvas.itemconfigure(oval_id, fill="black")
    check_file_type(event.data)


# Add an event handler to highlight the background when a file is dropped
# root.on_drop_file = highlight_background
root.bind("<Button-1>", handle_drop)


# Create the oval on the canvas
oval_id = canvas.create_oval(8,8,352,212,activewidth=2)

# Add an event handler to darken the oval when a file is dropped

def check_file_type(event, data):
    # Get the file path from the event data
    file_path = data
    print(data)

    # Check the file extension
    if not file_path.endswith(".key"):
        # If the file is not a .key file, display an error message
        label.configure(text="Error: Invalid file type", fg="red")

# start the main event loop
root.mainloop()
