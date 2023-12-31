import random
import time
import numpy as np
from matplotlib import pyplot as plt
import os
import random
import numpy as np
from fractions import Fraction
from PIL import Image
from list_reg_print import *
## call ch341dll_wrap
from ch341dll_32bits_wrap.ch341dll_wrap  import *
from pmic_op import *
from PMIC51208b_CHIPTEST import *


#def i2c_read(self, i2c_addr7b, reg_addr, read_num=1, pec=0):
#def i2c_write(self, i2c_addr7b, addr, ldata, pec=0):
class FACE_FPGA_REGS_BUS_HD():
    def __init__(self, REGRW_HD):
        self.REGRW_HD = REGRW_HD
        self.i2c_addr = 0x1b;

    #def spi_wr(addr, wdata):
    def write(self, addr, wdata):
        #print("call FPGA_BUS_HD write")
#        lwdata = [];
#        lwdata.append(wdata)
        wret = self.REGRW_HD.i2c_write(self.i2c_addr,addr,[wdata])
        if (wret > 1):
            return 1;
        else:
            if (wret > 0):
                return 1;
            else:
                return 0;

    #def spi_rr(addr, wdata=0):
    def read(self, addr, wdata=0):
        #rdata = self.REGRW_HD.ch341_spi4w_stream([addr, 0x00, (wdata >> 8) & 0xff, wdata & 0xff])
        rdata = self.REGRW_HD.i2c_read(self.i2c_addr,addr,1)
#        out = (rdata[0] & 0xff) << 8;
#        out += (rdata[3] & 0xff);
        out = rdata[0];
        return out;

    #def read(self, addr):
    #    return 0x1f;

    #def write(self, addr, wdata):
    #    return 0x1;


#if __name__ == '__main__':
slv_addr = 0x40;
i2c_hd = pmic_i2c_options(0); ##USB2I2C hardware initial
i2c_hd.ch341_i2c_speed(3) ; ## i2c speed setting , 1: 100k 2: 400k, 3:750Khz; 0:20k
REGRW_HD = FACE_FPGA_REGS_BUS_HD(i2c_hd)
REGRW_HD.i2c_addr = 0x4f;
CHIP_REG = PMIC5120(REGRW_HD)
xx = CHIP_REG.R04.reads()
xx = CHIP_REG.R05.reads()
xx = CHIP_REG.R06.reads()
xx = CHIP_REG.R08.reads()
xx = CHIP_REG.R09.reads()
xx = CHIP_REG.R0A.reads()
xx = CHIP_REG.R0B.reads()
xx = CHIP_REG.R0C.reads()
xx = CHIP_REG.R32.reads()
#xx = CHIP_REG.R32.reads()
xx = CHIP_REG.R2F.write(0x4)
xx = CHIP_REG.R2F.reads()
xx = CHIP_REG.R32.write(0x0)
xx = CHIP_REG.R32.write(0x0)
time.sleep(1)
bf_vr = i2c_hd.i2c_read(0x4f,0x0,64)
xx = CHIP_REG.R32.write(0x80)
time.sleep(2)
aft_vr = i2c_hd.i2c_read(0x4f,0x0,64)
#xx = CHIP_REG.R32.write(0x00)
#yy = i2c_hd.i2c_read(0x4f,0x0,255)
print(CHIP_REG.dic_name.keys())
list_reg_print(bf_vr,0,aft_vr)
list_reg_print(aft_vr,0,bf_vr)
#for ii in range(0x7f):
#    REGRW_HD.i2c_addr = ii;
#    xx = CHIP_REG.R04.read()

##try read R41
CHIP_REG.R37.write(0x73)
CHIP_REG.R38.write(0x94)
CHIP_REG.R39.write(0x40)
xx = CHIP_REG.R41.reads()
