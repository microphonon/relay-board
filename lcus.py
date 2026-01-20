########################################################
#                                                      #
#    LCUS-16 16-channel USB Relay Board Controller     #
#                                                      #
#    WB2FKO mph@sportscliche.com                       #
#    January 2026                                      #
#                                                      #
########################################################

import tkinter as tk
import tk_tools as tkt
import tkinter.font as tkFont
from tkinter import messagebox
import serial
import time

root = tk.Tk()
root.title("Relay Board Controller by WB2FKO")

buttons = []        
current_active_button_1 = None
current_active_button_2 = None
index2 = 99 # Set a dummy index value at startup

# Read serial port entry on front panel and place on top of first column   
serial_port = tk.Entry(root, bd=3, width=15, bg="white", relief=tk.SUNKEN)
serial_port.grid(row=1, column=0, padx=3, pady=3)
serial_port.insert(0, "/dev/ttyUSB0") # Sets the default serial port; replace with eg. COM3 on Windows
#label = tk.Label(root, text="Serial Port:")
#label.grid(row=0, column=0, sticky="s", padx=3, pady=0)

# Configure serial port
def config_serial():
    global sp
    global ser
    try:
        sp = serial_port.get()
        ser = serial.Serial(
            port=sp, 
            baudrate=9600, 
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
        )
        time.sleep(2) # Give the port some time to initialize
        print("Serial port opened successfully.")
        set_serial.config(text='CONNECTED', bg='lawn green')
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        ser = None # Handle cases where serial port is unavailable
        set_serial.config(text='RESET', bg='red')
        messagebox.showerror("SERIAL PORT ERROR", "The relay board is not communicating with this computer. Enter the correct serial port and/or check the USB connection, then press the RESET button.")

# Place a button to change serial port   
set_serial = tk.Button(root, width=12, text="Reset Serial Port", command=config_serial)
set_serial.grid(row=0, column=0, padx=0, pady=3)

# Try to configure serial port at startup 
root.after_idle(config_serial)     

# Action of Column 1 button. Only one relay can be active
def on_button_click_1(clicked_button):
    global current_active_button_1
    global index1
        
    # Revert the appearance of the previously active button
    if current_active_button_1:
        current_active_button_1.config(relief=tk.RAISED, bd=2, bg='LightGoldenrod1')

    # Set the appearance of the newly clicked button
    clicked_button.config(relief=tk.SUNKEN, bd=3, bg='lawn green')
    current_active_button_1 = clicked_button
    
    # Use index1 to track the value of Bank 1 button
    index1 = buttons.index(clicked_button)
    print(f"Bank 1 at index {index1} is active.")
    
# Syntax: xA0, Relay Identifier (1--16), State (ON x01, OFF x00), Checksum of first 3 bytes
    if index1 == 0: 
         hex_string = b'\xA0\x01\x01\xA2' # Relay 1 selected    
    else:
        hex_string = b'\xA0\x01\x00\xA1' # Else turn it off
    ser.write(hex_string)
    time.sleep(0.1) # Wait for response 
        
    if index1 == 1: # Relay 2 selected
        hex_string = b'\xA0\x02\x01\xA3'    
    else:
        hex_string = b'\xA0\x02\x00\xA2'
    ser.write(hex_string)  
    time.sleep(0.1) # Wait for response
      
    if index1 == 2: # Relay 3 selected
        hex_string = b'\xA0\x03\x01\xA4'      
    else:
        hex_string = b'\xA0\x03\x00\xA3'
    ser.write(hex_string)  
    time.sleep(0.1) # Wait for response
   
    if index1 == 3: # Relay 4 selected
        hex_string = b'\xA0\x04\x01\xA5'     
    else:
        hex_string = b'\xA0\x04\x00\xA4'
    ser.write(hex_string)  
    time.sleep(0.1) # Wait for response
        
    if index1 == 4: # Relay 5 selected
        hex_string = b'\xA0\x05\x01\xA6'      
    else:
        hex_string = b'\xA0\x05\x00\xA5'
    ser.write(hex_string)  
    time.sleep(0.1) # Wait for response
        
    if index1 == 5: # Relay 6 selected
        hex_string = b'\xA0\x06\x01\xA7'    
    else:
        hex_string = b'\xA0\x06\x00\xA6'
    ser.write(hex_string)  
    time.sleep(0.1) # Wait for response
        
    if index1 == 6: # Relay 7 selected
        hex_string = b'\xA0\x07\x01\xA8'       
    else:
        hex_string = b'\xA0\x07\x00\xA7'
    ser.write(hex_string)  
    time.sleep(0.1) # Wait fo response
        
    if index1 == 7: # Relay 8 selected
        hex_string = b'\xA0\x08\x01\xA9'    
    else:
        hex_string = b'\xA0\x08\x00\xA8'
    ser.write(hex_string)  
    time.sleep(0.1) # Wait for response
    
    # Any relay selected in Bank 1 unsets "Disable All" button in Bank 2
    if index2 == 15:
        current_active_button_2.config(relief=tk.RAISED, bg='aquamarine')
    
