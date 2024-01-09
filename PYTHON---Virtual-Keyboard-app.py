import tkinter as tk

def key_press(key):
    print(f"Clicked: {key}")

root = tk.Tk()
root.title("Keyboard GUI")

keys = [
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
    'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
    'Z', 'X', 'C', 'V', 'B', 'N', 'M'
]

row_num = 0
col_num = 0

for key in keys:
    button = tk.Button(root, text=key, padx=10, pady=5, command=lambda k=key: key_press(k))
    button.grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 9:
        col_num = 0
        row_num += 1

root.mainloop()
