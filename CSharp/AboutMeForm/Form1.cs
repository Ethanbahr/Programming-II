namespace AboutMeForm

{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            label1.Text = "Ethan Bahr";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label1.Text = "Minecraft Club";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            label1.Text = "'No, Luke, I am your father.' - Darth Vader, Star Wars Episode 5";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            label1.Text = "";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}