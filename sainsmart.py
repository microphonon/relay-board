########################################################
#                                                      #
#    SainSmart 16-channel USB Relay Board Controller   #
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
        ser = serial.Serial(port=sp, baudrate=9600, timeout=1)
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
    
# The binary commands were found on the SainSMART wiki
    if index1 == 0: 
        hex_string = b':FE050000FF00FE\r\n' # Relay 1 selected    
    else:
        hex_string = b':FE0500000000FD\r\n' # Else turn it off
    ser.write(hex_string) 
        
    if index1 == 1: # Relay 2 selected
        hex_string = b':FE050001FF00FD\r\n'     
    else:
        hex_string = b':FE0500010000FC\r\n'
    ser.write(hex_string)
        
    if index1 == 2: # Relay 3 selected
        hex_string = b':FE050002FF00FC\r\n'     
    else:
        hex_string = b':FE0500020000FB\r\n'
    ser.write(hex_string)
   
    if index1 == 3: # Relay 4 selected
        hex_string = b':FE050003FF00FB\r\n'     
    else:
        hex_string = b':FE0500030000FA\r\n'
    ser.write(hex_string)
        
    if index1 == 4: # Relay 5 selected
        hex_string = b':FE050004FF00FA\r\n'     
    else:
        hex_string = b':FE0500040000F9\r\n'
    ser.write(hex_string)
        
    if index1 == 5: # Relay 6 selected
        hex_string = b':FE050005FF00F9\r\n'       
    else:
        hex_string = b':FE0500050000F8\r\n'
    ser.write(hex_string)
        
    if index1 == 6: # Relay 7 selected
        hex_string = b':FE050006FF00F8\r\n'      
    else:
        hex_string = b':FE0500060000F7\r\n'
    ser.write(hex_string)
        
    if index1 == 7: # Relay 8 selected
        hex_string = b':FE050007FF00F7\r\n'      
    else:
        hex_string = b':FE0500070000F6\r\n' 
    ser.write(hex_string) 
    
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
        hex_string = b':FE050008FF00F6\r\n' # Relay 9 selected     
    else:
        hex_string = b':FE0500080000F5\r\n' # Else turn it off
    ser.write(hex_string)
        
    if index2 == 9: # Relay 10 selected
        hex_string = b':FE050009FF00F5\r\n'      
    else:
        hex_string = b':FE0500090000F4\r\n'
    ser.write(hex_string)
        
    if index2 == 10: # Relay 11 selected
        hex_string = b':FE05000AFF00F4\r\n'       
    else:
        hex_string = b':FE05000A0000F3\r\n'
    ser.write(hex_string)
   
    if index2 == 11: # Relay 12 selected
        hex_string = b':FE05000BFF00F3\r\n'
        ser.write(hex_string)       
    else:
        hex_string = b':FE05000B0000F2\r\n'
    ser.write(hex_string)
        
    if index2 == 12: # Relay 13 selected
        hex_string = b':FE05000CFF00F2\r\n'    
    else:
        hex_string = b':FE05000C0000F1\r\n'
    ser.write(hex_string)
        
    if index2 == 13: # Relay 14 selected
        hex_string = b':FE05000DFF00F1\r\n'    
    else:
        hex_string = b':FE05000D0000F0\r\n'
    ser.write(hex_string)
        
    if index2 == 14: # Relay 15 selected
        hex_string = b':FE05000EFF00F0\r\n'      
    else:
        hex_string = b':FE05000E0000FF\r\n'
    ser.write(hex_string)
        
    if index2 == 15: # Disable all relays 
        hex_string = b':FE0F00000010020000E1\r\n' # Convenient global command
        ser.write(hex_string)
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
