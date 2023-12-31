# coding=gbk 
#################################################################################
# chip test python file generated by Jmanager 
# use it in python , to configure chip regs in form like  
#usage: 
#    CHIPREG.U_RAG0x1.set_cur.set(0x1); 
#    CHIPREG.U_RAG0x1.write(0x1); 
#################################################################################


##########################main code ##################################################
#    CHIPREG.U_RAG0x1.set_cur.set(0x1); 
#    CHIPREG.U_RAG0x1.write(0x1); 
from output.base_pyt_reg_definition import *
#from base_pyt_reg_definition import *

class REG0 (pyt_reg):
    def __init__(self, name="REG0", bus_hd=None, bits_w=8, addr=0, desc="""for reset control""" ):
        super(REG0,self).__init__(name,bus_hd,bits_w,addr,desc)
        self.field5a       = pyt_reg_field("field5a",       2, 6, 0x0, "RW","""描述寄存器内容5；
1. 开启， 0： 关闭""")
        self.reserved      = pyt_reg_field("reserved",      1, 5, 0x0, "-","""保留""")
        self.reg444ba      = pyt_reg_field("reg444ba",      1, 4, 0x1, "RO","""取得xx状态， 1： abb； 0：bbb""")
        self.reg3to2a      = pyt_reg_field("reg3to2a",      3, 1, 0x4, "RW","""reg3to2的对于数据*3+1""")
        self.reg00a        = pyt_reg_field("reg00a",        1, 0, 0x0, "RW","""00reg3to2对于数据*3+1""")
        self.fl = [     self.field5a,     self.reserved,     self.reg444ba,     self.reg3to2a,     self.reg00a]

class REG2 (pyt_reg):
    def __init__(self, name="REG2", bus_hd=None, bits_w=8, addr=1, desc="""用于xx控制1""" ):
        super(REG2,self).__init__(name,bus_hd,bits_w,addr,desc)
        self.field5b       = pyt_reg_field("field5b",       2, 6, 0x0, "RW","""描述寄存器内容5；
1. 开启， 0： 关闭""")
        self.reserved      = pyt_reg_field("reserved",      1, 5, 0x0, "-","""保留""")
        self.reg444b       = pyt_reg_field("reg444b",       2, 3, 0x0, "RO","""取得xx状态， 1： abb； 0：bbb""")
        self.reg3to2b      = pyt_reg_field("reg3to2b",      2, 1, 0x3, "RW","""reg3to2的对于数据*3+1""")
        self.reg00ab       = pyt_reg_field("reg00ab",       1, 0, 0x0, "RW","""00reg3to2的对于数据*3+1""")
        self.fl = [     self.field5b,     self.reserved,     self.reg444b,     self.reg3to2b,     self.reg00ab]

class REG3 (pyt_reg):
    def __init__(self, name="REG3", bus_hd=None, bits_w=8, addr=3, desc="""用于xx控制1""" ):
        super(REG3,self).__init__(name,bus_hd,bits_w,addr,desc)
        self.field5c       = pyt_reg_field("field5c",       2, 6, 0x0, "W1C","""描述寄存器内容5；
1. 开启， 0： 关闭""")
        self.reserved      = pyt_reg_field("reserved",      2, 4, 0x0, "-","""保留""")
        self.reg444c       = pyt_reg_field("reg444c",       1, 3, 0x0, "W1C","""取得xx状态， 1： abb； 0：bbb""")
        self.reserved      = pyt_reg_field("reserved",      2, 1, 0x0, "-","""reg3to2的对于数据*3+1""")
        self.reg00c        = pyt_reg_field("reg00c",        1, 0, 0x0, "W1C","""00reg3to2的对于数据*3+1""")
        self.fl = [     self.field5c,     self.reserved,     self.reg444c,     self.reserved,     self.reg00c]

class REG1C (pyt_reg):
    def __init__(self, name="REG1C", bus_hd=None, bits_w=8, addr=28, desc="""用于xx控制122""" ):
        super(REG1C,self).__init__(name,bus_hd,bits_w,addr,desc)
        self.field5c12     = pyt_reg_field("field5c12",     2, 6, 0x0, "RO","""描述寄存器内容5；
1. 开启， 0： 关闭""")
        self.reg00c12      = pyt_reg_field("reg00c12",      6, 0, 0x0, "RW","""00reg3to2的对于数据*3+1""")
        self.fl = [     self.field5c12,     self.reg00c12]

class REG1D (pyt_reg):
    def __init__(self, name="REG1D", bus_hd=None, bits_w=8, addr=29, desc="""reg9edec""" ):
        super(REG1D,self).__init__(name,bus_hd,bits_w,addr,desc)
        self.xx_name       = pyt_reg_field("xx_name",       8, 0, 0x9e, "RW","""描述寄存器内容5；
1. 开启， 0： 关闭""")
        self.fl = [     self.xx_name]

