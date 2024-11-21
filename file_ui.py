import tkinter as tk
from tkinter import filedialog, messagebox
import os
from src.data_preprocessing import load_and_preprocess_data, split_data

def add_file():
    """
    Opens a file dialog to add .txt files and displays them in the listbox.
    """
    file_path = filedialog.askopenfilename(
        title="Select a Data File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        # Add file path to the listbox
        file_listbox.insert(tk.END, file_path)
        messagebox.showinfo("File Added", f"File {os.path.basename(file_path)} added successfully!")

def remove_selected():
    """
    Removes the selected file from the listbox.
    """
    selected = file_listbox.curselection()
    if selected:
        file_listbox.delete(selected)
    else:
        messagebox.showwarning("No Selection", "Please select a file to remove.")

def process_files():
    """
    Processes all files added to the listbox using the data preprocessing logic.
    """
    files = file_listbox.get(0, tk.END)
    if not files:
        messagebox.showerror("No Files", "No files to process. Please add files first.")
        return

    for file_path in files:
        try:
            # Step 1: Load and preprocess the data
            scaled_data, scaler = load_and_preprocess_data(file_path)

            # Step 2: Split the data into sequences
            X, y = split_data(scaled_data)

            # Example output: Log the number of samples processed
            print(f"Processed {file_path}:")
            print(f"Number of samples (X): {len(X)}")
            print(f"Number of targets (y): {len(y)}")

            # Additional processing logic can be added here
            # e.g., training a model, making predictions, etc.

        except Exception as e:
            messagebox.showerror("Processing Error", f"Error processing {file_path}: {e}")
            return

    messagebox.showinfo("Processing Complete", "All files processed successfully!")

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