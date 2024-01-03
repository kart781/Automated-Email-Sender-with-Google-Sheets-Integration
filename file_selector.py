import tkinter as tk
from tkinter import filedialog, ttk, messagebox

def open_file_dialog():
    global file_path
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("All files", "*.*")],
        parent=root
    )
    update_file_path_label()

def update_file_path_label():
    file_path_label.config(text=file_path or "No file selected")

def confirm_selection():
    if file_path:
        print("Selected file:", file_path)  # Example action
        root.destroy()
    else:
        messagebox.showinfo("No file selected", "Please select a file.")

def store_link():
    global link
    link = link_entry.get()
    if link:
        print("Stored link:", link)  # Example action
        messagebox.showinfo("Link stored", f"Link '{link}' has been stored.")
    else:
        messagebox.showinfo("No link", "No link was entered.")

# Create the main window
root = tk.Tk()
root.title("File and Directory Explorer")
root.geometry("600x500")

file_path = None
link = None

# Style configuration
style = ttk.Style(root)
style.configure('TButton', font=('Arial', 12))
style.configure('TLabel', font=('Arial', 12), anchor="center")

# Create a label for file selection instructions
title_label = ttk.Label(root, text="Please select a file", font=('Arial', 14, 'bold'))
title_label.pack(pady=(20, 10))

# Create a button to open the file dialog
file_button = ttk.Button(root, text="Open File Explorer", command=open_file_dialog)
file_button.pack(pady=10)

# Label to display the selected file path
file_path_label = ttk.Label(root, text="No file selected", wraplength=350)
file_path_label.pack(pady=10, fill='x')

# Entry for link input
link_entry = ttk.Entry(root, font=('Arial', 12), width=30)
link_entry.pack(pady=10)

# Button to store link
store_link_button = ttk.Button(root, text="Store Link", command=store_link)
store_link_button.pack(pady=10)

# Button to confirm file selection
confirm_button = ttk.Button(root, text="Confirm Selection", command=confirm_selection)
confirm_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