class REG1F (pyt_reg):
    def __init__(self, name="REG1F", bus_hd=None, bits_w=8, addr=31, desc="""reg9edec""" ):
        super(REG1F,self).__init__(name,bus_hd,bits_w,addr,desc)
        self.reg9e_name2   = pyt_reg_field("reg9e_name2",   8, 0, 0x9e, "RW","""描述寄存器内容5；
1. 开启， 0： 关闭""")
        self.fl = [     self.reg9e_name2]

class REG21_W1C (pyt_reg):
    def __init__(self, name="REG21_W1C", bus_hd=None, bits_w=8, addr=33, desc="""TRY W1C""" ):
        super(REG21_W1C,self).__init__(name,bus_hd,bits_w,addr,desc)
        self.reg21w1c      = pyt_reg_field("reg21w1c",      8, 0, 0x0, "W1C","""描述寄存器内容5；
1. 开启， 0： 关闭""")
        self.fl = [     self.reg21w1c]

class STATUS_BYTE (pyt_reg):
    def __init__(self, name="STATUS_BYTE", bus_hd=None, bits_w=8, addr=51, desc="""PMBUS STATUS BYTE""" ):
        super(STATUS_BYTE,self).__init__(name,bus_hd,bits_w,addr,desc)
        self.busy          = pyt_reg_field("busy",          1, 7, 0x0, "W1C","""描述寄存器内容5；
1. 开启， 0： 关闭""")
        self.off           = pyt_reg_field("off",           1, 6, 0x0, "RO","""off state""")
        self.vout_ov_fault  = pyt_reg_field("vout_ov_fault", 1, 5, 0x0, "RO","""vout ov fault""")
        self.iout_oc_fault  = pyt_reg_field("iout_oc_fault", 1, 4, 0x0, "RO","""iout_oc  fault""")
        self.vin_uv_fault  = pyt_reg_field("vin_uv_fault",  1, 3, 0x3, "RO","""vin uv""")
        self.tempereature  = pyt_reg_field("tempereature",  1, 2, 0x0, "RO","""temp over""")
        self.cml           = pyt_reg_field("cml",           1, 1, 0x0, "RO","""cml error""")
        self.none_of_the_above  = pyt_reg_field("none_of_the_above", 1, 0, 0x0, "RO","""not above""")
        self.fl = [     self.busy,     self.off,     self.vout_ov_fault,     self.iout_oc_fault,     self.vin_uv_fault,     self.tempereature,     self.cml,     self.none_of_the_above]

class FAULT7B (pyt_reg):
    def __init__(self, name="FAULT7B", bus_hd=None, bits_w=8, addr=52, desc="""FAULT7BITS""" ):
        super(FAULT7B,self).__init__(name,bus_hd,bits_w,addr,desc)
        self.ocp7_f        = pyt_reg_field("ocp7_f",        1, 7, 0x0, "W1C","""描述寄存器内容5；
1. 开启， 0： 关闭""")
        self.opt6_f        = pyt_reg_field("opt6_f",        1, 6, 0x0, "W1C","""off state""")
        self.ocv5          = pyt_reg_field("ocv5",          1, 5, 0x0, "W1C","""vout ov fault""")
        self.uvp4          = pyt_reg_field("uvp4",          1, 4, 0x0, "W1C","""iout_oc  fault""")
        self.uvpw3         = pyt_reg_field("uvpw3",         1, 3, 0x0, "W1C","""vin uv""")
        self.uvpf2         = pyt_reg_field("uvpf2",         1, 2, 0x0, "W1C","""temp over""")
        self.abcf1         = pyt_reg_field("abcf1",         1, 1, 0x0, "W1C","""cml error""")
        self.beef0         = pyt_reg_field("beef0",         1, 0, 0x0, "W1C","""not above""")
        self.fl = [     self.ocp7_f,     self.opt6_f,     self.ocv5,     self.uvp4,     self.uvpw3,     self.uvpf2,     self.abcf1,     self.beef0]

class FRC (pyt_reg):
    def __init__(self, name="FRC", bus_hd=None, bits_w=8, addr=54, desc="""FAULT7BITS""" ):
        super(FRC,self).__init__(name,bus_hd,bits_w,addr,desc)
        self.rc7           = pyt_reg_field("rc7",           1, 7, 0x0, "RC","""描述寄存器内容5；
1. 开启， 0： 关闭""")
        self.rc6           = pyt_reg_field("rc6",           1, 6, 0x0, "RC","""off state""")
        self.reserved      = pyt_reg_field("reserved",      1, 5, 0x0, "-","""vout ov fault""")
        self.rc5           = pyt_reg_field("rc5",           1, 4, 0x0, "RC","""iout_oc  fault""")
        self.rc4           = pyt_reg_field("rc4",           1, 3, 0x0, "RC","""vin uv""")
        self.rc3           = pyt_reg_field("rc3",           1, 2, 0x0, "RC","""temp over""")
        self.rc2           = pyt_reg_field("rc2",           1, 1, 0x0, "RC","""cml error""")
        self.rc1           = pyt_reg_field("rc1",           1, 0, 0x0, "RC","""not above""")
        self.fl = [     self.rc7,     self.rc6,     self.reserved,     self.rc5,     self.rc4,     self.rc3,     self.rc2,     self.rc1]

