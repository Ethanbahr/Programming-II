
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.HotPink
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Teal
		self._button3.Location = System.Drawing.Point(253, 189)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(115, 60)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.HotPink
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Teal
		self._button2.Location = System.Drawing.Point(132, 189)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(115, 60)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.HotPink
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Teal
		self._button1.Location = System.Drawing.Point(11, 189)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(115, 60)
		self._button1.TabIndex = 3
		self._button1.Text = "Temporary Text"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# Form1
		# 
		self.BackColor = System.Drawing.Color.Olive
		self.ClientSize = System.Drawing.Size(380, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "Form1"
		self.Text = "Form1"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		MainForm.Show()
		Self.Hide