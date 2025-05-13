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
            foreach (int num in Range(-12, 17)) 
            {
            int ans = ((num**6) + (num**5 * (0 - 3)) + (num**4 * (0 - 93)) + (num**3 * 87) + (num**2 * 1596) - (num * (0 - 1380)) - 2800);
            listBox1.Items.Add(ans);
            }
            // ans = ((num**6) + (num **5 * (0-3)) + (num **4 *(0 - 93)) + (num **3 * 87) + (num **2 * 1596) - (num * (0 - 1380)) - 2800)
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}