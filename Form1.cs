using System.Windows.Forms.Design;

namespace config_app
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            button1.Text = "Valider";
            label1.Text = "IP de la seedbox";
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (!ToolBox.ValidateIPv4(textBox1.Text))
            {
                label2.Text = "l'ip entree est invalide";
                label2.ForeColor = Color.Red;
                label2.Visible = true;
            }
            else
            {
                label2.Text = "default";
                label2.ForeColor = Color.Black;
                label2.Visible = false;
            }

        }
    }
}