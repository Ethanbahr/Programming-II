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
		self._rbsi61 = System.Windows.Forms.RadioButton()
		self._rbsi58 = System.Windows.Forms.RadioButton()
		self._rbsi55 = System.Windows.Forms.RadioButton()
		self._rbsi51 = System.Windows.Forms.RadioButton()
		self._gbStyles = System.Windows.Forms.GroupBox()
		self._rbTSK = System.Windows.Forms.RadioButton()
		self._rbTDOG = System.Windows.Forms.RadioButton()
		self._rbTMT = System.Windows.Forms.RadioButton()
		self._labelSubTot = System.Windows.Forms.Label()
		self._gbTruck = System.Windows.Forms.GroupBox()
		self._rbax85 = System.Windows.Forms.RadioButton()
		self._rbax8 = System.Windows.Forms.RadioButton()
		self._rbax775 = System.Windows.Forms.RadioButton()
		self._cbGT = System.Windows.Forms.CheckBox()
		self._cbBEAR = System.Windows.Forms.CheckBox()
		self._cbRISER = System.Windows.Forms.CheckBox()
		self._cbNUTS = System.Windows.Forms.CheckBox()
		self._cbASMBL = System.Windows.Forms.CheckBox()
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
		self._gbMisc.Controls.Add(self._cbASMBL)
		self._gbMisc.Controls.Add(self._cbNUTS)
		self._gbMisc.Controls.Add(self._cbRISER)
		self._gbMisc.Controls.Add(self._cbBEAR)
		self._gbMisc.Controls.Add(self._cbGT)
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
		self._gbWS.Controls.Add(self._rbsi61)
		self._gbWS.Controls.Add(self._rbsi58)
		self._gbWS.Controls.Add(self._rbsi55)
		self._gbWS.Controls.Add(self._rbsi51)
		self._gbWS.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._gbWS.ForeColor = System.Drawing.Color.Navy
		self._gbWS.Location = System.Drawing.Point(225, 5)
		self._gbWS.Name = "gbWS"
		self._gbWS.Size = System.Drawing.Size(201, 208)
		self._gbWS.TabIndex = 10
		self._gbWS.TabStop = False
		self._gbWS.Text = "Wheel sets"
		# 
		# rbsi61
		# 
		self._rbsi61.BackColor = System.Drawing.Color.MintCream
		self._rbsi61.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbsi61.Location = System.Drawing.Point(6, 154)
		self._rbsi61.Name = "rbsi61"
		self._rbsi61.Size = System.Drawing.Size(189, 36)
		self._rbsi61.TabIndex = 3
		self._rbsi61.TabStop = True
		self._rbsi61.Text = "61 mm"
		self._rbsi61.UseVisualStyleBackColor = False
		# 
		# rbsi58
		# 
		self._rbsi58.BackColor = System.Drawing.Color.MintCream
		self._rbsi58.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbsi58.Location = System.Drawing.Point(6, 114)
		self._rbsi58.Name = "rbsi58"
		self._rbsi58.Size = System.Drawing.Size(189, 36)
		self._rbsi58.TabIndex = 2
		self._rbsi58.TabStop = True
		self._rbsi58.Text = "58 mm"
		self._rbsi58.UseVisualStyleBackColor = False
		# 
		# rbsi55
		# 
		self._rbsi55.BackColor = System.Drawing.Color.MintCream
		self._rbsi55.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbsi55.Location = System.Drawing.Point(6, 73)
		self._rbsi55.Name = "rbsi55"
		self._rbsi55.Size = System.Drawing.Size(189, 34)
		self._rbsi55.TabIndex = 1
		self._rbsi55.TabStop = True
		self._rbsi55.Text = "55 mm"
		self._rbsi55.UseVisualStyleBackColor = False
		# 
		# rbsi51
		# 
		self._rbsi51.BackColor = System.Drawing.Color.MintCream
		self._rbsi51.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbsi51.Location = System.Drawing.Point(6, 29)
		self._rbsi51.Name = "rbsi51"
		self._rbsi51.Size = System.Drawing.Size(189, 38)
		self._rbsi51.TabIndex = 0
		self._rbsi51.TabStop = True
		self._rbsi51.Text = "51 mm"
		self._rbsi51.UseVisualStyleBackColor = False
		# 
		# gbStyles
		# 
		self._gbStyles.BackColor = System.Drawing.Color.Transparent
		self._gbStyles.Controls.Add(self._rbTSK)
		self._gbStyles.Controls.Add(self._rbTDOG)
		self._gbStyles.Controls.Add(self._rbTMT)
		self._gbStyles.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._gbStyles.ForeColor = System.Drawing.Color.Navy
		self._gbStyles.Location = System.Drawing.Point(12, 5)
		self._gbStyles.Name = "gbStyles"
		self._gbStyles.Size = System.Drawing.Size(207, 165)
		self._gbStyles.TabIndex = 9
		self._gbStyles.TabStop = False
		self._gbStyles.Text = "Styles"
		# 
		# rbTSK
		# 
		self._rbTSK.BackColor = System.Drawing.Color.MintCream
		self._rbTSK.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbTSK.Location = System.Drawing.Point(6, 114)
		self._rbTSK.Name = "rbTSK"
		self._rbTSK.Size = System.Drawing.Size(189, 36)
		self._rbTSK.TabIndex = 2
		self._rbTSK.TabStop = True
		self._rbTSK.Text = "The Street King"
		self._rbTSK.UseVisualStyleBackColor = False
		# 
		# rbTDOG
		# 
		self._rbTDOG.BackColor = System.Drawing.Color.MintCream
		self._rbTDOG.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbTDOG.Location = System.Drawing.Point(6, 74)
		self._rbTDOG.Name = "rbTDOG"
		self._rbTDOG.Size = System.Drawing.Size(189, 34)
		self._rbTDOG.TabIndex = 1
		self._rbTDOG.TabStop = True
		self._rbTDOG.Text = "The Dictator of Grind"
		self._rbTDOG.UseVisualStyleBackColor = False
		# 
		# rbTMT
		# 
		self._rbTMT.BackColor = System.Drawing.Color.MintCream
		self._rbTMT.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbTMT.Location = System.Drawing.Point(6, 29)
		self._rbTMT.Name = "rbTMT"
		self._rbTMT.Size = System.Drawing.Size(189, 38)
		self._rbTMT.TabIndex = 0
		self._rbTMT.TabStop = True
		self._rbTMT.Text = "The Master Thrasher"
		self._rbTMT.UseVisualStyleBackColor = False
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
		self._gbTruck.Controls.Add(self._rbax85)
		self._gbTruck.Controls.Add(self._rbax8)
		self._gbTruck.Controls.Add(self._rbax775)
		self._gbTruck.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._gbTruck.ForeColor = System.Drawing.Color.Navy
		self._gbTruck.Location = System.Drawing.Point(225, 219)
		self._gbTruck.Name = "gbTruck"
		self._gbTruck.Size = System.Drawing.Size(207, 165)
		self._gbTruck.TabIndex = 10
		self._gbTruck.TabStop = False
		self._gbTruck.Text = "Truck assemblies"
		# 
		# rbax85
		# 
		self._rbax85.BackColor = System.Drawing.Color.MintCream
		self._rbax85.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbax85.Location = System.Drawing.Point(6, 114)
		self._rbax85.Name = "rbax85"
		self._rbax85.Size = System.Drawing.Size(189, 36)
		self._rbax85.TabIndex = 2
		self._rbax85.TabStop = True
		self._rbax85.Text = "8.5 axle"
		self._rbax85.UseVisualStyleBackColor = False
		# 
		# rbax8
		# 
		self._rbax8.BackColor = System.Drawing.Color.MintCream
		self._rbax8.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbax8.Location = System.Drawing.Point(6, 74)
		self._rbax8.Name = "rbax8"
		self._rbax8.Size = System.Drawing.Size(189, 34)
		self._rbax8.TabIndex = 1
		self._rbax8.TabStop = True
		self._rbax8.Text = "8 axle"
		self._rbax8.UseVisualStyleBackColor = False
		# 
		# rbax775
		# 
		self._rbax775.BackColor = System.Drawing.Color.MintCream
		self._rbax775.ForeColor = System.Drawing.Color.DodgerBlue
		self._rbax775.Location = System.Drawing.Point(6, 29)
		self._rbax775.Name = "rbax775"
		self._rbax775.Size = System.Drawing.Size(189, 38)
		self._rbax775.TabIndex = 0
		self._rbax775.TabStop = True
		self._rbax775.Text = "7.75 axle"
		self._rbax775.UseVisualStyleBackColor = False
		# 
		# cbGT
		# 
		self._cbGT.BackColor = System.Drawing.Color.MintCream
		self._cbGT.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._cbGT.ForeColor = System.Drawing.Color.DodgerBlue
		self._cbGT.Location = System.Drawing.Point(6, 23)
		self._cbGT.Name = "cbGT"
		self._cbGT.Size = System.Drawing.Size(188, 34)
		self._cbGT.TabIndex = 5
		self._cbGT.Text = "Grip tape"
		self._cbGT.UseVisualStyleBackColor = False
		# 
		# cbBEAR
		# 
		self._cbBEAR.BackColor = System.Drawing.Color.MintCream
		self._cbBEAR.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._cbBEAR.ForeColor = System.Drawing.Color.DodgerBlue
		self._cbBEAR.Location = System.Drawing.Point(6, 63)
		self._cbBEAR.Name = "cbBEAR"
		self._cbBEAR.Size = System.Drawing.Size(188, 34)
		self._cbBEAR.TabIndex = 6
		self._cbBEAR.Text = "Bearings"
		self._cbBEAR.UseVisualStyleBackColor = False
		# 
		# cbRISER
		# 
		self._cbRISER.BackColor = System.Drawing.Color.MintCream
		self._cbRISER.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._cbRISER.ForeColor = System.Drawing.Color.DodgerBlue
		self._cbRISER.Location = System.Drawing.Point(6, 100)
		self._cbRISER.Name = "cbRISER"
		self._cbRISER.Size = System.Drawing.Size(188, 34)
		self._cbRISER.TabIndex = 7
		self._cbRISER.Text = "Riser pads"
		self._cbRISER.UseVisualStyleBackColor = False
		# 
		# cbNUTS
		# 
		self._cbNUTS.BackColor = System.Drawing.Color.MintCream
		self._cbNUTS.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._cbNUTS.ForeColor = System.Drawing.Color.DodgerBlue
		self._cbNUTS.Location = System.Drawing.Point(6, 140)
		self._cbNUTS.Name = "cbNUTS"
		self._cbNUTS.Size = System.Drawing.Size(188, 34)
		self._cbNUTS.TabIndex = 8
		self._cbNUTS.Text = "Nuts and bolts kit"
		self._cbNUTS.UseVisualStyleBackColor = False
		# 
		# cbASMBL
		# 
		self._cbASMBL.BackColor = System.Drawing.Color.MintCream
		self._cbASMBL.Font = System.Drawing.Font("Tempus Sans ITC", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._cbASMBL.ForeColor = System.Drawing.Color.DodgerBlue
		self._cbASMBL.Location = System.Drawing.Point(6, 180)
		self._cbASMBL.Name = "cbASMBL"
		self._cbASMBL.Size = System.Drawing.Size(188, 34)
		self._cbASMBL.TabIndex = 9
		self._cbASMBL.Text = "Assembly"
		self._cbASMBL.UseVisualStyleBackColor = False
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
		if self._rbTMT.Checked == True:
			amt1 = 60
		if self._rbTDOG.Checked == True:
			amt1 = 45
		if self._rbTSK.Checked == True:
			amt1 = 50
		if self._rbsi51.Checked == True:
			amt2 = 20
		if self._rbsi55.Checked == True:
			amt2 = 22
		if self._rbsi58.Checked == True:
			amt2 = 24
		if self._rbsi61.Checked == True:
			amt2 = 28
		if self._rbax775.Checked == True:
			amt3 = 35
		if self._rbax8.Checked == True:
			amt3 = 40
		if self._rbax85.Checked == True:
			amt3 = 45
		if self._cbGT.Checked == True:
			amt4 += 10
		elif self._cbBEAR.Checked == True:
			amt4 += 30
		elif self._cbRISER.Checked == True:
			amt4 += 2
		elif self._cbNUTS.Checked == True:
			amt4 += 3
		subtot = amt1 + amt2 + amt3 + amt4
		tax = subtot * 0.06
		tot = subtot + tax
		if self._cbASMBL.Checked == True:
			tot = tot - 0.60
		self._labelSubTot.Text = "Subtotal: $" + str(subtot)
		self._labelTot.Text    = "Total: $" + str(tot)

	def Button3Click(self, sender, e):
		self._labelSubTot.Text = ""
		self._labelTot.Text    = ""

	def Button4Click(self, sender, e):
		Application.Exit()