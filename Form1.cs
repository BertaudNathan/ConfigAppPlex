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
        public bool Flag = false;


        public List<Control> ElemInvisible { get; set; } = new List<Control>();

        public List<Control> Page1 { get; set; } = new List<Control>();
        public List<Control> Page2 { get; set; } = new List<Control>();
        public List<List<Control>> Pages { get; set; } = new List<List<Control>>();
        public List<string> PagesTitle { get; set; } = new List<string>();
        public int test { get; set; } = 0;
        public int CurrentPage { get; set; } = 1;



        private void SwitchPage(int newPage)
        {

            if (CurrentPage != newPage)
            {
                foreach (var elem in ElemInvisible)
                {
                    elem.Visible = false;
                }
                foreach (var elem in Pages[CurrentPage - 1])
                {
                    elem.Visible = false;
                }
                foreach (var elem in Pages[newPage - 1])
                {
                    if (!ElemInvisible.Contains(elem))
                    {
                        elem.Visible = true;
                    }
                }
                label6.Text = PagesTitle[newPage - 1];
                CurrentPage = newPage;
            }
        }

        private void addToElemInvisible()
        {
            ElemInvisible.Add(label2);
            ElemInvisible.Add(label3);
            ElemInvisible.Add(flowLayoutPanel1);
        }


        private void addToPage1()
        {
            Page1.Add(button1);
            Page1.Add(textBox1);
            Page1.Add(label1);
            Page1.Add(label2);
            Page1.Add(label3);
            Page1.Add(label4);
            Page1.Add(textBox2);
            Page1.Add(button2);
            Page1.Add(label5);
            Page1.Add(checkBox1);
            Page1.Add(radioButton1);
            Page1.Add(flowLayoutPanel1);
        }

        private void addToPage2()
        {
            Page2.Add(textBox3);
            Page2.Add(label7);
        }

        private void addToPageTitle()
        {
            PagesTitle.Add("Configuration de l'IP");
            PagesTitle.Add("A propos");
        }


        private void indexPages()
        {
            Pages.Add(Page1);
            Pages.Add(Page2);
        }

        public Form1()
        {
            CurrentPage = 1;
            InitializeComponent();
            addToPage1();
            addToPage2();
            indexPages();
            addToPageTitle();
            addToElemInvisible();
            button1.Text = "Valider";
            label1.Text = "IP de la seedbox";
            Json = JsonConvert.DeserializeObject<Dictionary<string, string>>(File.ReadAllText("../../../config.json"));
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

        private void button2_Click(object sender, EventArgs e)
        {
            if (!ToolBox.ValidateIPv4(textBox2.Text))
            {
                label3.Text = "l'ip entree est invalide";
                label3.ForeColor = Color.Red;
                label3.Visible = true;
            }
            else
            {
                label3.Text = "default";
                label3.ForeColor = Color.Black;
                label3.Visible = false;
                Json["PlexIP"] = textBox2.Text;
                File.WriteAllText("../../../config.json", JsonConvert.SerializeObject(Json));
            }
        }

        private void checkedRadio(object sender, EventArgs e)
        {
            RadioButton rb = sender as RadioButton;
            textBox2.Text = rb.Text;
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            switch (checkBox1.Checked)
            {
                case true:
                    string hostName = Dns.GetHostName();
                    IPAddress[] IPs = Dns.GetHostEntry(hostName).AddressList;
                    var i = 2;
                    foreach (var ip in IPs)
                    {
                        if (ToolBox.ValidateIPv4(ip.ToString()))
                        {
                            flowLayoutPanel1.Visible = true;
                            var radio = new RadioButton();
                            radio.Text = ip.ToString();
                            radio.CheckedChanged += checkedRadio;
                            flowLayoutPanel1.Controls.Add(radio);
                            i += 2;
                        }
                    }
                    break;
                case false:
                    flowLayoutPanel1.Visible = false;
                    flowLayoutPanel1.Controls.Clear();
                    break;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {

            if (!Flag)
            {
                panel2.Visible = true;
                Flag = true;
            }
            else
            {
                panel2.Visible = false;
                Flag = false;
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            SwitchPage(1);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            SwitchPage(2);
        }


    }
}