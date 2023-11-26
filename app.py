import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=1000, height=600)

with dpg.window(label="Configuration", width=1000, height=600,no_collapse=True):
    dpg.add_input_text(label="ip de la seedbox")
    dpg.add_text()
    dpg.add_input_text(label="ip du serveur plex")
    dpg.add_text()
    

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()