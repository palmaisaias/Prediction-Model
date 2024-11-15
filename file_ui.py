import tkinter as tk
from tkinter import filedialog, messagebox
import os

def add_file():
    file_path = filedialog.askopenfilename(
        title="Select a Data File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        # Add file path to the listbox
        file_listbox.insert(tk.END, file_path)
        messagebox.showinfo("File Added", f"File {os.path.basename(file_path)} added successfully!")

def remove_selected():
    selected = file_listbox.curselection()
    if selected:
        file_listbox.delete(selected)
    else:
        messagebox.showwarning("No Selection", "Please select a file to remove.")

def process_files():
    files = file_listbox.get(0, tk.END)
    if not files:
        messagebox.showerror("No Files", "No files to process. Please add files first.")
        return

    # Pass files to your main predictive model program
    for file_path in files:
        print(f"Processing file: {file_path}")
        # Here you can add the logic to use `file_path` in your main program

    messagebox.showinfo("Processing Complete", "Files processed successfully!")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Add Data Files")

# Frame for file list
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

file_listbox = tk.Listbox(frame, width=50, height=10)
file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame, orient="vertical", command=file_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")
file_listbox.config(yscrollcommand=scrollbar.set)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

add_button = tk.Button(button_frame, text="Add File", command=add_file)
add_button.grid(row=0, column=0, padx=5, pady=5)

remove_button = tk.Button(button_frame, text="Remove Selected", command=remove_selected)
remove_button.grid(row=0, column=1, padx=5, pady=5)

process_button = tk.Button(button_frame, text="Process Files", command=process_files)
process_button.grid(row=0, column=2, padx=5, pady=5)

# Run the Tkinter main loop
root.mainloop()