import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My Tkinter App")

# Create a button widget
button = tk.Button(window, text="Click Me")
button.pack()

# Start the main event loop
window.mainloop()