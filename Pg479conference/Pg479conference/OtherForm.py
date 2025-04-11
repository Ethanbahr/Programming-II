import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class OtherForm(Form):
	def __init__(self):
		self.InitializeComponent()
#		self.myparent = parent
		"""parent - might help later"""
	
	def InitializeComponent(self):
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.HotPink
		self._button3.Font = System.Drawing.Font("Times New Roman", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Teal
		self._button3.Location = System.Drawing.Point(180, 196)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(115, 60)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.HotPink
		self._button2.Font = System.Drawing.Font("Times New Roman", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Teal
		self._button2.Location = System.Drawing.Point(49, 196)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(115, 60)
		self._button2.TabIndex = 7
		self._button2.Text = "Reset"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# checkBox1
		# 
		self._checkBox1.BackColor = System.Drawing.Color.Gold
		self._checkBox1.Font = System.Drawing.Font("Times New Roman", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox1.Location = System.Drawing.Point(12, 50)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(115, 52)
		self._checkBox1.TabIndex = 9
		self._checkBox1.Text = "Conference Registration"
		self._checkBox1.UseVisualStyleBackColor = False
		# 
		# checkBox2
		# 
		self._checkBox2.BackColor = System.Drawing.Color.Gold
		self._checkBox2.Font = System.Drawing.Font("Times New Roman", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox2.Location = System.Drawing.Point(12, 108)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(115, 82)
		self._checkBox2.TabIndex = 10
		self._checkBox2.Text = "Opening Night Dinner and Keynote Speaker"
		self._checkBox2.UseVisualStyleBackColor = False
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["Introduction to E-commerce",
			"The Future of the Web",
			"Advanced Visual Basic",
			"Network Security"]))
		self._comboBox1.Location = System.Drawing.Point(170, 50)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(131, 21)
		self._comboBox1.TabIndex = 11
		self._comboBox1.Text = "Select One Option"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Khaki
		self._label2.Font = System.Drawing.Font("Times New Roman", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Blue
		self._label2.Location = System.Drawing.Point(12, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(152, 28)
		self._label2.TabIndex = 12
		self._label2.Text = "Conference options:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Khaki
		self._label1.Font = System.Drawing.Font("Times New Roman", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Blue
		self._label1.Location = System.Drawing.Point(197, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(98, 28)
		self._label1.TabIndex = 13
		self._label1.Text = "Workshops:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# OtherForm
		# 
		self.BackColor = System.Drawing.Color.Olive
		self.ClientSize = System.Drawing.Size(327, 268)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Name = "OtherForm"
		self.Text = "OtherForm"
		self.FormClosing += self.OtherFormFormClosing
		self.ResumeLayout(False)



	def Button2Click(self, sender, e):
		self._checkBox1.Checked = False()
		self._checkBox1.Checked = False()
		self._comboBox1.Text 	= ""
	
	def Button3Click(self, sender, e):
		MainForm = MainForm()
		MainForm.Show()
#		self.myparent.Show()
		self.Hide()
	
	def OtherFormFormClosing(self, sender, e):
		MainForm = MainForm()
		MainForm.Show()