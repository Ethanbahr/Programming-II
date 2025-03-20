import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._labelTot = System.Windows.Forms.Label()
		self._button4 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._gbColors = System.Windows.Forms.GroupBox()
		self._rbcGreen = System.Windows.Forms.RadioButton()
		self._rbcRed = System.Windows.Forms.RadioButton()
		self._rbcTeal = System.Windows.Forms.RadioButton()
		self._rbcBlue = System.Windows.Forms.RadioButton()
		self._rbcNat = System.Windows.Forms.RadioButton()
		self._gbSizes = System.Windows.Forms.GroupBox()
		self._rbsi40 = System.Windows.Forms.RadioButton()
		self._rbsi32 = System.Windows.Forms.RadioButton()
		self._rbsi27 = System.Windows.Forms.RadioButton()
		self._rbsi25 = System.Windows.Forms.RadioButton()
		self._gbShades = System.Windows.Forms.GroupBox()
		self._TSK = System.Windows.Forms.RadioButton()
		self._TDOG = System.Windows.Forms.RadioButton()
		self._TMT = System.Windows.Forms.RadioButton()
		self._gbColors.SuspendLayout()
		self._gbSizes.SuspendLayout()
		self._gbShades.SuspendLayout()
		self.SuspendLayout()
		# 
		# labelTot
		# 
		self._labelTot.BackColor = System.Drawing.Color.MintCream
		self._labelTot.Font = System.Drawing.Font("Tempus Sans ITC", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._labelTot.ForeColor = System.Drawing.Color.DodgerBlue
		self._labelTot.Location = System.Drawing.Point(461, 254)
		self._labelTot.Name = "labelTot"
		self._labelTot.Size = System.Drawing.Size(201, 37)
		self._labelTot.TabIndex = 15
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.MintCream
		self._button4.Font = System.Drawing.Font("Tempus Sans ITC", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.ForeColor = System.Drawing.Color.DodgerBlue
		self._button4.Location = System.Drawing.Point(562, 355)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(94, 49)
		self._button4.TabIndex = 14
		self._button4.Text = "Exit"
		self._button4.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.MintCream
		self._button3.Font = System.Drawing.Font("Tempus Sans ITC", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.DodgerBlue
		self._button3.Location = System.Drawing.Point(463, 355)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(93, 49)
		self._button3.TabIndex = 13
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = False
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.MintCream
		self._button2.Font = System.Drawing.Font("Tempus Sans ITC", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.DodgerBlue
		self._button2.Location = System.Drawing.Point(461, 300)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(201, 49)
		self._button2.TabIndex = 12
		self._button2.Text = "Calculate"
		self._button2.UseVisualStyleBackColor = False
		# 
		# gbColors
		# 
		self._gbColors.BackColor = System.Drawing.Color.Transparent
		self._gbColors.Controls.Add(self._rbcGreen)
		self._gbColors.Controls.Add(self._rbcRed)
		self._gbColors.Controls.Add(self._rbcTeal)
		self._gbColors.Controls.Add(self._rbcBlue)
		self._gbColors.Controls.Add(self._rbcNat)
		self._gbColors.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._gbColors.ForeColor = System.Drawing.Color.DarkBlue
		self._gbColors.Location = System.Drawing.Point(12, 183)
		self._gbColors.Name = "gbColors"
		self._gbColors.Size = System.Drawing.Size(201, 235)
		self._gbColors.TabIndex = 11
		self._gbColors.TabStop = False
		self._gbColors.Text = "Colors"
		# 
		# rbcGreen
		# 
		self._rbcGreen.BackColor = System.Drawing.Color.MintCream
		self._rbcGreen.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbcGreen.Location = System.Drawing.Point(6, 193)
		self._rbcGreen.Name = "rbcGreen"
		self._rbcGreen.Size = System.Drawing.Size(189, 36)
		self._rbcGreen.TabIndex = 4
		self._rbcGreen.TabStop = True
		self._rbcGreen.UseVisualStyleBackColor = False
		# 
		# rbcRed
		# 
		self._rbcRed.BackColor = System.Drawing.Color.MintCream
		self._rbcRed.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbcRed.Location = System.Drawing.Point(6, 154)
		self._rbcRed.Name = "rbcRed"
		self._rbcRed.Size = System.Drawing.Size(189, 36)
		self._rbcRed.TabIndex = 3
		self._rbcRed.TabStop = True
		self._rbcRed.UseVisualStyleBackColor = False
		# 
		# rbcTeal
		# 
		self._rbcTeal.BackColor = System.Drawing.Color.MintCream
		self._rbcTeal.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbcTeal.Location = System.Drawing.Point(6, 114)
		self._rbcTeal.Name = "rbcTeal"
		self._rbcTeal.Size = System.Drawing.Size(189, 34)
		self._rbcTeal.TabIndex = 2
		self._rbcTeal.TabStop = True
		self._rbcTeal.UseVisualStyleBackColor = False
		# 
		# rbcBlue
		# 
		self._rbcBlue.BackColor = System.Drawing.Color.MintCream
		self._rbcBlue.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbcBlue.Location = System.Drawing.Point(6, 73)
		self._rbcBlue.Name = "rbcBlue"
		self._rbcBlue.Size = System.Drawing.Size(189, 35)
		self._rbcBlue.TabIndex = 1
		self._rbcBlue.TabStop = True
		self._rbcBlue.UseVisualStyleBackColor = False
		# 
		# rbcNat
		# 
		self._rbcNat.BackColor = System.Drawing.Color.MintCream
		self._rbcNat.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbcNat.Location = System.Drawing.Point(6, 29)
		self._rbcNat.Name = "rbcNat"
		self._rbcNat.Size = System.Drawing.Size(189, 38)
		self._rbcNat.TabIndex = 0
		self._rbcNat.TabStop = True
		self._rbcNat.UseVisualStyleBackColor = False
		# 
		# gbSizes
		# 
		self._gbSizes.BackColor = System.Drawing.Color.Transparent
		self._gbSizes.Controls.Add(self._rbsi40)
		self._gbSizes.Controls.Add(self._rbsi32)
		self._gbSizes.Controls.Add(self._rbsi27)
		self._gbSizes.Controls.Add(self._rbsi25)
		self._gbSizes.Font = System.Drawing.Font("Tempus Sans ITC", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._gbSizes.ForeColor = System.Drawing.Color.Navy
		self._gbSizes.Location = System.Drawing.Point(225, 5)
		self._gbSizes.Name = "gbSizes"
		self._gbSizes.Size = System.Drawing.Size(201, 201)
		self._gbSizes.TabIndex = 10
		self._gbSizes.TabStop = False
		self._gbSizes.Text = "Sizes"
		# 
		# rbsi40
		# 
		self._rbsi40.BackColor = System.Drawing.Color.MintCream
		self._rbsi40.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbsi40.Location = System.Drawing.Point(6, 154)
		self._rbsi40.Name = "rbsi40"
		self._rbsi40.Size = System.Drawing.Size(189, 36)
		self._rbsi40.TabIndex = 3
		self._rbsi40.TabStop = True
		self._rbsi40.UseVisualStyleBackColor = False
		# 
		# rbsi32
		# 
		self._rbsi32.BackColor = System.Drawing.Color.MintCream
		self._rbsi32.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbsi32.Location = System.Drawing.Point(6, 114)
		self._rbsi32.Name = "rbsi32"
		self._rbsi32.Size = System.Drawing.Size(189, 36)
		self._rbsi32.TabIndex = 2
		self._rbsi32.TabStop = True
		self._rbsi32.UseVisualStyleBackColor = False
		# 
		# rbsi27
		# 
		self._rbsi27.BackColor = System.Drawing.Color.MintCream
		self._rbsi27.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbsi27.Location = System.Drawing.Point(6, 73)
		self._rbsi27.Name = "rbsi27"
		self._rbsi27.Size = System.Drawing.Size(189, 34)
		self._rbsi27.TabIndex = 1
		self._rbsi27.TabStop = True
		self._rbsi27.UseVisualStyleBackColor = False
		# 
		# rbsi25
		# 
		self._rbsi25.BackColor = System.Drawing.Color.MintCream
		self._rbsi25.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbsi25.Location = System.Drawing.Point(6, 29)
		self._rbsi25.Name = "rbsi25"
		self._rbsi25.Size = System.Drawing.Size(189, 38)
		self._rbsi25.TabIndex = 0
		self._rbsi25.TabStop = True
		self._rbsi25.UseVisualStyleBackColor = False
		# 
		# gbShades
		# 
		self._gbShades.BackColor = System.Drawing.Color.Transparent
		self._gbShades.Controls.Add(self._TSK)
		self._gbShades.Controls.Add(self._TDOG)
		self._gbShades.Controls.Add(self._TMT)
		self._gbShades.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._gbShades.ForeColor = System.Drawing.Color.Navy
		self._gbShades.Location = System.Drawing.Point(12, 5)
		self._gbShades.Name = "gbShades"
		self._gbShades.Size = System.Drawing.Size(207, 165)
		self._gbShades.TabIndex = 9
		self._gbShades.TabStop = False
		self._gbShades.Text = "Styles"
		# 
		# TSK
		# 
		self._TSK.BackColor = System.Drawing.Color.MintCream
		self._TSK.ForeColor = System.Drawing.Color.DodgerBlue
		self._TSK.Location = System.Drawing.Point(6, 114)
		self._TSK.Name = "TSK"
		self._TSK.Size = System.Drawing.Size(189, 36)
		self._TSK.TabIndex = 2
		self._TSK.TabStop = True
		self._TSK.Text = "The Street King"
		self._TSK.UseVisualStyleBackColor = False
		# 
		# TDOG
		# 
		self._TDOG.BackColor = System.Drawing.Color.MintCream
		self._TDOG.ForeColor = System.Drawing.Color.DodgerBlue
		self._TDOG.Location = System.Drawing.Point(6, 74)
		self._TDOG.Name = "TDOG"
		self._TDOG.Size = System.Drawing.Size(189, 34)
		self._TDOG.TabIndex = 1
		self._TDOG.TabStop = True
		self._TDOG.Text = "The Dictator of Grind"
		self._TDOG.UseVisualStyleBackColor = False
		# 
		# TMT
		# 
		self._TMT.BackColor = System.Drawing.Color.MintCream
		self._TMT.ForeColor = System.Drawing.Color.DodgerBlue
		self._TMT.Location = System.Drawing.Point(6, 29)
		self._TMT.Name = "TMT"
		self._TMT.Size = System.Drawing.Size(189, 38)
		self._TMT.TabIndex = 0
		self._TMT.TabStop = True
		self._TMT.Text = "The Master Thrasher"
		self._TMT.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SteelBlue
		self.ClientSize = System.Drawing.Size(674, 430)
		self.Controls.Add(self._labelTot)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._gbColors)
		self.Controls.Add(self._gbSizes)
		self.Controls.Add(self._gbShades)
		self.Name = "MainForm"
		self.Text = "Pg485skate"
		self.Load += self.MainFormLoad
		self._gbColors.ResumeLayout(False)
		self._gbSizes.ResumeLayout(False)
		self._gbShades.ResumeLayout(False)
		self.ResumeLayout(False)

# !!!!!!!!!! TODO: !!!!!!!!!!
# Fix names
# Write code