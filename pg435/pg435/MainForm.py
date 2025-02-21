import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Snow
		self._label1.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(29, 38)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(120, 46)
		self._label1.TabIndex = 0
		self._label1.Text = "General Sales"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Snow
		self._label2.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(29, 99)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(120, 46)
		self._label2.TabIndex = 1
		self._label2.Text = "Student Sales"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Snow
		self._button1.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(186, 29)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(111, 64)
		self._button1.TabIndex = 2
		self._button1.Text = "General Sales"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Snow
		self._button2.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(186, 99)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(111, 64)
		self._button2.TabIndex = 3
		self._button2.Text = "Student Sales"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Snow
		self._button3.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(186, 169)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(111, 55)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Tomato
		self.ClientSize = System.Drawing.Size(319, 246)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg435"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from GeneralSales import *
		GS = GeneralSales()
		GS.Show()
		self.Hide()

	def Button2Click(self, sender, e):
		from StudentSales import *
		SS = StudentSales()
		SS.Show()
		self.Hide()

	def Button3Click(self, sender, e):
		Application.Exit()