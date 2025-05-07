namespace pg347
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            import math
            int num  = int.Parse(textBox1.Text);
            long sum = 0;
            // ---------- Factorial code (comment) ----------
            // for (int i = 0; i < num; i++) {
            //     sum *= i
            // }
            label3.Text = sum;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}