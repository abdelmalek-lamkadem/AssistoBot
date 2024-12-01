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
    public partial class Emploi : Form
    {
        public Emploi()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Emploi1 f = new Emploi1();
            f.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Emploi2 f = new Emploi2();
            f.Show();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Emploi3 f = new Emploi3();
            f.Show();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Home f = new Home();
            f.Show();
        }
    }
}
