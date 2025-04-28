namespace pg273_Books__real_
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int Books = int.Parse(textBox1.Text);
            int Points = 0;
            if (Books == 0); 
            {
                Points = 0;
            }
            if (Books = 1); 
            {
                Points = 5;
            }
            if (Books = 2); 
            {
                Points = 15;
            }
            if (Books = 3);
            {
                Points = 30;
            }
            if (Books >= 4);
            {
                Points = 60;
            }
            label2.Text = ("You have ") + (Points) + (" points");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}