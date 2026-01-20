# relay-board
Graphical User Interfaces for SainSMART (sainsmart.py) and LCUS (lcus.py) 16-channel serial relay boards

<p>Stand-alone python GUIs for 16-channel relay boards from two different Chinese suppliers. The specific board can be identified in the photos below. There are no manufacturer model numbers and documentation for this hardware is almost non-existent. The needed hex command strings, however, were obtained from various online sources including reddit forums. If your board doesn't match either of the photos, the code in this repo is highly unlikely to work. 
  
<p>Install `pyserial`, `tk-tools`, and possibly a driver for the CH-340 USB-serial interface. A USB interface cable (either Type-B or C depending on model) provides communication and board power. Use the jumpers to select the USB interface; an external DC power connection is <b>not needed</b>. I have no idea how to configure the COM option. Serial port selection on the host is made using the button and Entry Box at the top of the GUI. 

<p>This code was developed for an amateur radio antenna selector using Linux, python3, and tkinter running from the terminal. There should be enough information in the comments to adapt for other platforms and applications. In this application, there are two banks of relays in separate, color-coded columns. BANK 1 uses Relays 1--8 and BANK 2 uses Relays 9--15. Only one relay per bank can be selected, i.e. there are only two relays active simultaneously. 

<p>The primary difference between the two programs involves the hex command set and serial communication. The LCUS hardware automatically returns a response on the bus after every command, requiring that a short delay be inserted or communication will fail. Some diagnostic information is sent to the terminal; disable these as desired. There are certainly more compact and elegant ways to code this, but I wanted to make it transparent and easy to follow.


![GUI](GUIb.jpg)

![hardware](relay_board_1.jpg)

![hardware](relay_board_2.jpg)



