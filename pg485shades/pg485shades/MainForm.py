import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._gbShades = System.Windows.Forms.GroupBox()
		self._rbsReg = System.Windows.Forms.RadioButton()
		self._rbsFold = System.Windows.Forms.RadioButton()
		self._rbsRome = System.Windows.Forms.RadioButton()
		self._gbSizes = System.Windows.Forms.GroupBox()
		self._rbsi32 = System.Windows.Forms.RadioButton()
		self._rbsi27 = System.Windows.Forms.RadioButton()
		self._rbsi25 = System.Windows.Forms.RadioButton()
		self._rbsi40 = System.Windows.Forms.RadioButton()
		self._gbColors = System.Windows.Forms.GroupBox()
		self._rbcRed = System.Windows.Forms.RadioButton()
		self._rbcTeal = System.Windows.Forms.RadioButton()
		self._rbcBlue = System.Windows.Forms.RadioButton()
		self._rbcNat = System.Windows.Forms.RadioButton()
		self._rbcGreen = System.Windows.Forms.RadioButton()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._gbShades.SuspendLayout()
		self._gbSizes.SuspendLayout()
		self._gbColors.SuspendLayout()
		self.SuspendLayout()
		# 
		# gbShades
		# 
		self._gbShades.BackColor = System.Drawing.Color.SpringGreen
		self._gbShades.Controls.Add(self._rbsRome)
		self._gbShades.Controls.Add(self._rbsFold)
		self._gbShades.Controls.Add(self._rbsReg)
		self._gbShades.Font = System.Drawing.Font("Tahoma", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._gbShades.Location = System.Drawing.Point(12, 12)
		self._gbShades.Name = "gbShades"
		self._gbShades.Size = System.Drawing.Size(201, 165)
		self._gbShades.TabIndex = 0
		self._gbShades.TabStop = False
		self._gbShades.Text = "Styles"
		# 
		# rbsReg
		# 
		self._rbsReg.BackColor = System.Drawing.Color.MintCream
		self._rbsReg.Location = System.Drawing.Point(6, 29)
		self._rbsReg.Name = "rbsReg"
		self._rbsReg.Size = System.Drawing.Size(189, 38)
		self._rbsReg.TabIndex = 0
		self._rbsReg.TabStop = True
		self._rbsReg.Text = "Regular (+$0)"
		self._rbsReg.UseVisualStyleBackColor = False
		# 
		# rbsFold
		# 
		self._rbsFold.BackColor = System.Drawing.Color.MintCream
		self._rbsFold.Location = System.Drawing.Point(6, 74)
		self._rbsFold.Name = "rbsFold"
		self._rbsFold.Size = System.Drawing.Size(189, 34)
		self._rbsFold.TabIndex = 1
		self._rbsFold.TabStop = True
		self._rbsFold.Text = "Folding (+$10)"
		self._rbsFold.UseVisualStyleBackColor = False
		# 
		# rbsRome
		# 
		self._rbsRome.BackColor = System.Drawing.Color.MintCream
		self._rbsRome.Location = System.Drawing.Point(6, 114)
		self._rbsRome.Name = "rbsRome"
		self._rbsRome.Size = System.Drawing.Size(189, 36)
		self._rbsRome.TabIndex = 2
		self._rbsRome.TabStop = True
		self._rbsRome.Text = "Roman (+$15)"
		self._rbsRome.UseVisualStyleBackColor = False
		# 
		# gbSizes
		# 
		self._gbSizes.BackColor = System.Drawing.Color.SpringGreen
		self._gbSizes.Controls.Add(self._rbsi40)
		self._gbSizes.Controls.Add(self._rbsi32)
		self._gbSizes.Controls.Add(self._rbsi27)
		self._gbSizes.Controls.Add(self._rbsi25)
		self._gbSizes.Font = System.Drawing.Font("Tahoma", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._gbSizes.Location = System.Drawing.Point(238, 12)
		self._gbSizes.Name = "gbSizes"
		self._gbSizes.Size = System.Drawing.Size(201, 201)
		self._gbSizes.TabIndex = 3
		self._gbSizes.TabStop = False
		self._gbSizes.Text = "Sizes"
		# 
		# rbsi32
		# 
		self._rbsi32.BackColor = System.Drawing.Color.MintCream
		self._rbsi32.Location = System.Drawing.Point(6, 114)
		self._rbsi32.Name = "rbsi32"
		self._rbsi32.Size = System.Drawing.Size(189, 36)
		self._rbsi32.TabIndex = 2
		self._rbsi32.TabStop = True
		self._rbsi32.Text = "32 in. (+$4)"
		self._rbsi32.UseVisualStyleBackColor = False
		# 
		# rbsi27
		# 
		self._rbsi27.BackColor = System.Drawing.Color.MintCream
		self._rbsi27.Location = System.Drawing.Point(6, 73)
		self._rbsi27.Name = "rbsi27"
		self._rbsi27.Size = System.Drawing.Size(189, 34)
		self._rbsi27.TabIndex = 1
		self._rbsi27.TabStop = True
		self._rbsi27.Text = "27 in. (+$2)"
		self._rbsi27.UseVisualStyleBackColor = False
		# 
		# rbsi25
		# 
		self._rbsi25.BackColor = System.Drawing.Color.MintCream
		self._rbsi25.Location = System.Drawing.Point(6, 29)
		self._rbsi25.Name = "rbsi25"
		self._rbsi25.Size = System.Drawing.Size(189, 38)
		self._rbsi25.TabIndex = 0
		self._rbsi25.TabStop = True
		self._rbsi25.Text = "25 in. (+$0)"
		self._rbsi25.UseVisualStyleBackColor = False
		# 
		# rbsi40
		# 
		self._rbsi40.BackColor = System.Drawing.Color.MintCream
		self._rbsi40.Location = System.Drawing.Point(6, 154)
		self._rbsi40.Name = "rbsi40"
		self._rbsi40.Size = System.Drawing.Size(189, 36)
		self._rbsi40.TabIndex = 3
		self._rbsi40.TabStop = True
		self._rbsi40.Text = "40 in. (+$6)"
		self._rbsi40.UseVisualStyleBackColor = False
		# 
		# gbColors
		# 
		self._gbColors.BackColor = System.Drawing.Color.SpringGreen
		self._gbColors.Controls.Add(self._button1)
		self._gbColors.Controls.Add(self._rbcGreen)
		self._gbColors.Controls.Add(self._rbcRed)
		self._gbColors.Controls.Add(self._rbcTeal)
		self._gbColors.Controls.Add(self._rbcBlue)
		self._gbColors.Controls.Add(self._rbcNat)
		self._gbColors.Font = System.Drawing.Font("Tahoma", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._gbColors.Location = System.Drawing.Point(12, 183)
		self._gbColors.Name = "gbColors"
		self._gbColors.Size = System.Drawing.Size(201, 235)
		self._gbColors.TabIndex = 4
		self._gbColors.TabStop = False
		self._gbColors.Text = "Colors"
		# 
		# rbcRed
		# 
		self._rbcRed.BackColor = System.Drawing.Color.MintCream
		self._rbcRed.Location = System.Drawing.Point(6, 154)
		self._rbcRed.Name = "rbcRed"
		self._rbcRed.Size = System.Drawing.Size(189, 36)
		self._rbcRed.TabIndex = 3
		self._rbcRed.TabStop = True
		self._rbcRed.Text = "Red (+$0)"
		self._rbcRed.UseVisualStyleBackColor = False
		# 
		# rbcTeal
		# 
		self._rbcTeal.BackColor = System.Drawing.Color.MintCream
		self._rbcTeal.Location = System.Drawing.Point(6, 114)
		self._rbcTeal.Name = "rbcTeal"
		self._rbcTeal.Size = System.Drawing.Size(189, 34)
		self._rbcTeal.TabIndex = 2
		self._rbcTeal.TabStop = True
		self._rbcTeal.Text = "Teal (+$0)"
		self._rbcTeal.UseVisualStyleBackColor = False
		# 
		# rbcBlue
		# 
		self._rbcBlue.BackColor = System.Drawing.Color.MintCream
		self._rbcBlue.Location = System.Drawing.Point(6, 73)
		self._rbcBlue.Name = "rbcBlue"
		self._rbcBlue.Size = System.Drawing.Size(189, 35)
		self._rbcBlue.TabIndex = 1
		self._rbcBlue.TabStop = True
		self._rbcBlue.Text = "Blue (+$0)"
		self._rbcBlue.UseVisualStyleBackColor = False
		# 
		# rbcNat
		# 
		self._rbcNat.BackColor = System.Drawing.Color.MintCream
		self._rbcNat.Location = System.Drawing.Point(6, 29)
		self._rbcNat.Name = "rbcNat"
		self._rbcNat.Size = System.Drawing.Size(189, 38)
		self._rbcNat.TabIndex = 0
		self._rbcNat.TabStop = True
		self._rbcNat.Text = "Natural (+$5)"
		self._rbcNat.UseVisualStyleBackColor = False
		# 
		# rbcGreen
		# 
		self._rbcGreen.BackColor = System.Drawing.Color.MintCream
		self._rbcGreen.Location = System.Drawing.Point(6, 193)
		self._rbcGreen.Name = "rbcGreen"
		self._rbcGreen.Size = System.Drawing.Size(189, 36)
		self._rbcGreen.TabIndex = 4
		self._rbcGreen.TabStop = True
		self._rbcGreen.Text = "Green (+$0)"
		self._rbcGreen.UseVisualStyleBackColor = False
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(90, 26)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(8, 8)
		self._button1.TabIndex = 5
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.MintCream
		self._button2.Font = System.Drawing.Font("Tahoma", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(264, 242)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(140, 49)
		self._button2.TabIndex = 5
		self._button2.Text = "Calculate"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.MintCream
		self._button3.Font = System.Drawing.Font("Tahoma", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(264, 297)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(140, 49)
		self._button3.TabIndex = 6
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = False
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.MintCream
		self._button4.Font = System.Drawing.Font("Tahoma", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(264, 352)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(140, 49)
		self._button4.TabIndex = 7
		self._button4.Text = "Exit"
		self._button4.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MediumSeaGreen
		self.ClientSize = System.Drawing.Size(451, 443)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._gbColors)
		self.Controls.Add(self._gbSizes)
		self.Controls.Add(self._gbShades)
		self.Name = "MainForm"
		self.Text = "pg485shades"
		self._gbShades.ResumeLayout(False)
		self._gbSizes.ResumeLayout(False)
		self._gbColors.ResumeLayout(False)
		self.ResumeLayout(False)