# Action of Column 2 button. Only one relay can be active    
def on_button_click_2(clicked_button):
    global current_active_button_2
    global index2
   
    # Revert the appearance of the previously active button
    if current_active_button_2:
        current_active_button_2.config(relief=tk.RAISED, bd=2, bg='aquamarine')

    # Set the appearance of the newly clicked button
    clicked_button.config(relief=tk.SUNKEN, bd=3, bg='lawn green')
    current_active_button_2 = clicked_button
    
    # Use index2 to track the value associated with the Bank 2 button
    index2 = buttons.index(clicked_button)
    print(f"Bank 2 at index {index2} is active.")
     
    if index2 == 8: 
        hex_string = b'\xA0\x09\x01\xAA' # Relay 9 selected     
    else:
        hex_string = b'\xA0\x09\x00\xA9' # Else turn it off
    ser.write(hex_string)  
    time.sleep(0.1) # Wait for response
        
    if index2 == 9: # Relay 10 selected
        hex_string = b'\xA0\x0A\x01\xAB'    
    else:
        hex_string = b'\xA0\x0A\x00\xAA'
    ser.write(hex_string)  
    time.sleep(0.1) # Wait for response
        
    if index2 == 10: # Relay 11 selected
        hex_string = b'\xA0\x0B\x01\xAC'     
    else:
        hex_string = b'\xA0\x0B\x00\xAB'
    ser.write(hex_string)  
    time.sleep(0.1) # Wait for response
   
    if index2 == 11: # Relay 12 selected
        hex_string = b'\xA0\x0C\x01\xAD'     
    else:
        hex_string = b'\xA0\x0C\x00\xAC'
    ser.write(hex_string)  
    time.sleep(0.1) # Wait for response
        
    if index2 == 12: # Relay 13 selected
        hex_string = b'\xA0\x0D\x01\xAE'    
    else:
        hex_string = b'\xA0\x0D\x00\xAD'
    ser.write(hex_string)  
    time.sleep(0.1) # Wait for response
        
    if index2 == 13: # Relay 14 selected
        hex_string = b'\xA0\x0E\x01\xAF'    
    else:
        hex_string =b'\xA0\x0E\x00\xAE'
    ser.write(hex_string)  
    time.sleep(0.1) # Wait for response
        
    if index2 == 14: # Relay 15 selected
        hex_string = b'\xA0\x0F\x01\xB0'     
    else:
        hex_string = b'\xA0\x0F\x00\xAF'
    ser.write(hex_string)  
    time.sleep(0.1) # Wait for response
        
    if index2 == 15: # Disable all relays
       # Column 1 relays must be turned off individually
        hex_string = b'\xA0\x01\x00\xA1'
        ser.write(hex_string) 
        time.sleep(0.1)
        hex_string = b'\xA0\x02\x00\xA2'
        ser.write(hex_string) 
        time.sleep(0.1)
        hex_string = b'\xA0\x03\x00\xA3'
        ser.write(hex_string) 
        time.sleep(0.1)
        hex_string = b'\xA0\x04\x00\xA4'
        ser.write(hex_string) 
        time.sleep(0.1)
        hex_string = b'\xA0\x05\x00\xA5'
        ser.write(hex_string) 
        time.sleep(0.1)
        hex_string = b'\xA0\x06\x00\xA6'
        ser.write(hex_string) 
        time.sleep(0.1)
        hex_string = b'\xA0\x07\x00\xA7'
        ser.write(hex_string) 
        time.sleep(0.1)
        hex_string = b'\xA0\x08\x00\xA8'
        ser.write(hex_string) 
        time.sleep(0.1)
        
        # Column 2 relays can be turned off with these two combined commands   
        hex_string = b'\xA0\x09\x00\xA9\xA0\x0A\x00\xAA\xA0\x0B\x00\xAB\xA0\x0C\x00\xAC'
        ser.write(hex_string) 
        time.sleep(0.1)
        hex_string = b'\xA0\x0D\x00\xAD\xA0\x0E\x00\xAE\xA0\x0F\x00\xAF'
        ser.write(hex_string)
        time.sleep(0.1)
         
        # Reset Column 1 button
        current_active_button_1.config(relief=tk.RAISED, bg='LightGoldenrod1')   
        
# Place a blank row for vertical space
label = tk.Label(root, text=" ") 
label.grid(row=2, column=0, padx=0, pady=10)  

label = tk.Label(root, text=" ") 
label.grid(row=2, column=1, padx=0, pady=0) 

# Set column labels as MAIN RX and 2nd RX        
bank_font = tkFont.Font(family="Helvetica", size=14, weight="bold") 

