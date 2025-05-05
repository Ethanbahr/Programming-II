using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg435ticketsales
{
    public partial class StudentForm_pg435_ : Form
    {
        public partial class StudentForm : Form {
            private Form myParent;
        }
        public StudentForm(Form myParent) {
            InitializeComponent();
            this.myParent = myParent;
        }
    }
    public StudentForm_pg435_()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e) {
            this.myParent.Show();
            this.Hide();
        }
    }
}
