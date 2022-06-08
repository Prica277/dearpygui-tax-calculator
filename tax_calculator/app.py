# app.py - My DearPyGui windowed app.
import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Sales Tax Calculator', width=600, height=300)

with dpg.window(label="Example Window": width=600, height=300):
    dpg.add_text("Welcome to the Sales Tax Calculator")
    dpg.add_input_float(label="Tax Rate")
    dpg.add_input_float(label="Price")
    dpg.add_button(label="Calculate")
    dpg.add_button(label="Clear")


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()