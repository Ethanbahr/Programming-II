import System.Drawing
import System.Windows.Forms
import tkinter as tk

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		# 
		# MainForm
		# 
		self.Name = "MainForm"
		self.Text = "TKinter test thingy"

# Create the main window
window = tk.Tk()
window.title("My Tkinter App")

# Create a button widget
button = tk.Button(window, text="Click Me")
button.pack()

# Start the main event loop
window.mainloop()

