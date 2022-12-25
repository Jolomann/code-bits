# buttons don't do anything lol
# i also wanted to make this a standalone python executable but couldn't get the build from PyInstaller to work properly

import tkinter as tk

# Make the window
window = tk.Tk()
window.title("Calculator")


# Make the current number display
display = tk.Label(window, text="0", font=("Helvetica", 32), width=20, anchor="e")
display.grid(row=0, column=0, columnspan=4)

# Make buttons
button_7 = tk.Button(window, text="7", font=("Helvetica", 32), width=5)
button_7.grid(row=1, column=0)
button_8 = tk.Button(window, text="8", font=("Helvetica", 32), width=5)
button_8.grid(row=1, column=1)
button_9 = tk.Button(window, text="9", font=("Helvetica", 32), width=5)
button_9.grid(row=1, column=2)
button_div = tk.Button(window, text="/", font=("Helvetica", 32), width=5)
button_div.grid(row=1, column=3)

button_4 = tk.Button(window, text="4", font=("Helvetica", 32), width=5)
button_4.grid(row=2, column=0)
button_5 = tk.Button(window, text="5", font=("Helvetica", 32), width=5)
button_5.grid(row=2, column=1)
button_6 = tk.Button(window, text="6", font=("Arial", 32), width=5)
button_6.grid(row=2, column=2)
button_mul = tk.Button(window, text="*", font=("Arial", 32), width=5)
button_mul.grid(row=2, column=3)

button_1 = tk.Button(window, text="1", font=("Arial", 32), width=5)
button_1.grid(row=3, column=0)
button_2 = tk.Button(window, text="2", font=("Arial", 32), width=5)
button_2.grid(row=3, column=1)
button_3 = tk.Button(window, text="3", font=("Arial", 32), width=5)
button_3.grid(row=3, column=2)
button_sub = tk.Button(window, text="-", font=("Arial", 32), width=5)
button_sub.grid(row=3, column=3)

button_0 = tk.Button(window, text="0", font=("Arial", 32), width=5)
button_0.grid(row=4, column=0)
button_dot = tk.Button(window, text=".", font=("Arial", 32), width=5)
button_dot.grid(row=4, column=1)

# use this to make the program actually work. won't launch otherwise (probably because it only does a single pass of the code without it)
window.mainloop()