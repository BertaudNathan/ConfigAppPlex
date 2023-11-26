using System.IO;
using System.Net.Http.Json;
using System.Text.Json.Serialization;
using System.Windows.Forms.Design;
using Newtonsoft;
using Newtonsoft.Json;
using System.Net;
using static System.Net.Mime.MediaTypeNames;

namespace config_app
{
    public partial class Form1 : Form
    {
        public Dictionary<string, string> Json { get; set; }
        public Form1()
        {

            InitializeComponent();
            button1.Text = "Valider";
            label1.Text = "IP de la seedbox";
            Json = JsonConvert.DeserializeObject<Dictionary<string, string>>(File.ReadAllText("../../../config.json"));
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
                Json["seedboxIP"] = textBox1.Text;
                File.WriteAllText("../../../config.json", JsonConvert.SerializeObject(Json));
            }
        }

        private void checkedRadio()
        {

        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            switch (checkBox1.Checked)
            {
                case true:
                    string hostName = Dns.GetHostName();
                    IPAddress[] IPs = Dns.GetHostEntry(hostName).AddressList;
                    var i = 2;
                    label1.Text = IPs[0].ToString();
                    foreach (var ip in IPs)
                    {
                        flowLayoutPanel1.Visible = true;
                        var radio = new RadioButton();
                        radio.Text = ip.ToString();
                        //radio.Location = new Point(panel2.Location.X, panel2.Location.Y + i);
                        flowLayoutPanel1.Controls.Add(radio);
                        i += 2;
                    }
                    break;
                case false:
                    break;
            }
        }


    }
}