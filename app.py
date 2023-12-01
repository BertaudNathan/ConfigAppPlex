import dearpygui.dearpygui as dpg
import socket
import json
global currentPage,default,ip_addresses

currentPage=1
default=True
ip_addresses=[]


dpg.create_context()
dpg.create_viewport(title='Application de configuration', width=1000, height=600,resizable=False,small_icon="assets/icon.ico",large_icon="assets/icon.ico")

def page1_callback(sender,app_data):
    global default,currentPage,ip_addresses
    if currentPage!=1 or default==True:
        currentPage=1
        default=False
        if dpg.does_alias_exist("page2"):
            dpg.delete_item("page2", children_only=False)
        with dpg.window(label="Configuration", width=1000, height=600,no_collapse=True,tag="page1",no_resize=True,no_move=True,no_close=True):
            with dpg.menu_bar():
                with dpg.menu(label="Menu"):
                    dpg.add_menu_item(label="Configuration")
                    dpg.add_menu_item(label="A propos", callback=page2_callback)
            dpg.add_input_text(label="utilisateur de la seedbox",tag="input4")
            dpg.add_button(label="Valider",callback=verifyInput,user_data="4")
            dpg.add_input_text(label="ip de la seedbox",tag="input1")
            dpg.add_text(default_value="l'ip est invalide",tag="notif1",show=False,color=(255,0,0))
            dpg.add_button(label="Valider",callback=verifyInput,user_data="1")
            dpg.add_input_text(label="utilisateur du serveur plex",tag="input3")
            dpg.add_button(label="Valider",callback=verifyInput,user_data="3")
            dpg.add_input_text(label="ip du serveur plex",tag="input2")
            dpg.add_text(default_value="l'ip est invalide",tag="notif2",show=False,color=(255,0,0))
            dpg.add_button(label="Valider",callback=verifyInput,user_data="2")
            dpg.add_checkbox(label="suggestion d'ip", callback=showIpSuggestion)
            
            
            dpg.add_radio_button(label="radio",items= ip_addresses, tag="radio",show=False,callback=selectIp)

            dpg.add_radio_button(show=False)
            

def page2_callback(sender,app_data):
    global default,currentPage
    if currentPage!=2:
        currentPage=2
        if dpg.does_alias_exist("page1"):
            dpg.delete_item("page1", children_only=False)
        with dpg.window(label="A propos", width=1000, height=600,no_collapse=True,tag="page2",no_resize=True,no_move=True,no_close=True):  
            with dpg.menu_bar():
                with dpg.menu(label="Menu"):
                    dpg.add_menu_item(label="Configuration",callback= page1_callback)
                    dpg.add_menu_item(label="A propos")    
            dpg.add_text(default_value="Cette application permet de configurer les ip des differentes machines sans avoir a modifier les fichiers bash.",pos=(80,300))
            dpg.add_text(default_value="par Lafon Rafael, Suckiel Theo, Leroi Remi, Bertaud Nathan",pos=(20,530))
            
            

def verifyInput(sender,app_data,user_data):
    if verifyip(user_data)==False and (user_data==1 or user_data==2):
        dpg.show_item("notif"+user_data)
    elif verifyip(user_data)==True and (user_data==1 or user_data==2):
       dpg.hide_item("notif"+user_data)
    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)
        if user_data=="1":
                data["seedboxIP"]=dpg.get_value("input1")

        elif user_data=="2":
            data["PlexIP"]=dpg.get_value("input2")
        elif user_data=="3":
            data["PlexName"]=dpg.get_value("input3")
        elif user_data=="4":
            data["SeedName"]=dpg.get_value("input4")

        with open("config.json", "w") as jsonFile:
            json.dump(data, jsonFile)


    
def showIpSuggestion(sender,app_data):
    if dpg.is_item_shown("radio"):
        dpg.hide_item("radio")
    else:
        dpg.show_item("radio")

def selectIp(sender,app_data):
    dpg.set_value("input2",dpg.get_value("radio"))




def verifyip(user_data) :
    if user_data==1:
        address=dpg.get_value("input1")
    else:
         address=dpg.get_value("input2") 

    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False

    return True

    

def launch():
    global ip_addresses
    local_hostname = socket.gethostname()
    ip_addresses = socket.gethostbyname_ex(local_hostname)[2]
    page1_callback(None,None)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

launch()
