import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
from MainForm import *

class FormTotal(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.MintCream
		self._button1.Font = System.Drawing.Font("Tahoma", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(200, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(96, 49)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.MintCream
		self._button2.Font = System.Drawing.Font("Tahoma", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(200, 67)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(96, 49)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.MintCream
		self._button3.Font = System.Drawing.Font("Tahoma", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(200, 122)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(96, 49)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.SpringGreen
		self._groupBox1.Controls.Add(self._label9)
		self._groupBox1.Controls.Add(self._label8)
		self._groupBox1.Controls.Add(self._label7)
		self._groupBox1.Controls.Add(self._label6)
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Font = System.Drawing.Font("Tahoma", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(182, 169)
		self._groupBox1.TabIndex = 3
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Checkout"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.MintCream
		self._label1.Location = System.Drawing.Point(6, 26)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(85, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Options:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MintCream
		self._label2.Location = System.Drawing.Point(6, 55)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(64, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Type:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.MintCream
		self._label3.Location = System.Drawing.Point(6, 81)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(64, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Size:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.MintCream
		self._label4.Location = System.Drawing.Point(6, 110)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(64, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Color:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LimeGreen
		self._label5.Location = System.Drawing.Point(76, 55)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 4
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LimeGreen
		self._label6.Location = System.Drawing.Point(76, 81)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 5
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.LimeGreen
		self._label7.Location = System.Drawing.Point(76, 110)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 6
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.MintCream
		self._label8.Location = System.Drawing.Point(6, 136)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(64, 23)
		self._label8.TabIndex = 5
		self._label8.Text = "Total:"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.LimeGreen
		self._label9.Location = System.Drawing.Point(76, 136)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 7
		# 
		# FormTotal
		# 
		self.BackColor = System.Drawing.Color.MediumSeaGreen
		self.ClientSize = System.Drawing.Size(308, 188)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "FormTotal"
		self.Text = "FormTotal"
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		tot  = 50
		opt1 = 0
		opt2 = 0
		opt3 = 0
		self._label5.Text = str(opt1)
		self._label6.Text = str(opt2)
		self._label7.Text = str(opt3)
		self._label8.Text = str(tot)

	def Button2Click(self, sender, e):
		self._label5.Text = ""
		self._label6.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""

	def Button3Click(self, sender, e):
		MyParent = MainForm
		self.MyParent.Show()
		self.Hide()
		# !!!!!!!!!! Error: MainForm not defined !!!!!!!!!!