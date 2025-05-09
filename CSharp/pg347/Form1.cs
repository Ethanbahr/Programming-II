using Microsoft.VisualBasic;
namespace pg347
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        const int intZERO = 0;
        private void button1_Click(object sender, EventArgs e)
        {
            // import math;
            int num  = int.Parse(textBox1.Text);
            long sum = 0;
            // ---------- Factorial code ----------
            for (int i = 0; i < num; i++) {
                sum *= i;
            }
            // label3.Text = sum;
            for (sum = 0; sum < intZERO; sum++)
            {
                while (int.TryParse(Interaction.InputBox("Enter number: " + (sum + 1).ToString(), "Need a number"), out num) == false)
                {
                    MessageBox.Show("Please enter an integer");
                }
            }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}