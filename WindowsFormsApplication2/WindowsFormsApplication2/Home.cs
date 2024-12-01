using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication2
{
    public partial class Home : Form
    {
        public Home()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Emploi f = new Emploi();
            f.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Maps f = new Maps();
            f.Show();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            News f = new News();
            f.Show();
        }
    }
}
