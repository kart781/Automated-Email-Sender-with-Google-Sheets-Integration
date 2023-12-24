import tkinter as tk
from tkinter import filedialog, ttk

def open_file_dialog():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("All files", "*.*")],
        parent=root  # Set the dialog's parent to the main window
    )
    if file_path:
        root.destroy()
        # You might want to add more logic here based on the file path

# Create the main window
root = tk.Tk()
root.title("File and Directory Explorer")
root.geometry("200x200")  # Set the size of the window

file_path = None

# Style configuration
style = ttk.Style(root)
style.configure('TButton', font=('Arial', 12))
style.configure('TLabel', font=('Arial', 12), anchor="center")

# Create a label for instructions or title
title_label = ttk.Label(root, text="Please select a file", font=('Arial', 14, 'bold'))
title_label.pack(pady=(20, 10))

# Create a button to trigger the file dialog
file_button = ttk.Button(root, text="Open File Explorer", command=open_file_dialog)
file_button.pack(pady=10)

# Label to display the selected file path
file_path_label = ttk.Label(root, text="", wraplength=550)
file_path_label.pack(pady=20, fill='x')

# Start the Tkinter event loop
root.mainloop()
