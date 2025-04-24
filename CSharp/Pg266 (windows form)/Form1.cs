namespace Pg266__windows_form_
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int NumA      = int.Parse(textBox1.Text);
            int NumB      = int.Parse(textBox2.Text);

            if (NumA > NumB) {
                label3.Text = "Value A is greater than Value B";
            } if (NumB > NumA) {
                label3.Text = "Value B is greater than Value A";
            } if (NumA == NumB) {
                label3.Text = "Value A is the same as Value B";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}