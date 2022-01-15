 # ctypes -FOCAS only support via C C++ .Net to convert in py used Ctypes
 # threading -for two process run
 # time -taking system internal time
 # Support -call fuction from other py named "support"
 # csv - to do csv file operation 
import csv,tkinter,threading,time,support

import tkinter as tk  # GUI library 
from tkinter.ttk import * # Gui Design Lib
from tkinter import ttk
from tkinter import filedialog   # cvs file opner filedialog
from datetime import datetime # datetime 
from tkinter.scrolledtext import ScrolledText # in GUI scrolledtext
from PIL import Image, ImageTk
import tkinter.font as font

stop_event = threading.Event()

LARGEFONT = ("calibri", 40)


class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0)
        container.grid_columnconfigure(0)
  
        # initializing frames to an empty array
        self.frames = {} 
        self.title('DGN Monitor')   # GUI Title
        self.geometry("800x400")    # GUI App Window Size
                
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="white")

        # Start Image
        global startimage
        bg = Image.open("image\main.png")
        bg = bg.resize((533, 400), Image.ANTIALIAS)
        startimage = ImageTk.PhotoImage(bg)
        panel = tk.Label(self, image=startimage, highlightthickness = 0,borderwidth=0,  wraplength = 230)
        panel.grid(row = 0,rowspan= 40, column = 0)

        # label DGN Monitor
        label = ttk.Label(self, text ="DGN", font = LARGEFONT, background="white" )
        label1 = ttk.Label(self, text ="MONITOR", font = LARGEFONT, background="white") 

        ttk.Label(self, text ="     ", font = LARGEFONT, background="white" ).grid(padx=100, row =1,column=1)
        label.grid(row = 8, column = 1,sticky = tk.NW)
        label1.grid(row = 9, column = 1,sticky=tk.NW)
        myFont = font.Font(size=15)

        # button Start Here
        button1 = tk.Button(self, text ="Start Here!",relief="flat",
                            bg= "#4ABDAC", 
                            activebackground='White',
                            fg='white',
                            height=1, width=9,
                            command = lambda : controller.show_frame(Page1))
        button1['font']= myFont
        button1.grid(row = 16, column = 1, sticky=tk.NW)    
  
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)

        self.configure(bg="white")
        
        # Connect labale, IP & PORT enetry 
        myFont = font.Font(size=15)
        label = ttk.Label(self, text ="Connect", font = "calibri",
                        background="white")
        label['font']= myFont
        label.grid(row = 0, column = 0,columnspan= 3,sticky=tk.NW, padx=20 )

        ipadd =tk.StringVar()
        ip = ttk.Label(self,text="IP",background="white").grid(row=1, column=0,sticky=tk.NW, padx=20)
        ipinput = tk.Entry(self,textvariable=ipadd, width=15)
        ipinput.grid(row=1, column=1, columnspan=2,sticky=tk.NW,)

        portnum = tk.StringVar()
        port = tk.Label(self,text="Port",background="white").grid(row=1, column=2)
        portinput = tk.Entry(self,textvariable=portnum, width=10)
        portinput.grid(row=1, column=3,sticky=tk.NW)

        # Button conn & disconn
        conn = tk.Button(self, text ="Connect", command = lambda:connect(self) , 
                                relief=tk.FLAT , 
                                bg= "#4ABDAC", fg='white',
                                activebackground='white').grid(row=1, column=4,sticky=tk.NW)
        disconn = tk.Button(self, text ="Disconnect", command =lambda : disconnect(self),
                                relief=tk.FLAT,
                                bg='#f78733', fg='white',
                                activebackground='white').grid(row=1, column=5,sticky=tk.NW)


        # DGN & Axis Input
        label1 = ttk.Label(self, text ="DGN-Axis Number", font = "calibri",
                        background="white")
        label1['font']= myFont
        label1.grid(row = 2, column = 0,columnspan= 3,sticky=tk.NW, padx=20,pady=10 )
        
        dgn1 = tk.IntVar()  # DGN 1
        dgnvalue1 = tkinter.Label(self,text="DGN 1",background="white").grid(row=3, column=0,sticky=tk.NW, padx=20)
        dgnvalueinput1 = tkinter.Entry(self,textvariable=dgn1, width=10)
        dgnvalueinput1.grid(row=3, column=1,sticky=tk.NW)

        dgn2 = tk.IntVar() # DGN 2
        dgnvalue2 = tkinter.Label(self,text="2nd",background="white").grid(row=3, column=2)
        dgnvalueinput2 = tkinter.Entry(self,textvariable=dgn2, width=10)
        dgnvalueinput2.grid(row=3, column=3,sticky=tk.NW)

        dgn3 = tk.IntVar() # DGN 3
        dgnvalue3 = tkinter.Label(self,text="3rd",background="white").grid(row=3, column=4)
        dgnvalueinput3 = tkinter.Entry(self,textvariable=dgn3, width=10)
        dgnvalueinput3.grid(row=3, column=5,sticky=tk.NW)
        
        axisinput = tk.IntVar()
        axis = tkinter.Label(self,text="Axis 1",background="white").grid(row=5, column=0,sticky=tk.NW, padx=20)
        axisent = tkinter.Entry(self,textvariable=axisinput, width=10)
        axisent.grid(row=5, column=1,sticky=tk.NW)

        axisinput1 = tk.IntVar()
        axis1 = tkinter.Label(self,text="2nd",background="white").grid(row=5, column=2)
        axisent1 = tkinter.Entry(self,textvariable=axisinput1, width=10)
        axisent1.grid(row=5, column=3,sticky=tk.NW)

        axisinput2 = tk.IntVar()
        axis2 = tkinter.Label(self,text="3rd",background="white").grid(row=5, column=4)
        axisent2 = tkinter.Entry(self,textvariable=axisinput2, width=10)
        axisent2.grid(row=5, column=5,sticky=tk.NW)

        # DGN Check Button
        CheckDGN = tkinter.Button(self, text ="Check DGN", command =lambda : checkDGN(self) ,
                                relief=tk.FLAT,
                                bg= "#4ABDAC", fg='white',activebackground='white').grid(row=5, column=6,sticky=tk.NW)


        # R Mode R Read & R write
        label2 = ttk.Label(self, text ="Confirmation Signals by R - Auto", font = "calibri",
                        background="white")
        label2['font']= myFont
        label2.grid(row = 6, column = 0,columnspan= 5,sticky=tk.NW, padx=20,pady=10 )
        
        rininput = tk.IntVar()
        rin = tkinter.Label(self,text="Read",background="white").grid(row=7, column=0,sticky=tk.NW, padx=20)
        rinent = tkinter.Entry(self,textvariable=rininput, width=10)
        rinent.grid(row=7, column=1,sticky=tk.NW)
        
        rbitread = tkinter.Button(self, text ="Check", command =lambda : rread(self), 
                                relief=tk.FLAT,
                                bg= "#4ABDAC", fg='white',activebackground='white').grid(row=7, column=2,sticky=tk.NW)

        routinput = tk.IntVar()
        rout = tkinter.Label(self,text="Punch",background="white").grid(row=7, column=3,sticky=tk.NW, padx=20)
        routent = tkinter.Entry(self,textvariable=routinput, width=10)
        routent.grid(row=7, column=4,sticky=tk.NW)
        rbitwrite = tkinter.Button(self, text ="Check", command =lambda : rwrite(self), 
                                relief=tk.FLAT,
                                bg= "#4ABDAC", fg='white',activebackground='white'
                                ).grid(row=7, column=5)

        # time Entry & Drop down    
        label2 = ttk.Label(self, text ="Time for AutoMode in min", font = "calibri",
                        background="white")
        label2['font']= myFont
        label2.grid(row = 8, column = 0,columnspan= 4,sticky=tk.NW, padx=20,pady=10 )

        ar ="Auto By R(M-Code/PMC)"
        bt= "Auto By Time Interval(Time)"
        c ="   "
        options = [
            c,
            ar,
            bt,
            ]
        clicked = tk.StringVar()    
        clicked.set( "   " )
        drop = OptionMenu( self , clicked , *options )
        drop.grid(column=4, row =8,columnspan= 3,sticky=tk.W)

        tiinput = tk.IntVar()
        ti = tkinter.Label(self,text="T if Invertal",background="white").grid(row=9, column=3,columnspan=2 ,sticky=tk.NW, padx=20)
        tiinent = tkinter.Entry(self,textvariable=tiinput, width=10)
        tiinent.grid(row=9, column=4,sticky=tk.NW)
        tiinput.set(10)
        tkinter.Label(self,text="In Sec",background="white").grid(row=9, column=5,sticky=tk.NW,)

        tinput = tk.IntVar()
        t = tkinter.Label(self,text="Time to Run",background="white").grid(row=9, column=0,columnspan=2,sticky=tk.NW, padx=20)
        tinent = tkinter.Entry(self,textvariable=tinput, width=10)
        tinent.grid(row=9, column=1,sticky=tk.NW)
        tinput.set(2)
        tkinter.Label(self,text="In Min",background="white").grid(row=9, column=1,columnspan=2,sticky=tk.E,)

        # Start , Stop , Manual in & Selec CSV button & Process Monitor
        global play, sto, man,sav
        play = ImageTk.PhotoImage(file = "image\play.png")
        sto = ImageTk.PhotoImage(file = "image\stop.png")    
        cyc = tkinter.Button( self,text ="Start",image =play, command = lambda: threading.Thread(target = cycle,args=(self,)).start(),
                                relief=tk.FLAT,
                                bg='white', compound = tk.LEFT,
                                activebackground='white').grid(row=11 ,rowspan=2, column=8,) #Cycle Button

        stp = tkinter.Button( self, text ="Stop",image =sto, command =lambda :stop(self),
                                relief=tk.FLAT,
                                bg='white', compound = tk.LEFT,
                                activebackground='white').grid(row=11,rowspan=2, column=10,) #stop Button

        myFon = font.Font(size=8)
        label3 = ttk.Label(self, text ="Process Moni", font = "calibri",
                        background="white")
        label3['font']= myFon
        label3.grid(row = 0, column = 7,columnspan= 3,sticky=tk.NW)

        label4 = ttk.Label(self, text ="Data Saved - Timer", font = "calibri",
                        background="white")
        label4['font']= myFon
        label4.grid(row = 7, column = 7,columnspan= 2,sticky=tk.NW)

        label5 = ttk.Label(self, text ="                                                                                                                                                                                                       "
                        , font = "calibri",)
        label5.grid(row = 10, column = 0,columnspan= 13,sticky=tk.NW)                

        text= ScrolledText(self, width=35, height= 10)
        text.grid(row=1, column=7, rowspan= 6 ,columnspan=4)
        text1= ScrolledText(self, width=35, height= 3)
        text1.grid(row=8, column=7, rowspan= 2 ,columnspan=4)
        man = ImageTk.PhotoImage(file = "image\manual.png")
        Manual = tkinter.Button( self,text ="Manual In",image =man, command =lambda : manual(self) ,
                                relief=tk.FLAT,
                                bg='white', compound = tk.LEFT,
                                activebackground='white').grid(row=11, column=7,rowspan=2)
        sav = ImageTk.PhotoImage(file = "image\save.png")                       
        opencsv = tkinter.Button(self, text ="Save To", image =sav,command=lambda : csvopen(self),
                                relief=tk.FLAT,
                                bg='white', compound = tk.LEFT,
                                activebackground='white').grid(row=11, column=0,rowspan=2,columnspan=2 )
                       
        hour=tk.StringVar()
        minute=tk.StringVar()
        second=tk.StringVar()
        

        button3 = tk.Button(self, text ="Info Page",relief="flat",
                            bg= "#4ABDAC", 
                            activebackground='White',
                            fg='white',
                            command = lambda : controller.show_frame(Page2))
        button3.grid(row = 14, column = 10, sticky=tk.NW)
  
        # Timer Data
        hour.set("00")
        minute.set("00")
        second.set("00")
        hourEntry= Entry(self, width=3, font=("Arial",10,""),
                 textvariable=hour)
        minuteEntry= Entry(self, width=3, font=("Arial",10,""),
                   textvariable=minute)
        secondEntry= Entry(self, width=3, font=("Arial",10,""),
                   textvariable=second)   
        hourEntry.grid(row=7,column=10,columnspan=1,sticky=tk.NW)
        minuteEntry.grid(row=7,column=10,columnspan=1,sticky=tk.N)
        secondEntry.grid(row=7,column=10,columnspan=1,sticky=tk.NE)      
       
        self.num = 0
        def checkauto(self, *args, **kwargs):  # To check App running in auto mode or not
            if threading.activeCount() != 1:
                flag = True
                textwrite(self,"Auto Mode is On,Click stop")
            else:
                flag = False  
            return flag      

        def textwrite(self, string,*args , **kwargs):     # to Write on process Monitor
            text.insert(tkinter.INSERT,f"\n #{string}")
            text.see("end")
        def onscreenvalue(self, data,*args , **kwargs): # to write on Saved sata scrolled text
            self.num += 1
            text1.insert(tkinter.INSERT,f"\n #{self.num}-{data}")
            text1.see("end")
        def handlecheck(self):  # to check CNC connected or not
            try:
                print(libh)
                return True
            except:
                textwrite(self,f"Press Connect First or Handle Not good")
                return False
        def savefilechek(self): # to check File is saved or not
            try:
                print(filesave)
                return True
            except:
                textwrite(self,f"Selct CSV File First")
                return False                    
        
        def disconnect(self,*args , **kwargs):  # Dis -Connect to CNC via GUI button
            if checkauto(self) == False:
                handlecheck(self)    
                ret = support.disconnect(libh)
                if ret["ret"] == 0:
                    print ("Disconnected")
                    textwrite(self,"Disconnect Sussecfully,You can Close Application")
                else:
                    print (f"found Error {ret}")
                    textwrite(self,f"Found Error {ret}, Something went wrong")        

        def checkDGN(self,*args , **kwargs): # Read DGN value vai GUI Button
            if checkauto(self) == False: 
                handlecheck(self)
                dgn =int(dgn1.get())
                dg1 =int(dgn2.get())
                dg2 =int(dgn3.get())
                axis = int(axisinput.get())
                axis1 = int(axisinput1.get())
                axis2 = int(axisinput2.get())
                if dgn==0 and dg1==0 and dg2==0:
                    textwrite(self,"Enter DGN value")
                else:    
                    if dgn!=0:   
                        ret = support.readdgn(libh,dgn,axis)
                        r=ret["ret"]
                        if r !=0:
                            textwrite(self,f"1 NG data Er:{r}")
                            ret["value"] = f"ERR:{r}"
                    else:
                        ret={}
                        ret["value"]="NIL" 
                        ret["ret"]=0       
                    if dg1!=0:
                        ret1 = support.readdgn(libh,dg1,axis1)
                        r1=ret1["ret"]
                        if r1 !=0:
                            textwrite(self,"2 NG data Er:{r1}")
                            ret1["value"] = f"ERR:{r1}"
                    else:
                        ret1={}
                        ret1["value"]="NIL" 
                        ret1["ret"]=0       
                    if dg2!=0:
                        ret2 = support.readdgn(libh,dg2,axis2)
                        r2=ret2["ret"]
                        if ret2["ret"] !=0:
                            textwrite(self,"3 NG data Er:{r2}")
                            ret2["value"] = f"ERR:{r2}"
                    else:
                        ret2={}
                        ret2["value"]="NIL" 
                        ret2["ret"]=0

                    dt =[dgn,ret["value"],dg1,ret1["value"],dg2,ret2["value"]]
                    if ret["ret"] == 0 and ret2["ret"]==0 and ret1["ret"]==0:
                        print (f"Data recived {ret}")
                        textwrite(self,f"OK {dt} , Confirm With NC")
                    else:
                        print (f"Error {ret}") 
                        textwrite(self,f"NG Data- Enter Correct DGN & Axis or Other issue") 

        def rread(self,*args , **kwargs): # Read R Bit value vai GUI Button
            if checkauto(self) == False:
                handlecheck(self) 
                r = int(rininput.get())
                ret = support.readpmc(libh,r)
                if ret["ret"] == 0:
                    print (f"Data recived {ret}")
                    info =(f"OK Read {r}: {ret} in Decimal, Confirm With NC")
                    textwrite(self,info)
                else:
                    print (f"Error {ret}")
                    info =(f"Not Ok Read {ret} Enter Correct R or Other issue")
                    textwrite(self,info)  

        def rwrite(self,*args , **kwargs): # Write R Bit value vai GUI Button
            if checkauto(self) == False: 
                handlecheck(self)
                r = int(routinput.get())
                ret = support.writepmc(libh,r)
                if ret["ret"] == 0:
                    print (f"Data recived {ret}")
                    info =(f"Ok Write {r}=1 {ret}, Confirm With NC")
                    textwrite(self,info)
                else:
                    print (f"Error {ret}")
                    textwrite(self,f"Not ok Write {ret} Enter Correct R or Other issue")  

        def timer(self,t_end, *args, **kwargs): # On screen timer 
            print ("i am in timer")
            stop_event.clear()
            while time.time() < t_end:
                # Timer Screen 
                tdata =int(t_end- time.time())
                mins,secs = divmod(tdata,60)
                hours=0
                if mins >60:
                    # divmod(firstvalue = temp//60, secondvalue = temp%60)
                    hours, mins = divmod(mins, 60)
                hour.set("{0:2d}".format(hours))
                minute.set("{0:2d}".format(mins))
                second.set("{0:2d}".format(secs))
                time.sleep(0.5)
                self.update()
                if threading.activeCount() != 3: # at stop need to stop
                    print("Break as second tread colsed")
                    break
                if stop_event.is_set():
                    print("i am out of while")
                    break
            hour.set("00")
            minute.set("00")
            second.set("00")        


        def cycle(self,*args , **kwargs): # Start auto cycle 
            if threading.activeCount() >= 3 : 
                textwrite(self,"Auto Mode is On, Click Stop")
            else:                        
                print("i am in cycle")
                if savefilechek(self) == True:
                    ip= ipadd.get()      #take IP input form 
                    port= portnum.get()
                    t = int(tinput.get())
                    dgn =int(dgn1.get())
                    dg1 =int(dgn2.get())
                    dg2 =int(dgn3.get())
                    axis = int(axisinput.get())
                    axis1 = int(axisinput1.get())
                    axis2 = int(axisinput2.get())
                    ti = int(tiinput.get())
                    rin = int(rininput.get())
                    rout = int(routinput.get())
                    stop_event.clear()
                    dropdown =clicked.get()
                    if dropdown == c:
                        textwrite(self,"Select Mode in drop down")
                    else:
                        if dropdown == ar:
                            back = support.connect(ip,port)
                            libh = back["libh"]
                            if back["ret"] != 0 :
                                textwrite(self,"Auto Handle NG - Conn issue")
                            else:
                                t_end = time.time() + 60 * t   # t in Min time.time is system internal time

                                threading.Thread(target = timer,args=(self,t_end,)).start()
                                while time.time() < t_end:

                                        # read PMC
                                        ret = support.readpmc(libh,rin)
                                        print(ret)
                                        time.sleep(1.2)
                                        # read ok & value 1 
                                        if ret["value"] == 1 and ret["ret"]==0:
                                            if dgn==0 and dgn1==0 and dgn2==0: # if all DGN 0 so break
                                                textwrite(self,"No DGN Value- Break Auto")
                                                try:
                                                    ret = support.disconnect(libh)
                                                except:
                                                    textwrite(self,"Handle NG - Conn issue")   
                                                break
                                            else:
                                                now = datetime.now()
                                                if dgn!=0:   
                                                    ret0 = support.readdgn(libh,dgn,axis)
                                                    r=ret0["ret"]
                                                    if r !=0:
                                                        textwrite(self,f"1 NG data Er:{r} break auto")
                                                        try:
                                                            ret = support.disconnect(libh)
                                                        except:
                                                            textwrite(self,"Handle NG - Conn issue")
                                                        break
                                                else:
                                                    ret0={}
                                                    ret0["value"]="NIL"        
                                                if dg1!=0:
                                                    ret1 = support.readdgn(libh,dg1,axis1)
                                                    r1=ret1["ret"]
                                                    if r1 !=0:
                                                        textwrite(self,"2 NG data Er:{r1} break auto")
                                                        try:
                                                            ret = support.disconnect(libh)
                                                        except:
                                                            textwrite(self,"Handle NG - Conn issue")
                                                        break
                                                else:
                                                    ret1={}
                                                    ret1["value"]="NIL"        
                                                if dg2!=0:
                                                    ret2 = support.readdgn(libh,dg2,axis2)
                                                    r2=ret2["ret"]
                                                    if ret2["ret"] !=0:
                                                        textwrite(self,"3 NG data Er:{r2} break auto")
                                                        try:
                                                            ret = support.disconnect(libh)
                                                        except:
                                                            textwrite(self,"Handle NG - Conn issue")
                                                        break
                                                else:
                                                    ret2={}
                                                    ret2["value"]="NIL"                

                                                data = [now.strftime("%x"),now.strftime("%X"),dgn,axis,ret0["value"],dg1,axis1,ret1["value"],dg2,axis2,ret2["value"]]
                                                dt =[dgn,ret0["value"],dg1,ret1["value"],dg2,ret2["value"]]
                                                with open(filesave,'a',newline='') as csvfile:
                                                    csvwriter = csv.writer(csvfile)
                                                    csvwriter.writerow(data)
                                                    onscreenvalue(self,dt)
                                                    csvfile.close()
                                                    
                                                pmcwrtret = support.writepmc(libh, rout)
                                                if pmcwrtret["ret"]==0:
                                                    print(f"PMC write ok {rout}=1")
                                                else:
                                                    err =pmcwrtret["ret"]
                                                    print(f"Error Occured {err}")
                                                    textwrite(self,f"PMC Write Er:{err}-break auto")
                                                    try:
                                                            ret = support.disconnect(libh)
                                                    except:
                                                            textwrite(self,"Handle NG - Conn issue")
                                                    break
                                                time.sleep(0.2) # 0.2 sec sleep
                                        elif ret["ret"]!=0:
                                            textwrite(self,"PMC Read Not ok- Break Auto")
                                            try:
                                                ret = support.disconnect(libh)
                                            except:
                                                textwrite(self,"Handle NG - Conn issue")
                                            break        
                                        if stop_event.is_set():
                                            print("i am out of while")
                                            textwrite(self,"Cycle Stopped Check CSV File ")
                                            try:
                                                ret = support.disconnect(libh)
                                            except:
                                                textwrite(self,"Handle NG - Conn issue")
                                            break
                                print("i am out of while - Finnaly")
                                hour.set("00")
                                minute.set("00")
                                second.set("00")
                                try:
                                    ret = support.disconnect(libh)
                                except:
                                    textwrite(self,"Handle NG - Conn issue")
                        elif dropdown==bt:
                            back = support.connect(ip,port)
                            libh = back["libh"]
                            if back["ret"] != 0 :
                                textwrite(self,"Auto Handle NG - Conn issue")
                            else:
                                t_end = time.time() + 60 * t 
                                if dgn==0 and dgn1==0 and dgn2==0: # if all DGN 0 so break
                                    textwrite(self,"No DGN Value- Break Auto")
                                    try:
                                        ret = support.disconnect(libh)
                                    except:
                                        textwrite(self,"Handle NG - Conn issue")
                                else:        
                                    threading.Thread(target = timer,args=(self,t_end,)).start()
                                    
                                    while time.time() < t_end:
                                        # Timer Screen 
                                                now = datetime.now()
                                                if dgn!=0:   
                                                    ret0 = support.readdgn(libh,dgn,axis)
                                                    r=ret0["ret"]
                                                    if r !=0:
                                                        textwrite(self,f"1 NG data Er:{r} break auto")
                                                        try:
                                                            ret = support.disconnect(libh)
                                                        except:
                                                            textwrite(self,"Handle NG - Conn issue")
                                                        break
                                                else:
                                                    ret0={}
                                                    ret0["value"]="NIL"        
                                                if dg1!=0:
                                                    ret1 = support.readdgn(libh,dg1,axis1)
                                                    r1=ret1["ret"]
                                                    if r1 !=0:
                                                        textwrite(self,"2 NG data Er:{r1} break auto")
                                                        try:
                                                            ret = support.disconnect(libh)
                                                        except:
                                                            textwrite(self,"Handle NG - Conn issue")
                                                        break
                                                else:
                                                    ret1={}
                                                    ret1["value"]="NIL"        
                                                if dg2!=0:
                                                    ret2 = support.readdgn(libh,dg2,axis2)
                                                    r2=ret2["ret"]
                                                    if ret2["ret"] !=0:
                                                        textwrite(self,"3 NG data Er:{r2} break auto")
                                                        try:
                                                            ret = support.disconnect(libh)
                                                        except:
                                                            textwrite(self,"Handle NG - Conn issue")
                                                        break
                                                else:
                                                    ret2={}
                                                    ret2["value"]="NIL"                

                                                data = [now.strftime("%x"),now.strftime("%X"),dgn,axis,ret0["value"],dg1,axis1,ret1["value"],dg2,axis2,ret2["value"]]
                                                dt =[dgn,ret0["value"],dg1,ret1["value"],dg2,ret2["value"]]
                                                with open(filesave,'a',newline='') as csvfile:
                                                    csvwriter = csv.writer(csvfile)
                                                    csvwriter.writerow(data)
                                                    onscreenvalue(self,dt)
                                                    csvfile.close()
                                                time.sleep(ti)
                                                if stop_event.is_set():
                                                    print("i am out of while")
                                                    textwrite(self,"Cycle Stopped Check CSV File ")
                                                    try:
                                                        ret = support.disconnect(libh)
                                                    except:
                                                        textwrite(self,"Handle NG - Conn issue")
                                                    break
                                print("i am out of while - Finnaly")
                                hour.set("00")
                                minute.set("00")
                                second.set("00")
                                try:
                                    ret = support.disconnect(libh)
                                except:
                                    textwrite(self,"Handle NG - Conn issue")
            

        def stop(self,*args , **kwargs): # to Stop cycle
                stop_event.set()
                

        def manual(self,*args , **kwargs): # Manual Data in
            if checkauto(self) == False:
                    handlecheck(self)
                    savefilechek(self)
                    dgn =int(dgn1.get())
                    dg1 =int(dgn2.get())
                    dg2 =int(dgn3.get())
                    axis = int(axisinput.get())
                    axis1 = int(axisinput1.get())
                    axis2 = int(axisinput2.get())
                    now = datetime.now()
                    if dgn!=0:   
                        ret = support.readdgn(libh,dgn,axis)
                        r=ret["ret"]
                        if r !=0:
                            textwrite(self,f"1 NG data Er:{r}")
                            ret["value"] = f"ERR:{r}"
                    else:
                        ret={}
                        ret["value"]="NIL"        
                    if dg1!=0:
                        ret1 = support.readdgn(libh,dg1,axis1)
                        r1=ret1["ret"]
                        if r1 !=0:
                            textwrite(self,"2 NG data Er:{r1}")
                            ret1["value"] = f"ERR:{r1}"
                    else:
                        ret1={}
                        ret1["value"]="NIL"        
                    if dg2!=0:
                        ret2 = support.readdgn(libh,dg2,axis2)
                        r2=ret2["ret"]
                        if ret2["ret"] !=0:
                            textwrite(self,"3 NG data Er:{r2}")
                            ret2["value"] = f"ERR:{r2}"
                    else:
                        ret2={}
                        ret2["value"]="NIL"                

                    data = [now.strftime("%x"),now.strftime("%X"),dgn,axis,ret["value"],dg1,axis1,ret1["value"],dg2,axis2,ret2["value"]]
                    dt =[dgn,ret["value"],dg1,ret1["value"],dg2,ret2["value"]]
                    with open(filesave,'a',newline='') as csvfile:
                        csvwriter = csv.writer(csvfile)
                        csvwriter.writerow(data)
                        onscreenvalue(self,dt)
                        csvfile.close()       

        def csvopen(self,*args , **kwargs): # to select csv file
            if checkauto(self) == False: 
                filename= filedialog.askopenfilename(initialdir="c:",title="Select CSV fiel",filetypes=(("csv file","*.csv"),))    
                global filesave
                filesave = filename
                info = (f"file stored at : {filename}")
                textwrite(self,info)
                fields = ['Date','Time','DGN1','Axis1','value1','DGN2','Axis2','value2','DGN3','Axis3','value3'] 
                
                with open(filesave, 'w',newline='') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(fields)
                    csvfile.close()
        def connect(self,*args , **kwargs):  # Connect to CNC via GUI button
            if checkauto(self) == False: 
                ip= ipadd.get()       
                port= portnum.get()
                ret = support.connect(ip,port) 
                info=(f"connecting to {ip} wait")
                textwrite(self,info)
                if ret["ret"] == 0:
                    print ("connected OK")
                    info = (f"connected to {ip}")
                    textwrite(self,info)
                else:
                    print ("not connected")
                    info = ("Not Ok Correct Your Conn. Or  Switch On/off CNC")
                    textwrite(self,info)
                global libh # make this value as golbal
                libh = ret["libh"]                             

  
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Info Page", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        text= ScrolledText(self, width=80, height= 20)
        text.grid(row=1, column=0, rowspan= 8 ,columnspan=8, padx= 20)
        text.insert(tk.INSERT,
        """
Note :IP
o	If Communication not established even if ping is healthy try to restart CNC & Your PC then Try once again. 
o	CNC & PC IP address should be different ex. 198.168.1.1 CNC then PC 192.168.1.0. 

Note :R red & Write
o	if you use M code/PMC based DGN data capture  never use Read &  Write value same. 
o	Dont use enterd R Addres for other fuctions as in auto mode if Read address is 1 then only it will capture data. & In punch value write pmc to Bit (00000001).
o	In FOCAS we cant write/punch system internal R bits that start after R9000. 


For Auto By R Mode -
Need to Change CNC PMC
R read & r Write  not to be used for other Fuction

	It will run for T time when ever R Read is ON (00000001 bn, 1 d) then it will write data in CSV file and gives feedback to CNC via R Punch address  to ON(00000001 bn,  1 d). On CNC need to reset R punch address to 0 after M code/ PMC signal feedback signal received.
	Things to be entered
•	IP & Port 
•	DGN value need to monitor (DGN & Axis)
•	R Read & Punch Value 
•	Time to Run (In Min)

For Auto by Time Interval(Time)
	It will run for T time and it will take data at interval of T Interval time entered in application (In sec) and store DGN data in CSV file that is selected.
	Things to be entered
•	IP & Port 
•	DGN value need to monitor (DGN & Axis)
•	Time to Run (In Min)
•	Time Interval (In sec)
o	For auto by interval no need change at CNC. It will take data at time interval as per T interval (in sec)

for CSV File note
o	You can only select CSV file, you need to create one first.
o	If selected file having some data that will be erased then its will start capturing data
o	At Every Selection of csv file already stored data will be erased. Do not open file during Auto or manual entry.


In DGN	In Axis 	    CNC of with axis		Data condition
______________________________________________________________________
319 ( Axis  example) #   1 = X2 = Y3 = Z	# 	Output as value in cnc
411 ( SP Example)	 #   1 = S1 2 = S2	 	#	Output as value in cnc
45 (without Axis)    #   0 or -1	 	    #  	Output as value in cnc
1007 without Axis/SP)#	0 or -1	 	        #   Output as Decimal
1774                 # 	1,2,3 = x,y,z       #   Output as Decimal
1775                 #   1,2=s1 s           #   Output as Decimal
 
Note 
: "-"Negative DGN Value , "0.000" long char DGN Value, Hexa DGN Value will Be not Ok Value
: Desimal Vaule, Bit value (As Decimal) will be GOOD Condition.

Notes:
•   Tested for 0i TF MF
•	you can only use 4 Max Axis value can be used or can be return
•	Multipath System Not tested
•	For Any Bugs or improvement please give feedback. 
        """)
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="DGN Moni",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 0, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 0, column = 2, padx = 10, pady = 10)
  
  
# Driver Code
app = tkinterApp()
app.mainloop()