class FAULT33W0C (pyt_reg):
    def __init__(self, name="FAULT33W0C", bus_hd=None, bits_w=8, addr=55, desc="""FAULT7BITS""" ):
        super(FAULT33W0C,self).__init__(name,bus_hd,bits_w,addr,desc)
        self.w0cocp7_f     = pyt_reg_field("w0cocp7_f",     1, 7, 0x0, "W0C","""描述寄存器内容5；
1. 开启， 0： 关闭""")
        self.w0opt6_f      = pyt_reg_field("w0opt6_f",      1, 6, 0x0, "W0C","""off state""")
        self.w0ocv5        = pyt_reg_field("w0ocv5",        1, 5, 0x0, "W0C","""vout ov fault""")
        self.uvp4w0        = pyt_reg_field("uvp4w0",        1, 4, 0x0, "RO","""iout_oc  fault""")
        self.uvpw3wo       = pyt_reg_field("uvpw3wo",       1, 3, 0x0, "W0C","""vin uv""")
        self.uvpf2w0       = pyt_reg_field("uvpf2w0",       1, 2, 0x0, "RO","""temp over""")
        self.abcf1w0       = pyt_reg_field("abcf1w0",       1, 1, 0x0, "W0C","""cml error""")
        self.beef0w0       = pyt_reg_field("beef0w0",       1, 0, 0x0, "W0C","""not above""")
        self.fl = [     self.w0cocp7_f,     self.w0opt6_f,     self.w0ocv5,     self.uvp4w0,     self.uvpw3wo,     self.uvpf2w0,     self.abcf1w0,     self.beef0w0]


######################### pack up all reg to sheet Module ############
class S2_8B_MOD():
    def __init__(self, bus_hd):
        self.REG0             = REG0("U_REG0" , bus_hd)
        self.REG2             = REG2("U_REG2" , bus_hd)
        self.REG3             = REG3("U_REG3" , bus_hd)
        self.REG1C            = REG1C("U_REG1C" , bus_hd)
        self.REG1D            = REG1D("U_REG1D" , bus_hd)
        self.REG1F            = REG1F("U_REG1F" , bus_hd)
        self.REG21_W1C        = REG21_W1C("U_REG21_W1C" , bus_hd)
        self.STATUS_BYTE      = STATUS_BYTE("U_STATUS_BYTE" , bus_hd)
        self.FAULT7B          = FAULT7B("U_FAULT7B" , bus_hd)
        self.FRC              = FRC("U_FRC" , bus_hd)
        self.FAULT33W0C       = FAULT33W0C("U_FAULT33W0C" , bus_hd)
        self.rl = [self.REG0,self.REG2,self.REG3,self.REG1C,self.REG1D,self.REG1F,self.REG21_W1C,self.STATUS_BYTE,self.FAULT7B,self.FRC,self.FAULT33W0C]
        self.dic_name = {\
                             "REG0":self.REG0,\
                             "REG2":self.REG2,\
                             "REG3":self.REG3,\
                             "REG1C":self.REG1C,\
                             "REG1D":self.REG1D,\
                             "REG1F":self.REG1F,\
                             "REG21_W1C":self.REG21_W1C,\
                             "STATUS_BYTE":self.STATUS_BYTE,\
                             "FAULT7B":self.FAULT7B,\
                             "FRC":self.FRC,\
                             "FAULT33W0C":self.FAULT33W0C}
        self.dic_addr = { \
                           0x0:self.REG0,\
                           0x1:self.REG2,\
                           0x3:self.REG3,\
                           0x1c:self.REG1C,\
                           0x1d:self.REG1D,\
                           0x1f:self.REG1F,\
                           0x21:self.REG21_W1C,\
                           0x33:self.STATUS_BYTE,\
                           0x34:self.FAULT7B,\
                           0x36:self.FRC,\
                           0x37:self.FAULT33W0C}


######################### usage reg module example ############


class FACE_S2_8B_MOD_BUS_HD():
     def __init__(self,name="FAKE_BUS"):                
          self.name = name                           
     def read (self,addr):                        
         return 0x1f;                               
     def write (self,addr,wdata):                  
         return 0x1;                                



if __name__ == '__main__':     
    bus_hd = FACE_S2_8B_MOD_BUS_HD()
    CHIP_REG = S2_8B_MOD(bus_hd)      
    print(CHIP_REG.dic_name.keys()) 
    print(CHIP_REG.dic_addr.keys()) 
                 
