using System;
using System.Drawing;
using System.Windows.Forms;

namespace WindowsFormsApplication2
{
    public partial class Maps : Form
    {
        public Maps()
        {
            InitializeComponent();
        }

        // Point d'entrée de l'application
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Maps());
        }

        private void Maps_Load(object sender, EventArgs e)
        {
            try
            {
                
                pictureBox1.Image = Resource1.cat; 
                pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Erreur lors du chargement de l'image : " + ex.Message);
            }
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
          
        }
    }
}
