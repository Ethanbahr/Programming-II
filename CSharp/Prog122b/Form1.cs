namespace Prog122b
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int lcv = 1;
            while (lcv <= 40)
            {
                listBox1.Items.Clear();
                int pay = lcv * 4;
                listBox1.Items.Add($"{lcv}\t\t{pay}");
                lcv++;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}