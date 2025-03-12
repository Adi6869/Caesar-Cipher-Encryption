import tkinter as tk
from tkinter import messagebox
from caesar_cipher_encryption import caesar_cipher, caesar_decipher

def text_process():
    text = text_entry.get("1.0", "end-1c")
    shift = shift_entry.get()
    
    if not shift.isdigit():
        messagebox.showerror("Error", "Shift value must be an integer")
        return
    
    shift = int(shift)
    
    if mode_var.get() == "Encrypt":
        output = caesar_cipher(shift, text)
    else:
        output = caesar_decipher(shift, text)
    
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, output)

root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry('400x300')

tk.Label(root, text="Enter the text:").pack()
text_entry = tk.Text(root, height=4, width=40)
text_entry.pack()

tk.Label(root, text="Shift Value:").pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

mode_var = tk.StringVar(value="Encrypt")
tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt").pack()
tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt").pack()

tk.Button(root, text="Process", command=text_process).pack()

tk.Label(root, text="Result:").pack()
result_text = tk.Text(root, height=4, width=40)
result_text.pack()

root.mainloop()