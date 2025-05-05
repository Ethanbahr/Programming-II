namespace Pg435ticketsales
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e) {
            GeneralForm frm = new GeneralForm(this);
            frm.Show();
            this.Hide();
        }

        private void button1_Click(object sender, EventArgs e) {
            Form frm = new StudentForm_pg435_();
            GeneralForm frm = new GeneralForm(this);
            frm.Show();
            this.Hide();
        }
    }
}