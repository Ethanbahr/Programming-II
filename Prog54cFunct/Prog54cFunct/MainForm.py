﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Azure
		self._button1.Font = System.Drawing.Font("Palatino Linotype", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(2, 137)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(102, 53)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Azure
		self._button2.Font = System.Drawing.Font("Palatino Linotype", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(110, 137)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(102, 53)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Azure
		self._button3.Font = System.Drawing.Font("Palatino Linotype", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(218, 137)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(102, 53)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Azure
		self._label1.Font = System.Drawing.Font("Palatino Linotype", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 20)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(76, 28)
		self._label1.TabIndex = 3
		self._label1.Text = "Radius:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Azure
		self._label2.Font = System.Drawing.Font("Palatino Linotype", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 58)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(59, 28)
		self._label2.TabIndex = 4
		self._label2.Text = "Area:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Azure
		self._label3.Font = System.Drawing.Font("Palatino Linotype", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 95)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(140, 28)
		self._label3.TabIndex = 5
		self._label3.Text = "Circumference:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Snow
		self._textBox1.Font = System.Drawing.Font("Palatino Linotype", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(192, 17)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(128, 33)
		self._textBox1.TabIndex = 6
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Snow
		self._label4.Font = System.Drawing.Font("Palatino Linotype", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(192, 58)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(128, 28)
		self._label4.TabIndex = 7
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Snow
		self._label5.Font = System.Drawing.Font("Palatino Linotype", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(192, 95)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(127, 28)
		self._label5.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightBlue
		self.ClientSize = System.Drawing.Size(331, 202)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog54cFunct"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Area(rad):
		rad = self._textBox1.Text
		pi  = 3.14
		
	def Circ(rad):
		rad = self._textBox1.Text
		pi  = 3.14
	
	def Button1Click(self, sender, e):
		def main():
			Area = Area(rad)
			Circ = Circ(rad)
			self._label4.Text = pi * (rad ** 2)
			self._label5.Text = 2 * (rad * pi)


		if __name__ == "__main__":
			main()

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label4.Text   = ""
		self._label5.Text   = ""

	def Button3Click(self, sender, e):
		Application.Exit()