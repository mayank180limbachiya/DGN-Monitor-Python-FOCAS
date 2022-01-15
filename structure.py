import ctypes

# DGN Read Struct as per define in FOCAS
MAX_AXIS = 4
class _U(ctypes.Union):
    _pack_ = 1 
    _fields_ =[("cdata", ctypes.c_char),
                ("idata", ctypes.c_short),
                ("ldata", ctypes.c_long),
                ("rdata", ctypes.c_long),
                ("cdatas_A", ctypes.c_char * MAX_AXIS),
                ("idatas_A", ctypes.c_short * MAX_AXIS),
                ("ldatas_A", ctypes.c_long * MAX_AXIS),
                ("rdatas_A", ctypes.c_long * MAX_AXIS),]

class Dgn2Info(ctypes.Structure):
    _pack_ = 4
    _anonymous_ = ("u",)
    _fields_ = [("datano",ctypes.c_short),
                ("type",ctypes.c_short),
                ("u",_U),]  
ODBDGN = Dgn2Info


# PMC Read & Write Structure as per define in FOCAS 
class PMCData(ctypes.Union):
    """
    Actual PMC values that were read
    Used to replace anonymous struct in IODBPMC called "u"
    """
    _pack_ = 1
    _fields_ = [("cdata", ctypes.c_short * 5), ]
    
class PMC(ctypes.Structure):
    """
    A data structure to hold values read from PMC addresses
    Equivalent of IODBPMC
    """
    _anonymous_ = ("data",)
    _pack_ = 4
    _fields_ = [("addressType", ctypes.c_short),
                ("dataType", ctypes.c_short),
                ("startAddress", ctypes.c_short),
                ("endAddress", ctypes.c_short),
                ("data", PMCData), ]
IODBPMC = PMC