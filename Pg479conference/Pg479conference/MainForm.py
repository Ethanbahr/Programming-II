import System.Drawing
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
		self._button4 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._textBox7 = System.Windows.Forms.TextBox()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.HotPink
		self._button1.Font = System.Drawing.Font("Times New Roman", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Teal
		self._button1.Location = System.Drawing.Point(12, 196)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(115, 91)
		self._button1.TabIndex = 0
		self._button1.Text = "Select Conference Options"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.HotPink
		self._button2.Font = System.Drawing.Font("Times New Roman", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Teal
		self._button2.Location = System.Drawing.Point(133, 227)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(115, 60)
		self._button2.TabIndex = 1
		self._button2.Text = "Reset"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.HotPink
		self._button3.Font = System.Drawing.Font("Times New Roman", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Teal
		self._button3.Location = System.Drawing.Point(254, 227)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(115, 60)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.HotPink
		self._button4.Font = System.Drawing.Font("Times New Roman", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.ForeColor = System.Drawing.Color.Teal
		self._button4.Location = System.Drawing.Point(254, 188)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(115, 43)
		self._button4.TabIndex = 3
		self._button4.Text = "Calculate"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Gold
		self._label1.Font = System.Drawing.Font("Times New Roman", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Blue
		self._label1.Location = System.Drawing.Point(133, 196)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(115, 28)
		self._label1.TabIndex = 4
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.Gold
		self._groupBox1.Controls.Add(self._textBox7)
		self._groupBox1.Controls.Add(self._textBox6)
		self._groupBox1.Controls.Add(self._textBox5)
		self._groupBox1.Controls.Add(self._textBox4)
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label8)
		self._groupBox1.Controls.Add(self._label7)
		self._groupBox1.Controls.Add(self._label6)
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Font = System.Drawing.Font("Times New Roman", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(354, 173)
		self._groupBox1.TabIndex = 5
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Registrant"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Khaki
		self._label2.Font = System.Drawing.Font("Times New Roman", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Blue
		self._label2.Location = System.Drawing.Point(6, 25)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(71, 28)
		self._label2.TabIndex = 6
		self._label2.Text = "Name:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Khaki
		self._label3.Font = System.Drawing.Font("Times New Roman", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Blue
		self._label3.Location = System.Drawing.Point(6, 56)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(95, 28)
		self._label3.TabIndex = 7
		self._label3.Text = "Company:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Khaki
		self._label4.Font = System.Drawing.Font("Times New Roman", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.Blue
		self._label4.Location = System.Drawing.Point(6, 114)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(95, 28)
		self._label4.TabIndex = 8
		self._label4.Text = "Address:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Khaki
		self._label5.Font = System.Drawing.Font("Times New Roman", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.Blue
		self._label5.Location = System.Drawing.Point(187, 62)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(49, 28)
		self._label5.TabIndex = 9
		self._label5.Text = "City:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Khaki
		self._label6.Font = System.Drawing.Font("Times New Roman", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.Blue
		self._label6.Location = System.Drawing.Point(169, 25)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(67, 28)
		self._label6.TabIndex = 10
		self._label6.Text = "Phone:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Khaki
		self._label7.Font = System.Drawing.Font("Times New Roman", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.Blue
		self._label7.Location = System.Drawing.Point(169, 99)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(67, 28)
		self._label7.TabIndex = 11
		self._label7.Text = "State:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Khaki
		self._label8.Font = System.Drawing.Font("Times New Roman", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.Blue
		self._label8.Location = System.Drawing.Point(187, 131)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(49, 28)
		self._label8.TabIndex = 12
		self._label8.Text = "Zip:"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Times New Roman", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(83, 30)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(80, 22)
		self._textBox1.TabIndex = 13
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Times New Roman", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(6, 89)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(133, 22)
		self._textBox2.TabIndex = 14
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Times New Roman", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(6, 145)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(133, 22)
		self._textBox3.TabIndex = 15
		# 
		# textBox4
		# 
		self._textBox4.Font = System.Drawing.Font("Times New Roman", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.Location = System.Drawing.Point(242, 25)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(96, 22)
		self._textBox4.TabIndex = 16
		# 
		# textBox5
		# 
		self._textBox5.Font = System.Drawing.Font("Times New Roman", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox5.Location = System.Drawing.Point(242, 62)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(96, 22)
		self._textBox5.TabIndex = 17
		# 
		# textBox6
		# 
		self._textBox6.Font = System.Drawing.Font("Times New Roman", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox6.Location = System.Drawing.Point(242, 105)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(96, 22)
		self._textBox6.TabIndex = 18
		# 
		# textBox7
		# 
		self._textBox7.Font = System.Drawing.Font("Times New Roman", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox7.Location = System.Drawing.Point(242, 137)
		self._textBox7.Name = "textBox7"
		self._textBox7.Size = System.Drawing.Size(96, 22)
		self._textBox7.TabIndex = 19
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Olive
		self.ClientSize = System.Drawing.Size(378, 299)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg479conference"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from OtherForm import *		
		OtherForm = OtherForm()
		OtherForm.Show()
		self.Hide()

	def Button2Click(self, sender, e):
		pass
	
	def Button4Click(self, sender, e):
		from OtherForm import *
		tot  = 0
		
		self._label1.Text = "Total: $" + str(tot)
	
	def Button3Click(self, sender, e):
		Application.Exit()

