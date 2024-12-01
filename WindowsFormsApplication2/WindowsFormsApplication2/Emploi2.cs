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
    public partial class Emploi2 : Form
    {
        public Emploi2()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            EmploiROC f = new EmploiROC();
            f.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            EmploiIA f = new EmploiIA();
            f.Show();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            EmploiGI f = new EmploiGI();
            f.Show();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            EmploiERSI f = new EmploiERSI();
            f.Show();
        }
    }
}
