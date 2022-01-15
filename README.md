# DGN-Monitor-Python-FOCAS
Its DGN Monitor for FANUC system 0i F &amp; 31iB series to monitor diagnosis data (temp, error bits, rpm, load) on PMC signal or at interval & data stored in csv file


TOOL REQUIREMENTS: 
1.	Ethernet Cable
2.	PC/ Laptop – With 64Bit Processor –Windows System
3.	Application DGN Monitor – Main.exe/ Project

Procedure
•	Connect System with Laptop/PC via Ethernet Cable. Established connection with CNC. Its same procedure to connect with Servo guide.
Note: 
o	If Communication not established even if ping is healthy try to restart CNC & Your PC then Try once again. 
o	CNC & PC IP address should be different ex. 198.168.1.1 CNC then PC 192.168.1.0. 

•	Open main.exe in PC, it will show below screen. Press Start Here.
•	Input IP & Port (if you don’t input port it will take as 8193) then press connect to check connection is healthy. Its will show in process monitor.  
•	In this you can monitor total 3 DGN value if you enter 0 in DGN it won’t be checked considered as NIL. Enter DGN value & enter Axis number and press Check DGN button. In process monitor it will show Data received from CNC is Ok or if data not good it will show error. Example screen.
 
Note:
o	Check which kind of DGN data you can read in this application at end of Document.

•	This application can be run by M Code/PMC for the same in this given R bits for Read & Write. If you want to check at particular program line or at PMC signal. Enter R read Address & check that particular address data via check button. Check R Write address button for confirmation signal or M code Fin signal.
o	In write it will set R address to =1 Decimal so (0000001)
o	In Read it will read R address by decimal value.  

Note: 
o	if you use M code/PMC based DGN data capture  never use Read &  Write value same. 
o	Don’t use enterd R Addres for other fuctionsin PMC as in data caputure if Read address value is 1 then only it will capture data & In punch value write to 1 Decimal in Bit (00000001).
o	In FOCAS we can’t write/punch system internal R bits that start after R9000. 
 
•	Enter how much time you need to capture DGN data in T (In min). 
•	In This DGN monitor you can use total Two Modes.

o	For Auto by R(M-code/PMC)
	It will run for T time when ever R Read is ON (00000001 bn, 1 d) then it will write data in CSV file and gives feedback to CNC via R Punch address to ON(00000001 bn,  1 d). On CNC need to reset R punch address to 0 after M code or PMC feedback signal received.
	Things to be entered
•	IP & Port 
•	DGN value need to monitor (DGN & Axis)
•	R Read & Punch Value 
•	Time to Run (In Min)

o	For Auto by Time Interval(Time)
	It will run for T time and it will take data at interval of T Interval time entered in application (In sec) and store DGN data in CSV file that is selected.
	Things to be entered
•	IP & Port 
•	DGN value need to monitor (DGN & Axis)
•	Time to Run (In Min)
•	Time Interval (In sec)
•	Select CSV file to store via selecting button. 

Note: 
o	You can only select CSV file, you need to create one first.
o	If selected file having some data that will be erased then its will start capturing data
o	At Every Selection of csv file already stored data will be erased. Do not open file during Auto or manual entry.

•	In this you can also take manual data via pressing manual in button.
           	-First Connect to CNC  - Enter DGN & Axis  - Select Which File Store
•	Press Manual In – At every data stored it will show in screen. 
•	If you press start Button It will start capturing data Based on Entry Value. Things to require  to start Auto 

On Application Inputs	Explain
IP address & Port	                                                  For connecting CNC
DGN Value & Axis No	                                                Which DGN need to Monitor
T time for Auto mode (min)	                                        How much time data need to capture
Select CSV	                                                        For Storing data
Auto By R mode	    Auto by time interval	                          Select Mode via Drop Down
R read & R write	  T interval time (sec)	
Press Start 	                                                      For Cycle Start
Press Stop (if required)	                                          For cycle stop

Note:
o	For Auto by R mode need to change PMC as mentioned in Mode. (It will read R continuously if data = 1 then give feed to CNC via R punch & store DGN data in csv file, Also need to make R punch address to 0 via CNC only)
o	For auto by interval no need change at CNC. It will take data at time interval as per T interval (in sec)
•	After Completion Please Check CSV file. 
 

DGN CAN BE MONITORED
In DGN	In Axis 	    CNC of with axis		Data condition
______________________________________________________________________
319 ( Axis  example) #   1 = X2 = Y3 = Z	# 	Output as value in cnc
411 ( SP Example)	 #   1 = S1 2 = S2	 	#	Output as value in cnc
45 (without Axis)    #   0 or -1	 	    #  	Output as value in cnc
1007 without Axis/SP)#	0 or -1	 	        #   Output as Decimal
1774                 # 	1,2,3 = x,y,z       #   Output as Decimal
1775                 #   1,2=s1 s           #   Output as Decimal
 
Note 
: "-"Negative DGN Value , 0.000 DGN Value, Hexa DGN Value will Be not Ok Value
: Desimal Vaule, Bit value (As Decimal) will be GOOD Condition.


•	For Auto By R Mode: PMC example 

EXAMPLE FOR R BY AUTO
Input Required: IP – Port – DGN – Axis 
R Read – 250 
R Punch – 260
Select CSV file
MCODE M50: Generated in CNC Used R 250 as Read & R 260 as fin signal
When Ever M50 is called Data DGN data will be stored.  Note Here after FIN we resetting R260 to 0 via CNC ONLY OTHER VISE IN NEXT MCODE CALL DATA WON'T BE STAORED AS MCODE FINISH QUICKLY.

Notes:
•	you can only use 4 Max Axis value can be used or can be return
•	Multipath System Not tested
•	For Any Bugs or improvement please give feedback.

