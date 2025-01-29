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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Maroon
		self._label1.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Red
		self._label1.Location = System.Drawing.Point(12, 28)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(109, 34)
		self._label1.TabIndex = 0
		self._label1.Text = "Radius:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Maroon
		self._label2.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Red
		self._label2.Location = System.Drawing.Point(12, 78)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(109, 34)
		self._label2.TabIndex = 1
		self._label2.Text = "Area:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Maroon
		self._label3.Font = System.Drawing.Font("Mongolian Baiti", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Red
		self._label3.Location = System.Drawing.Point(12, 128)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(109, 34)
		self._label3.TabIndex = 2
		self._label3.Text = "Circumference:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Salmon
		self._label4.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.CornflowerBlue
		self._label4.Location = System.Drawing.Point(156, 78)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(153, 34)
		self._label4.TabIndex = 3
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DarkSalmon
		self._textBox1.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.CornflowerBlue
		self._textBox1.Location = System.Drawing.Point(156, 33)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(153, 29)
		self._textBox1.TabIndex = 4
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Salmon
		self._label5.Font = System.Drawing.Font("Mongolian Baiti", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.CornflowerBlue
		self._label5.Location = System.Drawing.Point(156, 128)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(153, 34)
		self._label5.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Coral
		self._button1.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.SaddleBrown
		self._button1.Location = System.Drawing.Point(12, 179)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(95, 63)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Coral
		self._button2.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.SaddleBrown
		self._button2.Location = System.Drawing.Point(113, 179)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(95, 63)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Coral
		self._button3.Font = System.Drawing.Font("Mongolian Baiti", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.SaddleBrown
		self._button3.Location = System.Drawing.Point(214, 179)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(95, 63)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Tomato
		self.ClientSize = System.Drawing.Size(328, 254)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Radius = self._textBox1.Text
#		Circ = 2 * 3.14159

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label4.Text   = ""
		self._label5.Text   = ""

	def Button3Click(self, sender, e):
		Application.Exit()