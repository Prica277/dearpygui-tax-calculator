# app.py - My DearPyGui windowed app.
import dearpygui.dearpygui as dpg

dpg.create_context()
rate_id = dpg.generate_uuid()
price_id = dpg.generate_uuid()
output_id = dpg.generate_uuid()

def get_price():
    rate = dpg.get_value(rate_id)
    rate = round(rate, 3)
    price = dpg.get_value(price_id)
    sales_tax = calculate_sales_tax(rate, price)
    output= get_output(price, rate, sales_tax)
    dpg.set_value(output_id, output)

def calculate_sales_tax(p, r):
    #selling price x sales tax rate = sales tax, then selling price + sales tax = total price
    return p + p * r

def get_output(p, r, st):
    output = "With a price of ${}".format(p)
    output = "\nand a sales tax rate of {}".format(r)
    output = "\nThe total price is ${}".format(st)
    return output

dpg.create_viewport(title='Sales Tax Calculator', width=600, height=300)

with dpg.window(label="Sales Tax Calculator", width=600, height=300) :
    dpg.add_text("Welcome to the Sales Tax Calculator")
    dpg.add_input_float(label="Tax Rate", width=100, tag=rate_id, min_value=0, min_clamped=True, default_value=0)
    dpg.add_input_float(label="Price", width=100, tag=price_id, min_value=0, min_clamped=True, default_value=0)
    dpg.add_button(label="Calculate", callback=get_price)
    dpg.add_button(label="Clear")
    dpg.add_text("", tag=output_id)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()