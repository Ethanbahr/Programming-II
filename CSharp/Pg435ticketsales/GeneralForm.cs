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
    public partial class GeneralForm : Form {
        public partial class GeneralForm : Form {
            private Form myParent;
        }
        public GeneralForm(Form myParent)
        {
            InitializeComponent();
            this.myParent = myParent;
        }
    }
   
    public partial class GeneralForm_pg435_ : Form
    {
        public GeneralForm_pg435_()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e) {
            this.Parent.Show();
            this.Hide();
        }
    }
}
