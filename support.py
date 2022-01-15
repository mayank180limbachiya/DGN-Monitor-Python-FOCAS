import ctypes
from ctypes import *
from pathlib import Path
import structure
import os

#libpath = ("C:/Users/mayank.limbachiya/desktop/focas/Fwlib64.dll")
#libpath1 = (Path.cwd().parents[1] / "/desktop/DGN/Fwlib64.dll")
#print(libpath1)
#path = os.getcwd()
print(os.getcwd()+"\lib\Fwlib64.dll")
focas = ctypes.cdll.LoadLibrary(os.getcwd()+"\lib\Fwlib64.dll")

# Connect Fuction to connect with CNC taking Handle
def connect(ip,port):
    timeout = 10
    libh = ctypes.c_ushort(0)
    if port == "":
        port = 8193
    focas.cnc_allclibhndl3.restype = ctypes.c_short
    focas.cnc_freelibhndl.restype = ctypes.c_short
    ret = focas.cnc_allclibhndl3(ip.encode(),int(port),timeout,ctypes.byref(libh))
    info = dict()
    info['libh'] = libh
    info["ret"] = ret
    print (info)
    return info

# DisConnect Fuction to free cnc from handle
def disconnect(libh):
    print(libh)
    ret = focas.cnc_freelibhndl(libh)
    info = dict()
    info["ret"] = ret
    print(info)
    return info

# Read DGN via DGN & Axis Value
def readdgn(libh,DGN,axis):
    lenth = 9
    dgndata = structure.Dgn2Info()
    ret = focas.cnc_diagnoss(libh , DGN, axis, lenth, byref(dgndata))
    info = dict()
    info["value"] = dgndata.u.idata
    info["ret"] = ret
    return info

# Read PMC with handle & R Read value
def readpmc(libh,rin):
    datatype = 5 #for R bit its 5 in focas  
    datakind = 0 #for byte or word 0 in focas  
    lenth = 9 # via calculating for 1 addrase read its 8+N = 9
    pmc = structure.PMC()
    ret = focas.pmc_rdpmcrng(libh,datatype,datakind,rin,rin,lenth,byref(pmc) )
    info = dict()
    info["value"] = pmc.data.cdata[0]
    info["ret"] = ret
    return info

# Write PMC with Handle & r write = 1 in R 
def writepmc(libh, rout):    
    pmcwrite = structure.PMC()
    pmcwrite.addressType = 5 # Data 5 = r bit
    pmcwrite.typedataType = 0 # datakind byte , word etc
    pmcwrite.data.cdata[0] = 1 # write bit # 0 fyi you can't use that complte R
    ln=9 # lenth of byte by FOCAS manual
    pmcwrite.startAddress = rout
    pmcwrite.endAddress = rout
    ret = focas.pmc_wrpmcrng(libh,ln,byref(pmcwrite))
    info = dict()
    info["ret"] = ret
    return info
   
    

    











                



