import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Salmon
		self._listBox1.Font = System.Drawing.Font("Segoe UI Emoji", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.SpringGreen
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 26
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(431, 238)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Magenta
		self._button1.Font = System.Drawing.Font("Segoe UI Emoji", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.LightSkyBlue
		self._button1.Location = System.Drawing.Point(12, 283)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(118, 77)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Magenta
		self._button2.Font = System.Drawing.Font("Segoe UI Emoji", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.LightSkyBlue
		self._button2.Location = System.Drawing.Point(170, 283)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(118, 77)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Magenta
		self._button3.Font = System.Drawing.Font("Segoe UI Emoji", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.LightSkyBlue
		self._button3.Location = System.Drawing.Point(325, 283)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(118, 77)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SpringGreen
		self.ClientSize = System.Drawing.Size(455, 372)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog122a"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._listBox.Items.Clear()
		sqrd = 
		sqrt =

	def Button2Click(self, sender, e):
		self._listBox.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()