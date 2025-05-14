namespace Prog122d
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox1.Items.Add("X:\t\tY:");
            for (int x = -12; x <= 16; x++)
            {
                double ans = ((Math.Pow(x, 6)) + ((Math.Pow(x, 5)) * (0 - 3)) + ((Math.Pow(x, 4)) * (0 - 93)) + ((Math.Pow(x, 3)) * 87) + ((Math.Pow(x, 2)) * 1596) - (x * (0 - 1380)) - 2800);
                listBox1.Items.Add(x + "\t\t" + ans);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}