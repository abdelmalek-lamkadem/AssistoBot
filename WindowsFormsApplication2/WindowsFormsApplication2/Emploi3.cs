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
    public partial class Emploi3 : Form
    {
        public Emploi3()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            EmploiROC1 f = new EmploiROC1();
            f.Show();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            EmploiIA2 f = new EmploiIA2();
            f.Show();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            EmploiGI2 f = new EmploiGI2();
            f.Show();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            EmploiIRSI2 f = new EmploiIRSI2();
            f.Show();
        }
    }
}
