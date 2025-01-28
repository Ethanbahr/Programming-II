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
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Salmon
		self._label1.Font = System.Drawing.Font("Tahoma", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(40, 29)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Num 1:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Salmon
		self._label2.Font = System.Drawing.Font("Tahoma", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(40, 65)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Num 2:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Salmon
		self._label3.Font = System.Drawing.Font("Tahoma", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(40, 104)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Num 3:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Salmon
		self._label4.Font = System.Drawing.Font("Tahoma", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(40, 141)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Num 4:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Salmon
		self._label5.Font = System.Drawing.Font("Tahoma", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(40, 179)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(296, 76)
		self._label5.TabIndex = 4
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Yellow
		self._button1.Font = System.Drawing.Font("Tahoma", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(40, 275)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(86, 52)
		self._button1.TabIndex = 5
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Yellow
		self._button2.Font = System.Drawing.Font("Tahoma", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(148, 275)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(86, 52)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Yellow
		self._button3.Font = System.Drawing.Font("Tahoma", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(250, 275)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(86, 52)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LightGreen
		self._textBox1.Font = System.Drawing.Font("Tahoma", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.SystemColors.ControlText
		self._textBox1.Location = System.Drawing.Point(178, 32)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(158, 27)
		self._textBox1.TabIndex = 8
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.LightGreen
		self._textBox2.Font = System.Drawing.Font("Tahoma", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.SystemColors.ControlText
		self._textBox2.Location = System.Drawing.Point(178, 68)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(158, 27)
		self._textBox2.TabIndex = 9
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.LightGreen
		self._textBox3.Font = System.Drawing.Font("Tahoma", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.ForeColor = System.Drawing.SystemColors.ControlText
		self._textBox3.Location = System.Drawing.Point(178, 107)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(158, 27)
		self._textBox3.TabIndex = 10
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.Color.LightGreen
		self._textBox4.Font = System.Drawing.Font("Tahoma", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.ForeColor = System.Drawing.SystemColors.ControlText
		self._textBox4.Location = System.Drawing.Point(178, 141)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(158, 27)
		self._textBox4.TabIndex = 11
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.ForestGreen
		self.ClientSize = System.Drawing.Size(377, 352)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog54b"
		self.ResumeLayout(False)
		self.PerformLayout()




	def Button1Click(self, sender, e):
		A = self._TextBox1.Text
		B = self._TextBox2.Text
		C = self._TextBox3.Text
		D = self._TextBox1.Text
		Sum = A + B + C + D
		Avg = Sum / 4
		self._Label5.Text = "Sum = " + Sum + "Average = " + Avg 

	def Button2Click(self, sender, e):
		self._TextBox1.Text = ""
		self._TextBox2.Text = ""
		self._TextBox3.Text = ""
		self._TextBox4.Text = ""
		self._label1.Text   = ""

	def Button3Click(self, sender, e):
		Application.Exit()