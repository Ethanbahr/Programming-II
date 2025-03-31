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
		self._lblsi61 = System.Windows.Forms.RadioButton()
		self._lblsi58 = System.Windows.Forms.RadioButton()
		self._lblsi55 = System.Windows.Forms.RadioButton()
		self._lblsi51 = System.Windows.Forms.RadioButton()
		self._gbStyles = System.Windows.Forms.GroupBox()
		self._lblTSK = System.Windows.Forms.RadioButton()
		self._lblTDOG = System.Windows.Forms.RadioButton()
		self._lblTMT = System.Windows.Forms.RadioButton()
		self._labelSubTot = System.Windows.Forms.Label()
		self._gbTruck = System.Windows.Forms.GroupBox()
		self._lblax85 = System.Windows.Forms.RadioButton()
		self._lblax8 = System.Windows.Forms.RadioButton()
		self._lblax775 = System.Windows.Forms.RadioButton()
		self._lblGT = System.Windows.Forms.CheckBox()
		self._lblBEAR = System.Windows.Forms.CheckBox()
		self._lblRISER = System.Windows.Forms.CheckBox()
		self._lblNUTS = System.Windows.Forms.CheckBox()
		self._lblASMBL = System.Windows.Forms.CheckBox()
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
		self._gbMisc.Controls.Add(self._lblASMBL)
		self._gbMisc.Controls.Add(self._lblNUTS)
		self._gbMisc.Controls.Add(self._lblRISER)
		self._gbMisc.Controls.Add(self._lblBEAR)
		self._gbMisc.Controls.Add(self._lblGT)
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
		self._gbWS.Controls.Add(self._lblsi61)
		self._gbWS.Controls.Add(self._lblsi58)
		self._gbWS.Controls.Add(self._lblsi55)
		self._gbWS.Controls.Add(self._lblsi51)
		self._gbWS.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._gbWS.ForeColor = System.Drawing.Color.Navy
		self._gbWS.Location = System.Drawing.Point(225, 5)
		self._gbWS.Name = "gbWS"
		self._gbWS.Size = System.Drawing.Size(201, 208)
		self._gbWS.TabIndex = 10
		self._gbWS.TabStop = False
		self._gbWS.Text = "Wheel sets"
		# 
		# lblsi61
		# 
		self._lblsi61.BackColor = System.Drawing.Color.MintCream
		self._lblsi61.ForeColor = System.Drawing.Color.DodgerBlue
		self._lblsi61.Location = System.Drawing.Point(6, 154)
		self._lblsi61.Name = "lblsi61"
		self._lblsi61.Size = System.Drawing.Size(189, 36)
		self._lblsi61.TabIndex = 3
		self._lblsi61.TabStop = True
		self._lblsi61.Text = "61 mm"
		self._lblsi61.UseVisualStyleBackColor = False
		# 
		# lblsi58
		# 
		self._lblsi58.BackColor = System.Drawing.Color.MintCream
		self._lblsi58.ForeColor = System.Drawing.Color.DodgerBlue
		self._lblsi58.Location = System.Drawing.Point(6, 114)
		self._lblsi58.Name = "lblsi58"
		self._lblsi58.Size = System.Drawing.Size(189, 36)
		self._lblsi58.TabIndex = 2
		self._lblsi58.TabStop = True
		self._lblsi58.Text = "58 mm"
		self._lblsi58.UseVisualStyleBackColor = False
		# 
		# lblsi55
		# 
		self._lblsi55.BackColor = System.Drawing.Color.MintCream
		self._lblsi55.ForeColor = System.Drawing.Color.DodgerBlue
		self._lblsi55.Location = System.Drawing.Point(6, 73)
		self._lblsi55.Name = "lblsi55"
		self._lblsi55.Size = System.Drawing.Size(189, 34)
		self._lblsi55.TabIndex = 1
		self._lblsi55.TabStop = True
		self._lblsi55.Text = "55 mm"
		self._lblsi55.UseVisualStyleBackColor = False
		# 
		# lblsi51
		# 
		self._lblsi51.BackColor = System.Drawing.Color.MintCream
		self._lblsi51.ForeColor = System.Drawing.Color.DodgerBlue
		self._lblsi51.Location = System.Drawing.Point(6, 29)
		self._lblsi51.Name = "lblsi51"
		self._lblsi51.Size = System.Drawing.Size(189, 38)
		self._lblsi51.TabIndex = 0
		self._lblsi51.TabStop = True
		self._lblsi51.Text = "51 mm"
		self._lblsi51.UseVisualStyleBackColor = False
		# 
		# gbStyles
		# 
		self._gbStyles.BackColor = System.Drawing.Color.Transparent
		self._gbStyles.Controls.Add(self._lblTSK)
		self._gbStyles.Controls.Add(self._lblTDOG)
		self._gbStyles.Controls.Add(self._lblTMT)
		self._gbStyles.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._gbStyles.ForeColor = System.Drawing.Color.Navy
		self._gbStyles.Location = System.Drawing.Point(12, 5)
		self._gbStyles.Name = "gbStyles"
		self._gbStyles.Size = System.Drawing.Size(207, 165)
		self._gbStyles.TabIndex = 9
		self._gbStyles.TabStop = False
		self._gbStyles.Text = "Styles"
		# 
		# lblTSK
		# 
		self._lblTSK.BackColor = System.Drawing.Color.MintCream
		self._lblTSK.ForeColor = System.Drawing.Color.DodgerBlue
		self._lblTSK.Location = System.Drawing.Point(6, 114)
		self._lblTSK.Name = "lblTSK"
		self._lblTSK.Size = System.Drawing.Size(189, 36)
		self._lblTSK.TabIndex = 2
		self._lblTSK.TabStop = True
		self._lblTSK.Text = "The Street King"
		self._lblTSK.UseVisualStyleBackColor = False
		# 
		# lblTDOG
		# 
		self._lblTDOG.BackColor = System.Drawing.Color.MintCream
		self._lblTDOG.ForeColor = System.Drawing.Color.DodgerBlue
		self._lblTDOG.Location = System.Drawing.Point(6, 74)
		self._lblTDOG.Name = "lblTDOG"
		self._lblTDOG.Size = System.Drawing.Size(189, 34)
		self._lblTDOG.TabIndex = 1
		self._lblTDOG.TabStop = True
		self._lblTDOG.Text = "The Dictator of Grind"
		self._lblTDOG.UseVisualStyleBackColor = False
		# 
		# lblTMT
		# 
		self._lblTMT.BackColor = System.Drawing.Color.MintCream
		self._lblTMT.ForeColor = System.Drawing.Color.DodgerBlue
		self._lblTMT.Location = System.Drawing.Point(6, 29)
		self._lblTMT.Name = "lblTMT"
		self._lblTMT.Size = System.Drawing.Size(189, 38)
		self._lblTMT.TabIndex = 0
		self._lblTMT.TabStop = True
		self._lblTMT.Text = "The Master Thrasher"
		self._lblTMT.UseVisualStyleBackColor = False
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
		self._gbTruck.Controls.Add(self._lblax85)
		self._gbTruck.Controls.Add(self._lblax8)
		self._gbTruck.Controls.Add(self._lblax775)
		self._gbTruck.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._gbTruck.ForeColor = System.Drawing.Color.Navy
		self._gbTruck.Location = System.Drawing.Point(225, 219)
		self._gbTruck.Name = "gbTruck"
		self._gbTruck.Size = System.Drawing.Size(207, 165)
		self._gbTruck.TabIndex = 10
		self._gbTruck.TabStop = False
		self._gbTruck.Text = "Truck assemblies"
		# 
		# lblax85
		# 
		self._lblax85.BackColor = System.Drawing.Color.MintCream
		self._lblax85.ForeColor = System.Drawing.Color.DodgerBlue
		self._lblax85.Location = System.Drawing.Point(6, 114)
		self._lblax85.Name = "lblax85"
		self._lblax85.Size = System.Drawing.Size(189, 36)
		self._lblax85.TabIndex = 2
		self._lblax85.TabStop = True
		self._lblax85.Text = "8.5 axle"
		self._lblax85.UseVisualStyleBackColor = False
		# 
		# lblax8
		# 
		self._lblax8.BackColor = System.Drawing.Color.MintCream
		self._lblax8.ForeColor = System.Drawing.Color.DodgerBlue
		self._lblax8.Location = System.Drawing.Point(6, 74)
		self._lblax8.Name = "lblax8"
		self._lblax8.Size = System.Drawing.Size(189, 34)
		self._lblax8.TabIndex = 1
		self._lblax8.TabStop = True
		self._lblax8.Text = "8 axle"
		self._lblax8.UseVisualStyleBackColor = False
		# 
		# lblax775
		# 
		self._lblax775.BackColor = System.Drawing.Color.MintCream
		self._lblax775.ForeColor = System.Drawing.Color.DodgerBlue
		self._lblax775.Location = System.Drawing.Point(6, 29)
		self._lblax775.Name = "lblax775"
		self._lblax775.Size = System.Drawing.Size(189, 38)
		self._lblax775.TabIndex = 0
		self._lblax775.TabStop = True
		self._lblax775.Text = "7.75 axle"
		self._lblax775.UseVisualStyleBackColor = False
		# 
		# lblGT
		# 
		self._lblGT.BackColor = System.Drawing.Color.MintCream
		self._lblGT.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lblGT.ForeColor = System.Drawing.Color.DodgerBlue
		self._lblGT.Location = System.Drawing.Point(6, 23)
		self._lblGT.Name = "lblGT"
		self._lblGT.Size = System.Drawing.Size(188, 34)
		self._lblGT.TabIndex = 5
		self._lblGT.Text = "Grip tape"
		self._lblGT.UseVisualStyleBackColor = False
		# 
		# lblBEAR
		# 
		self._lblBEAR.BackColor = System.Drawing.Color.MintCream
		self._lblBEAR.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lblBEAR.ForeColor = System.Drawing.Color.DodgerBlue
		self._lblBEAR.Location = System.Drawing.Point(6, 63)
		self._lblBEAR.Name = "lblBEAR"
		self._lblBEAR.Size = System.Drawing.Size(188, 34)
		self._lblBEAR.TabIndex = 6
		self._lblBEAR.Text = "Bearings"
		self._lblBEAR.UseVisualStyleBackColor = False
		# 
		# lblRISER
		# 
		self._lblRISER.BackColor = System.Drawing.Color.MintCream
		self._lblRISER.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lblRISER.ForeColor = System.Drawing.Color.DodgerBlue
		self._lblRISER.Location = System.Drawing.Point(6, 100)
		self._lblRISER.Name = "lblRISER"
		self._lblRISER.Size = System.Drawing.Size(188, 34)
		self._lblRISER.TabIndex = 7
		self._lblRISER.Text = "Riser pads"
		self._lblRISER.UseVisualStyleBackColor = False
		# 
		# lblNUTS
		# 
		self._lblNUTS.BackColor = System.Drawing.Color.MintCream
		self._lblNUTS.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lblNUTS.ForeColor = System.Drawing.Color.DodgerBlue
		self._lblNUTS.Location = System.Drawing.Point(6, 140)
		self._lblNUTS.Name = "lblNUTS"
		self._lblNUTS.Size = System.Drawing.Size(188, 34)
		self._lblNUTS.TabIndex = 8
		self._lblNUTS.Text = "Nuts and bolts kit"
		self._lblNUTS.UseVisualStyleBackColor = False
		# 
		# lblASMBL
		# 
		self._lblASMBL.BackColor = System.Drawing.Color.MintCream
		self._lblASMBL.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lblASMBL.ForeColor = System.Drawing.Color.DodgerBlue
		self._lblASMBL.Location = System.Drawing.Point(6, 180)
		self._lblASMBL.Name = "lblASMBL"
		self._lblASMBL.Size = System.Drawing.Size(188, 34)
		self._lblASMBL.TabIndex = 9
		self._lblASMBL.Text = "Assembly"
		self._lblASMBL.UseVisualStyleBackColor = False
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
		if self._lblTMT.Checked == True:
			amt1 = 60
		if self._lblTDOG.Checked == True:
			amt1 = 45
		if self._lblTSK.Checked == True:
			amt1 = 50
		if self._lblsi51.Checked == True:
			amt2 = 20
		if self._lblsi55.Checked == True:
			amt2 = 22
		if self._lblsi58.Checked == True:
			amt2 = 24
		if self._lblsi61.Checked == True:
			amt2 = 28
		if self._lblax775.Checked == True:
			amt3 = 35
		if self._lblax8.Checked == True:
			amt3 = 40
		if self._lblax85.Checked == True:
			amt3 = 45
		""" ADD: amt4 stuff - the groupbox with checkboxes """
		self._labelSubTot.Text = str(subtot)
		self._labelTot.Text    = str(tot)

	def Button3Click(self, sender, e):
		self._labelSubTot.Text = ""
		self._labelTot.Text    = ""

	def Button4Click(self, sender, e):
		Application.Exit()