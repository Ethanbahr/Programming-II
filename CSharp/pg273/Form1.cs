namespace pg273
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double Weight = double.Parse(textBox1.Text);
            double Mass = Weight * 9.8;
            label2.Text = ("Mass: ") + (Mass.ToString()) + (" kilograms");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}