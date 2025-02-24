﻿
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
from MainForm import *

class GeneralSales(Form):
	def __init__(self):
		self.InitializeComponent()
		self.pet = 0.0
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.SeaShell
		self._label1.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.Desktop
		self._label1.Location = System.Drawing.Point(12, 28)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(162, 37)
		self._label1.TabIndex = 0
		self._label1.Text = "Num of tickets:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.SeaShell
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.ForeColor = System.Drawing.SystemColors.Desktop
		self._groupBox1.Location = System.Drawing.Point(12, 86)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(162, 149)
		self._groupBox1.TabIndex = 2
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Section:"
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.Color.SeaShell
		self._groupBox2.Controls.Add(self._label8)
		self._groupBox2.Controls.Add(self._label7)
		self._groupBox2.Controls.Add(self._label6)
		self._groupBox2.Controls.Add(self._label5)
		self._groupBox2.Controls.Add(self._label4)
		self._groupBox2.Controls.Add(self._label3)
		self._groupBox2.Controls.Add(self._label2)
		self._groupBox2.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.ForeColor = System.Drawing.SystemColors.Desktop
		self._groupBox2.Location = System.Drawing.Point(190, 86)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(162, 149)
		self._groupBox2.TabIndex = 3
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Cost:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.SystemColors.Desktop
		self._textBox1.Location = System.Drawing.Point(190, 28)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(158, 36)
		self._textBox1.TabIndex = 4
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.WhiteSmoke
		self._radioButton1.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.Location = System.Drawing.Point(6, 29)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(150, 36)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Section A"
		self._radioButton1.UseVisualStyleBackColor = False
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.WhiteSmoke
		self._radioButton2.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.Location = System.Drawing.Point(6, 65)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(150, 36)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Section B"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.WhiteSmoke
		self._radioButton3.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.Location = System.Drawing.Point(6, 107)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(150, 36)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Section C"
		self._radioButton3.UseVisualStyleBackColor = False
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SeaShell
		self._button1.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(33, 241)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(111, 51)
		self._button1.TabIndex = 5
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.SeaShell
		self._button2.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(232, 241)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(86, 51)
		self._button2.TabIndex = 6
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.WhiteSmoke
		self._label2.Location = System.Drawing.Point(6, 32)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(90, 33)
		self._label2.TabIndex = 0
		self._label2.Text = "Tickets:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.WhiteSmoke
		self._label3.Location = System.Drawing.Point(6, 65)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(81, 33)
		self._label3.TabIndex = 1
		self._label3.Text = "Tax:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.WhiteSmoke
		self._label4.Location = System.Drawing.Point(6, 98)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(81, 33)
		self._label4.TabIndex = 2
		self._label4.Text = "Total:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.WhiteSmoke
		self._label5.Location = System.Drawing.Point(99, 0)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(63, 33)
		self._label5.TabIndex = 3
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.WhiteSmoke
		self._label6.Location = System.Drawing.Point(99, 33)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(63, 33)
		self._label6.TabIndex = 4
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.WhiteSmoke
		self._label7.Location = System.Drawing.Point(95, 65)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(63, 33)
		self._label7.TabIndex = 5
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.WhiteSmoke
		self._label8.Location = System.Drawing.Point(93, 101)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(63, 33)
		self._label8.TabIndex = 6
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# GeneralSales
		# 
		self.BackColor = System.Drawing.Color.Salmon
		self.ClientSize = System.Drawing.Size(360, 304)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._label1)
		self.Name = "GeneralSales"
		self.Text = "GeneralSales"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()



	def Button1Click(self, sender, e):
		a   = self._radioButton1.Checked()
		b   = self._radioButton2.Checked()
		c   = self._radioButton3.Checked()
		cst = 0.0
		tix = self._textBox1.Text
		tax = 0.0
		tot = cost + tax
		if a == Checked():
			cst      = 3
			self.pet = 0
		self._label5.text = res

	def Button2Click(self, sender, e):
		MainForm.Show()
		self.Exit()