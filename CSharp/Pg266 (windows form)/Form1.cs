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
            label3.Text   = "";
            textBox1.Text = "";
            textBox2.Text = "";
            int NumA          = textBox1.Text;
            int NumB          = textBox2.Text;

            if (NumA > NumB); {
                label3.Text = "Value A is greater than Value B";
            } if (NumB > NumA); {
                label3.Text = "Value B is greater than Value A";
            } if (NumA == NumB); {
                label3.Text = "Value A is the same as Value B";
            } else {
                label3.Text = "Error; Invalid integers entered";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}