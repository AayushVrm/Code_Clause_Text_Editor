import tkinter as tk
from tkinter import filedialog, messagebox

def save_text():
    text = text_entry.get("1.0", tk.END)
    # Add your code here to save the text to a file or perform any other actions
    messagebox.showinfo("Success", "Text saved successfully!")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
            text_entry.delete("1.0", tk.END)
            text_entry.insert("1.0", text)

def open_popup():
    global text_entry
    popup = tk.Toplevel()
    popup.title("Text Editor")
    popup.geometry("600x450")

    text_entry = tk.Text(popup)
    text_entry.pack()

    open_file_button = tk.Button(popup, text="Open Existing File", command=open_file)
    open_file_button.pack()

    save_button = tk.Button(popup, text="Save", command=save_text)
    save_button.pack()

    popup.mainloop()

# Main window
window = tk.Tk()
window.title("Main Window")

open_button = tk.Button(window, text="Open Text Editor", command=open_popup)
open_button.pack()

window.mainloop()