label = tk.Label(root, text="MAIN RX", font=bank_font) 
label.grid(row=3, column=0, sticky="s", padx=0, pady=0)  

label = tk.Label(root, text="2nd RX", font=bank_font) 
label.grid(row=3, column=1, sticky="s", padx=0, pady=0)  
  
# Configure rows to NOT resize with the window
for i in range(11):
    root.rowconfigure(i, weight=0)
# Configure columns to resize with the window
for i in range(2):
    root.columnconfigure(i, weight=1)
       
# Place and configure the buttons in BANK 1
button = tk.Button(root, text=f"SW", width=10, height=2)
button.config(bg="LightGoldenrod1",command=lambda b=button: [on_button_click_1(b)]) 
buttons.append(button)
button.grid(row=4, column=0, padx=5, pady=5)

button = tk.Button(root, text=f"WEST", width=10, height=2)
button.config(bg="LightGoldenrod1",command=lambda b=button: [on_button_click_1(b)]) 
buttons.append(button)
button.grid(row=5, column=0, padx=5, pady=5)

button = tk.Button(root, text=f"NW", width=10, height=2)
button.config(bg="LightGoldenrod1",command=lambda b=button: on_button_click_1(b)) 
buttons.append(button)
button.grid(row=6, column=0, padx=5, pady=5)

button = tk.Button(root, text=f"NORTH", width=10, height=2)
button.config(bg="LightGoldenrod1",command=lambda b=button: on_button_click_1(b)) 
buttons.append(button)
button.grid(row=7, column=0, padx=5, pady=5)

button = tk.Button(root, text=f"NE", width=10, height=2)
button.config(bg="LightGoldenrod1",command=lambda b=button: on_button_click_1(b)) 
buttons.append(button)
button.grid(row=8, column=0, padx=5, pady=5)

button = tk.Button(root, text=f"EAST", width=10, height=2)
button.config(bg="LightGoldenrod1",command=lambda b=button: on_button_click_1(b)) 
buttons.append(button)
button.grid(row=9, column=0, padx=5, pady=5)

button = tk.Button(root, text=f"SE", width=10, height=2)
button.config(bg="LightGoldenrod1",command=lambda b=button: on_button_click_1(b)) 
buttons.append(button)
button.grid(row=10, column=0, padx=5, pady=5)

button = tk.Button(root, text=f"AUX 1", width=10, height=2)
button.config(bg="LightGoldenrod1",command=lambda b=button: on_button_click_1(b)) 
buttons.append(button)
button.grid(row=11, column=0, padx=5, pady=5)

# Place and configure the buttons in BANK 2
button = tk.Button(root, text=f"VERTICAL", width=10, height=2)
button.config(bg="aquamarine", command=lambda b=button: on_button_click_2(b)) 
buttons.append(button)
button.grid(row=4, column=1, padx=5, pady=5)

button = tk.Button(root, text=f"SW", width=10, height=2)
button.config(bg="aquamarine", command=lambda b=button: on_button_click_2(b)) 
buttons.append(button)
button.grid(row=5, column=1, padx=5, pady=5)

button = tk.Button(root, text=f"NW", width=10, height=2)
button.config(bg="aquamarine", command=lambda b=button: on_button_click_2(b)) 
buttons.append(button)
button.grid(row=6, column=1, padx=5, pady=5)

button = tk.Button(root, text=f"NE", width=10, height=2)
button.config(bg="aquamarine", command=lambda b=button: on_button_click_2(b)) 
buttons.append(button)
button.grid(row=7, column=1, padx=5, pady=5)

button = tk.Button(root, text=f"SE", width=10, height=2)
button.config(bg="aquamarine", command=lambda b=button: on_button_click_2(b)) 
buttons.append(button)
button.grid(row=8, column=1, padx=5, pady=5)

button = tk.Button(root, text=f"DIPOLE", width=10, height=2)
button.config(bg="aquamarine", command=lambda b=button: on_button_click_2(b)) 
buttons.append(button)
button.grid(row=9, column=1, padx=5, pady=5)

button = tk.Button(root, text=f"AUX 2", width=10, height=2)
button.config(bg="aquamarine", command=lambda b=button: on_button_click_2(b)) 
buttons.append(button)
button.grid(row=10, column=1, padx=5, pady=5)

button = tk.Button(root, text=f"ALL OFF", width=10, height=2)
button.config(bg="aquamarine", command=lambda b=button: on_button_click_2(b)) 
buttons.append(button)
button.grid(row=11, column=1, padx=5, pady=5)

# Close serial port
def on_closing():
    if ser and ser.isOpen():
        ser.close() # Close the port when the window is closed
        print("Serial port closed.")
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing) # Bind the closing handler

# Start the Tkinter event loop
root.mainloop()
