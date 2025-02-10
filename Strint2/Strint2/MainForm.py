import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Red
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(228, 129)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(113, 55)
		self._button2.TabIndex = 11
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Red
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(77, 129)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(113, 55)
		self._button1.TabIndex = 10
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Salmon
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(158, 45)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(255, 31)
		self._textBox1.TabIndex = 9
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Salmon
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(158, 82)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(255, 34)
		self._label3.TabIndex = 8
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Tomato
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(6, 82)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(146, 34)
		self._label2.TabIndex = 7
		self._label2.Text = "Anagrams?"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Tomato
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(6, 45)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(146, 34)
		self._label1.TabIndex = 6
		self._label1.Text = "Enter word 2:"
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Salmon
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.White
		self._textBox2.Location = System.Drawing.Point(158, 11)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(255, 31)
		self._textBox2.TabIndex = 13
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Tomato
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(6, 8)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(146, 34)
		self._label4.TabIndex = 12
		self._label4.Text = "Enter word 1:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(433, 196)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Strint2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label3.Text = ""
		word1 = self._textBox2.Text.lower()
		word2 = self._textBox1.Text.lower()
		if len(word1) != len(word2):
			self._label3.Text = "False"
			return
		else:
			for lcv in range(len(word1)):
				c 	  = word[lcv]
				index = word2.find(c)
				if index == -1:
					self._label3.Text = "False"
				else:
					word2 = word2[0:index] + word2[index+1:]
		self._label.Text = str(len(word2) == 0)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label3.Text   = ""