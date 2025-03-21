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
		self._gbMisc = System.Windows.Forms.GroupBox()
		self._gbWS = System.Windows.Forms.GroupBox()
		self._si61 = System.Windows.Forms.RadioButton()
		self._si58 = System.Windows.Forms.RadioButton()
		self._si55 = System.Windows.Forms.RadioButton()
		self._si51 = System.Windows.Forms.RadioButton()
		self._gbStyles = System.Windows.Forms.GroupBox()
		self._TSK = System.Windows.Forms.RadioButton()
		self._TDOG = System.Windows.Forms.RadioButton()
		self._TMT = System.Windows.Forms.RadioButton()
		self._labelSubTot = System.Windows.Forms.Label()
		self._gbTruck = System.Windows.Forms.GroupBox()
		self._ax85 = System.Windows.Forms.RadioButton()
		self._ax8 = System.Windows.Forms.RadioButton()
		self._ax775 = System.Windows.Forms.RadioButton()
		self._GT = System.Windows.Forms.CheckBox()
		self._BEAR = System.Windows.Forms.CheckBox()
		self._RISER = System.Windows.Forms.CheckBox()
		self._NUTS = System.Windows.Forms.CheckBox()
		self._ASMBL = System.Windows.Forms.CheckBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._gbMisc.SuspendLayout()
		self._gbWS.SuspendLayout()
		self._gbStyles.SuspendLayout()
		self._gbTruck.SuspendLayout()
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
		self._button4.Location = System.Drawing.Point(568, 355)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(94, 49)
		self._button4.TabIndex = 14
		self._button4.Text = "Exit"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.MintCream
		self._button3.Font = System.Drawing.Font("Tempus Sans ITC", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.DodgerBlue
		self._button3.Location = System.Drawing.Point(461, 355)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(93, 49)
		self._button3.TabIndex = 13
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
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
		self._button2.Click += self.Button2Click
		# 
		# gbMisc
		# 
		self._gbMisc.BackColor = System.Drawing.Color.Transparent
		self._gbMisc.Controls.Add(self._ASMBL)
		self._gbMisc.Controls.Add(self._NUTS)
		self._gbMisc.Controls.Add(self._RISER)
		self._gbMisc.Controls.Add(self._BEAR)
		self._gbMisc.Controls.Add(self._GT)
		self._gbMisc.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._gbMisc.ForeColor = System.Drawing.Color.DarkBlue
		self._gbMisc.Location = System.Drawing.Point(12, 183)
		self._gbMisc.Name = "gbMisc"
		self._gbMisc.Size = System.Drawing.Size(201, 221)
		self._gbMisc.TabIndex = 11
		self._gbMisc.TabStop = False
		self._gbMisc.Text = "Misc"
		# 
		# gbWS
		# 
		self._gbWS.BackColor = System.Drawing.Color.Transparent
		self._gbWS.Controls.Add(self._si61)
		self._gbWS.Controls.Add(self._si58)
		self._gbWS.Controls.Add(self._si55)
		self._gbWS.Controls.Add(self._si51)
		self._gbWS.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._gbWS.ForeColor = System.Drawing.Color.Navy
		self._gbWS.Location = System.Drawing.Point(225, 5)
		self._gbWS.Name = "gbWS"
		self._gbWS.Size = System.Drawing.Size(201, 208)
		self._gbWS.TabIndex = 10
		self._gbWS.TabStop = False
		self._gbWS.Text = "Wheel sets"
		# 
		# si61
		# 
		self._si61.BackColor = System.Drawing.Color.MintCream
		self._si61.ForeColor = System.Drawing.Color.DodgerBlue
		self._si61.Location = System.Drawing.Point(6, 154)
		self._si61.Name = "si61"
		self._si61.Size = System.Drawing.Size(189, 36)
		self._si61.TabIndex = 3
		self._si61.TabStop = True
		self._si61.Text = "61 mm"
		self._si61.UseVisualStyleBackColor = False
		# 
		# si58
		# 
		self._si58.BackColor = System.Drawing.Color.MintCream
		self._si58.ForeColor = System.Drawing.Color.DodgerBlue
		self._si58.Location = System.Drawing.Point(6, 114)
		self._si58.Name = "si58"
		self._si58.Size = System.Drawing.Size(189, 36)
		self._si58.TabIndex = 2
		self._si58.TabStop = True
		self._si58.Text = "58 mm"
		self._si58.UseVisualStyleBackColor = False
		# 
		# si55
		# 
		self._si55.BackColor = System.Drawing.Color.MintCream
		self._si55.ForeColor = System.Drawing.Color.DodgerBlue
		self._si55.Location = System.Drawing.Point(6, 73)
		self._si55.Name = "si55"
		self._si55.Size = System.Drawing.Size(189, 34)
		self._si55.TabIndex = 1
		self._si55.TabStop = True
		self._si55.Text = "55 mm"
		self._si55.UseVisualStyleBackColor = False
		# 
		# si51
		# 
		self._si51.BackColor = System.Drawing.Color.MintCream
		self._si51.ForeColor = System.Drawing.Color.DodgerBlue
		self._si51.Location = System.Drawing.Point(6, 29)
		self._si51.Name = "si51"
		self._si51.Size = System.Drawing.Size(189, 38)
		self._si51.TabIndex = 0
		self._si51.TabStop = True
		self._si51.Text = "51 mm"
		self._si51.UseVisualStyleBackColor = False
		# 
		# gbStyles
		# 
		self._gbStyles.BackColor = System.Drawing.Color.Transparent
		self._gbStyles.Controls.Add(self._TSK)
		self._gbStyles.Controls.Add(self._TDOG)
		self._gbStyles.Controls.Add(self._TMT)
		self._gbStyles.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._gbStyles.ForeColor = System.Drawing.Color.Navy
		self._gbStyles.Location = System.Drawing.Point(12, 5)
		self._gbStyles.Name = "gbStyles"
		self._gbStyles.Size = System.Drawing.Size(207, 165)
		self._gbStyles.TabIndex = 9
		self._gbStyles.TabStop = False
		self._gbStyles.Text = "Styles"
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
		# labelSubTot
		# 
		self._labelSubTot.BackColor = System.Drawing.Color.MintCream
		self._labelSubTot.Font = System.Drawing.Font("Tempus Sans ITC", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._labelSubTot.ForeColor = System.Drawing.Color.DodgerBlue
		self._labelSubTot.Location = System.Drawing.Point(461, 212)
		self._labelSubTot.Name = "labelSubTot"
		self._labelSubTot.Size = System.Drawing.Size(201, 37)
		self._labelSubTot.TabIndex = 16
		# 
		# gbTruck
		# 
		self._gbTruck.BackColor = System.Drawing.Color.Transparent
		self._gbTruck.Controls.Add(self._ax85)
		self._gbTruck.Controls.Add(self._ax8)
		self._gbTruck.Controls.Add(self._ax775)
		self._gbTruck.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._gbTruck.ForeColor = System.Drawing.Color.Navy
		self._gbTruck.Location = System.Drawing.Point(225, 219)
		self._gbTruck.Name = "gbTruck"
		self._gbTruck.Size = System.Drawing.Size(207, 165)
		self._gbTruck.TabIndex = 10
		self._gbTruck.TabStop = False
		self._gbTruck.Text = "Truck assemblies"
		# 
		# ax85
		# 
		self._ax85.BackColor = System.Drawing.Color.MintCream
		self._ax85.ForeColor = System.Drawing.Color.DodgerBlue
		self._ax85.Location = System.Drawing.Point(6, 114)
		self._ax85.Name = "ax85"
		self._ax85.Size = System.Drawing.Size(189, 36)
		self._ax85.TabIndex = 2
		self._ax85.TabStop = True
		self._ax85.Text = "8.5 axle"
		self._ax85.UseVisualStyleBackColor = False
		# 
		# ax8
		# 
		self._ax8.BackColor = System.Drawing.Color.MintCream
		self._ax8.ForeColor = System.Drawing.Color.DodgerBlue
		self._ax8.Location = System.Drawing.Point(6, 74)
		self._ax8.Name = "ax8"
		self._ax8.Size = System.Drawing.Size(189, 34)
		self._ax8.TabIndex = 1
		self._ax8.TabStop = True
		self._ax8.Text = "8 axle"
		self._ax8.UseVisualStyleBackColor = False
		# 
		# ax775
		# 
		self._ax775.BackColor = System.Drawing.Color.MintCream
		self._ax775.ForeColor = System.Drawing.Color.DodgerBlue
		self._ax775.Location = System.Drawing.Point(6, 29)
		self._ax775.Name = "ax775"
		self._ax775.Size = System.Drawing.Size(189, 38)
		self._ax775.TabIndex = 0
		self._ax775.TabStop = True
		self._ax775.Text = "7.75 axle"
		self._ax775.UseVisualStyleBackColor = False
		# 
		# GT
		# 
		self._GT.BackColor = System.Drawing.Color.MintCream
		self._GT.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._GT.ForeColor = System.Drawing.Color.DodgerBlue
		self._GT.Location = System.Drawing.Point(6, 23)
		self._GT.Name = "GT"
		self._GT.Size = System.Drawing.Size(188, 34)
		self._GT.TabIndex = 5
		self._GT.Text = "Grip tape"
		self._GT.UseVisualStyleBackColor = False
		# 
		# BEAR
		# 
		self._BEAR.BackColor = System.Drawing.Color.MintCream
		self._BEAR.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._BEAR.ForeColor = System.Drawing.Color.DodgerBlue
		self._BEAR.Location = System.Drawing.Point(6, 63)
		self._BEAR.Name = "BEAR"
		self._BEAR.Size = System.Drawing.Size(188, 34)
		self._BEAR.TabIndex = 6
		self._BEAR.Text = "Bearings"
		self._BEAR.UseVisualStyleBackColor = False
		# 
		# RISER
		# 
		self._RISER.BackColor = System.Drawing.Color.MintCream
		self._RISER.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._RISER.ForeColor = System.Drawing.Color.DodgerBlue
		self._RISER.Location = System.Drawing.Point(6, 100)
		self._RISER.Name = "RISER"
		self._RISER.Size = System.Drawing.Size(188, 34)
		self._RISER.TabIndex = 7
		self._RISER.Text = "Riser pads"
		self._RISER.UseVisualStyleBackColor = False
		# 
		# NUTS
		# 
		self._NUTS.BackColor = System.Drawing.Color.MintCream
		self._NUTS.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._NUTS.ForeColor = System.Drawing.Color.DodgerBlue
		self._NUTS.Location = System.Drawing.Point(6, 140)
		self._NUTS.Name = "NUTS"
		self._NUTS.Size = System.Drawing.Size(188, 34)
		self._NUTS.TabIndex = 8
		self._NUTS.Text = "Nuts and bolts kit"
		self._NUTS.UseVisualStyleBackColor = False
		# 
		# ASMBL
		# 
		self._ASMBL.BackColor = System.Drawing.Color.MintCream
		self._ASMBL.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._ASMBL.ForeColor = System.Drawing.Color.DodgerBlue
		self._ASMBL.Location = System.Drawing.Point(6, 180)
		self._ASMBL.Name = "ASMBL"
		self._ASMBL.Size = System.Drawing.Size(188, 34)
		self._ASMBL.TabIndex = 9
		self._ASMBL.Text = "Assembly"
		self._ASMBL.UseVisualStyleBackColor = False
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Chocolate
		self._label1.Location = System.Drawing.Point(514, 78)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(104, 46)
		self._label1.TabIndex = 17
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Chocolate
		self._label2.Location = System.Drawing.Point(514, 124)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(23, 24)
		self._label2.TabIndex = 18
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Chocolate
		self._label3.Location = System.Drawing.Point(595, 124)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(23, 24)
		self._label3.TabIndex = 19
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Chocolate
		self._label4.Location = System.Drawing.Point(604, 54)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(42, 30)
		self._label4.TabIndex = 20
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Chocolate
		self._label5.Location = System.Drawing.Point(604, 35)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(14, 19)
		self._label5.TabIndex = 21
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Chocolate
		self._label6.Location = System.Drawing.Point(595, 21)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(14, 14)
		self._label6.TabIndex = 22
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Chocolate
		self._label7.Location = System.Drawing.Point(505, 65)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(14, 19)
		self._label7.TabIndex = 23
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Chocolate
		self._label8.Location = System.Drawing.Point(494, 59)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(14, 19)
		self._label8.TabIndex = 24
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Black
		self._label9.Location = System.Drawing.Point(608, 44)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(10, 10)
		self._label9.TabIndex = 25
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Pink
		self._label10.Location = System.Drawing.Point(599, 25)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(10, 10)
		self._label10.TabIndex = 26
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Black
		self._label11.Location = System.Drawing.Point(636, 54)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(10, 10)
		self._label11.TabIndex = 27
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SteelBlue
		self.ClientSize = System.Drawing.Size(674, 430)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._gbTruck)
		self.Controls.Add(self._labelSubTot)
		self.Controls.Add(self._labelTot)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._gbMisc)
		self.Controls.Add(self._gbWS)
		self.Controls.Add(self._gbStyles)
		self.Name = "MainForm"
		self.Text = "Pg485skate"
		self._gbMisc.ResumeLayout(False)
		self._gbWS.ResumeLayout(False)
		self._gbStyles.ResumeLayout(False)
		self._gbTruck.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button2Click(self, sender, e):
		amt1 = 0
		amt2 = 0
		amt3 = 0
		amt4 = 0
		subtot = amt1 + amt2 + amt3 + amt4
		tax = subtot * 0.06
		tot = subtot + tax
		if TMT.Checked == True:
			amt1 = 60
		if TDOG.Checked == True:
			amt1 = 45
		if TSK.Checked == true:
			amt1 = 50
		if si51.Checked == True:
			amt2 = 20
		if si55.Checked == True:
			amt2 = 22
		if si58.Checked == True:
			amt2 = 24
		if si61.Checked == True:
			amt2 = 28
		if ax775.Checked == True:
			amt3 = 35
		if ax8.Checked == True:
			amt3 = 40
		if ax85.Checked == True:
			amt3 = 45
		""" ADD: amt4 stuff - the groupbox with checkboxes """
		self._labelSubTot.Text = str(subtot)
		self._labelTot.Text    = str(tot)

	def Button3Click(self, sender, e):
		self._labelSubTot.Text = ""
		self._labelTot.Text    = ""

	def Button4Click(self, sender, e):
		Application.Exit()