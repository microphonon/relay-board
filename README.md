# relay-board
GUI for 16-channel SainSMART serial relay board

<p>Stand-alone python GUI for a 16-channel SainSMART relay board as shown in the image below. There is no manufacturer model number and documentation for this hardware is almost non-existent, but the needed hex command strings were found on the SainSMART wiki page. Install pyserial and possibly a driver for the CH-340 USB-serial interface. A Type-B USB interface cable provides communication and board power. Use the jumper to select the USB interface; the external DC power connection is not needed. I have no idea how to configure the COM option.

<p>This code was developed for an amateur radio application using Linux. There should be enough information in the comments to adapt it for other platforms and uses. In this application, there are two banks of relays. BANK 1 uses Relays 1--8 and BANK 2 uses Relays 9--15. Only one relay per bank can be selected, i.e. there are only two relays active simultaneously. Serial port selection is made using the button and Entry Box at the top of the GUI. 

<p>There are certainly more compact and elegant ways to code this, but I wanted to make it transparent and easy to follow.


![GUI](GUIb.jpg)

![hardware](relay_board.jpg)



