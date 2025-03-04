
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
from MainForm import *

class GeneralSales(Form):
	def __init__(self):
		self.InitializeComponent()
		self.myparent = MainForm()
#		self.pet = 0.0
	
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
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._labelcst = System.Windows.Forms.Label()
		self._labeltax = System.Windows.Forms.Label()
		self._labeltot = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
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
		self._groupBox2.Controls.Add(self._label2)
		self._groupBox2.Controls.Add(self._labeltot)
		self._groupBox2.Controls.Add(self._labeltax)
		self._groupBox2.Controls.Add(self._labelcst)
		self._groupBox2.Controls.Add(self._label4)
		self._groupBox2.Controls.Add(self._label3)
		self._groupBox2.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.ForeColor = System.Drawing.SystemColors.Desktop
		self._groupBox2.Location = System.Drawing.Point(190, 86)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(174, 149)
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
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.WhiteSmoke
		self._label3.Location = System.Drawing.Point(8, 55)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(81, 33)
		self._label3.TabIndex = 1
		self._label3.Text = "Tax:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.WhiteSmoke
		self._label4.Location = System.Drawing.Point(8, 97)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(81, 33)
		self._label4.TabIndex = 2
		self._label4.Text = "Total:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# labelcst
		# 
		self._labelcst.BackColor = System.Drawing.Color.WhiteSmoke
		self._labelcst.Location = System.Drawing.Point(93, 22)
		self._labelcst.Name = "labelcst"
		self._labelcst.Size = System.Drawing.Size(75, 33)
		self._labelcst.TabIndex = 3
		self._labelcst.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# labeltax
		# 
		self._labeltax.BackColor = System.Drawing.Color.WhiteSmoke
		self._labeltax.Location = System.Drawing.Point(95, 55)
		self._labeltax.Name = "labeltax"
		self._labeltax.Size = System.Drawing.Size(79, 33)
		self._labeltax.TabIndex = 5
		self._labeltax.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# labeltot
		# 
		self._labeltot.BackColor = System.Drawing.Color.WhiteSmoke
		self._labeltot.Location = System.Drawing.Point(93, 97)
		self._labeltot.Name = "labeltot"
		self._labeltot.Size = System.Drawing.Size(81, 33)
		self._labeltot.TabIndex = 6
		self._labeltot.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.WhiteSmoke
		self._label2.Location = System.Drawing.Point(8, 22)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(97, 33)
		self._label2.TabIndex = 7
		self._label2.Text = "Cost:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# GeneralSales
		# 
		self.BackColor = System.Drawing.Color.Salmon
		self.ClientSize = System.Drawing.Size(376, 304)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._label1)
		self.Name = "GeneralSales"
		self.Text = "GeneralSales"
		self.FormClosing += self.GeneralSalesFormClosing
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()



	def Button1Click(self, sender, e):
		tix  = self._textBox1.Text
		if self._radioButton1.Checked:
			cst2           = str(tix) * 15
			self._labelcst = "$" + str(cst2)
			self._labeltax = "$" + round((cst2 * 0.06), 2)
			self._labeltot = "$" + round((cst2 * 0.06) + str(tix), 2)
		elif self._radioButton2.Checked:
			cst2           = str(tix) * 20
			self._labelcst = "$" + str(cst2)
			self._labeltax = "$" + round((cst2 * 0.06), 2)
			self._labeltot = "$" + round((cst2 * 0.06) + str(tix), 2)
		elif self._radioButton3.Checked:
			cst2           = str(tix) * 25
			self._labelcst = "$" + str(cst2)
			self._labeltax = "$" + round((cst2 * 0.06), 2)
			self._labeltot = "$" + round((cst2 * 0.06) + str(tix), 2)

	def Button2Click(self, sender, e):
		self.Hide()
		self.myparent.Show()

	def GeneralSalesFormClosing(self, sender, e):
		self.myparent.Show()