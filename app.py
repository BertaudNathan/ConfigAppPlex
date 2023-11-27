import dearpygui.dearpygui as dpg
import socket

global currentPage,default

currentPage=1
default=True


dpg.create_context()
dpg.create_viewport(title='Custom Title', width=1000, height=600,resizable=False)

def page1_callback(sender,app_data):
    global default,currentPage
    if currentPage!=1 or default==True:
        currentPage=1
        default=False
        if dpg.does_alias_exist("page2"):
            dpg.remove_alias("page2")
        with dpg.window(label="Configuration", width=1000, height=600,no_collapse=True,tag="page1",no_resize=True,no_move=True,no_close=True):
            dpg.add_input_text(label="ip de la seedbox",tag="input1")
            dpg.add_text(default_value="l'ip est invalide",tag="notif1",show=False,color=(255,0,0))
            dpg.add_button(label="submit",callback=verifyInput,user_data="1")
            dpg.add_input_text(label="ip du serveur plex",tag="input2")
            dpg.add_text(default_value="l'ip est invalide",tag="notif2",show=False,color=(255,0,0))
            dpg.add_button(label="submit",callback=verifyInput,user_data="2")
            with dpg.menu_bar():
                with dpg.menu(label="Menu"):
                    dpg.add_menu_item(label="Configuration")
                    dpg.add_menu_item(label="A propos", callback=page2_callback)

def page2_callback(sender,app_data):
    global default,currentPage
    if currentPage!=2:
        currentPage=2
        if dpg.does_alias_exist("page1"):
            dpg.remove_alias("page1")
        with dpg.window(label="A propos", width=1000, height=600,no_collapse=True,tag="page2",no_resize=True,no_move=True,no_close=True):  
            dpg.add_text(default_value="Cette application permet de configurer les ip des differentes machines sans avoir a modifier les fichiers bash.",pos=(80,300))
            dpg.add_text(default_value="par Lafon Rafael, Suckiel Theo, Leroi Remi, Bertaud Nathan",pos=(20,530))
            
            with dpg.menu_bar():
                with dpg.menu(label="Menu"):
                    dpg.add_menu_item(label="Configuration",callback= page1_callback)
                    dpg.add_menu_item(label="A propos")    

def verifyInput(sender,app_data,user_data):
    print("notif"+user_data)
    if verifyip(user_data)==False:
        dpg.show_item("notif"+user_data)
    else:
       dpg.hide_item("notif"+user_data)
    



def verifyip(user_data) :
    if user_data==1:
        address=dpg.get_value("input1")
    else:
         address=dpg.get_value("input2") 
    print(address)
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
    page1_callback(None,None)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

launch()
