# app.py - My DearPyGui windowed app.
import dearpygui.dearpygui as dpg

dpg.create_context()
rate_id = dpg.generate_uuid()
price_id = dpg.generate_uuid()
output_id = dpg.generate_uuid()

def callback():
    print("Rate ID: " + str(dpg.get_value(rate_id)))

dpg.create_viewport(title='Sales Tax Calculator', width=600, height=300)

with dpg.window(label="Example Window", width=600, height=300) :
    dpg.add_text("Welcome to the Sales Tax Calculator")
    dpg.add_input_float(label="Tax Rate", width=100, tag=rate_id)
    dpg.add_input_float(label="Price", width=100, tag=price_id)
    dpg.add_button(label="Calculate", callback=callback)
    dpg.add_button(label="Clear")
    dpg.add_text("", tag=output_id)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()