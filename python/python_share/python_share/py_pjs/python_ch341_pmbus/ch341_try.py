import random
import time
import numpy as np
from matplotlib import pyplot as plt
import os
import random
import numpy as np
from fractions import Fraction
from PIL import Image

## call ch341dll_wrap
from ch341dll_32bits_wrap.ch341dll_wrap  import *

###1.  init ch341 device
hd = CH341DEV(0)
hd.ch341_i2c_speed(2)
#hd.ch341_close()

def fl2hex (data):
    return 0xffff & int(data * 2**12)

def c2p_to_dec(data,bits=5):
    signb = data & (1<<(bits-1)) ;
    all_one = 2**bits -1 ;
    all_dat_with_out_signed = 2**(bits-1) -1;
    if ( signb == 0 ):
        out = data & all_dat_with_out_signed;
    else:
        out = -1 * ((data ^ all_one) + 1 );
    return out

def linear_dat_to_dec (data):
    exp_v_s = ((0x1f << 11) & data ) >> 11;
    exp_v_dec = c2p_to_dec(exp_v_s,5)

    body11b = 0x7ff & data;
    out = body11b * 2**(exp_v_dec) ;
    return out
###2.  init oled ----
#device_addr = round(0x78>>1)
#hd.ch341_swi2c(device_addr,0x00, 0x00); #// SSD1306_DISPLAYOFF
#rd1B = hd.ch341_sri2c(device_addr,0x81);
#for ii in range(256):
#    hd.ch341_stream_mri2c(device_addr,[ii,0x2,0x3,0x4,0x5,0x1f])
#xx = hd.ch341_stream_mri2c(device_addr,6)
#hd.pm_send_byte(device_addr,0,1)
#hd.pm_send_byte(device_addr,1,1)
#hd.pm_write_byte(device_addr,0x81,0x1,0x1)
#hd.pm_write_word(device_addr,0x11,0x1245,1)
#hd.pm_write_block(device_addr,0x11,[0x12,0x3,0x4,0x5],1)
#hd.pm_write_block(device_addr,0x1,[0x88],1)
#xx = hd.pm_read_byte(device_addr,0)
#yy = hd.pm_read_byte(device_addr,0,1)
#hd.pm_write_infine_reg(device_addr,0x1234,0x5678)
#h#d.pm_read_infine_reg(device_addr,0x1234,0x0)

device_addr = 0x12;
for ii in range(256):
    device_addr = ii;
    xx = hd.ch341_sri2c(ii,0x1)
    if (xx < 0xff):
        print("@ii",hex(ii),hex(xx))

@ii 0x10 0x0
@ii 0x40 0x0
@ii 0x90 0x0
@ii 0xc0 0x0
## OPTION
device_addr = 0x40;


for ii in range(256):
    device_addr = ii;
    cmd = 0x1;
    #xx = hd.pm_read_byte(device_addr,cmd,1)
    xx = hd.ch341_sri2c(ii,0x1)
    if (xx < 0xff):
        print(ii,"input cmd",hex(cmd),"get_date",hex(xx))

exit()
## OPTION
cmd = 0x2;
xx = hd.pm_read_byte(device_addr,cmd,1)
print("input cmd",hex(cmd),"get_date",hex(xx[0]))
## OPTION
cmd = 0x2;
xx = hd.pm_write_byte(device_addr,cmd,0x1d,1)
xx = hd.pm_write_byte(device_addr,cmd,0x0d,1)


xx = hd.pm_write_byte(device_addr,0x3,0x0)

##write protect
cmd = 0x10;
xx = hd.pm_read_byte(device_addr,cmd,1)
print("input cmd",hex(cmd),"get_date",hex(xx[0]))

## Vout_mode
cmd = 0x20;
xx = hd.pm_read_byte(device_addr,cmd,1)
print("input cmd",hex(cmd),"get_date",hex(xx[0]))
exp_v = c2p_to_dec(xx[0])

## VOUT_COMMAND:
cmd = 0x21;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("set Vout = ",(xx[1]*256+xx[0])* 2**(exp_v),"V")

xx = hd.pm_write_word(device_addr,cmd,0xc060,1)


## Freq SWitch:
cmd = 0x33;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("freq:",linear_dat_to_dec((xx[1]*256+xx[0])), "Khz")

## Vin on:
cmd = 0x35;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("get Vin on=",linear_dat_to_dec((xx[1]*256+xx[0])), "v")

## Vin off:
cmd = 0x36;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("get Vin on=",linear_dat_to_dec((xx[1]*256+xx[0])), "v")


## VOUT OV FAULT LIMIT :
cmd = 0x40;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("set Vout OV FAULT = ",(xx[1]*256+xx[0])* 2**(exp_v),"V")

## VOUT OV FAULT RESPONSE:
cmd = 0x41;
xx = hd.pm_read_byte(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]) )
#print("set Vout OV FAULT = ",(xx[1]*256+xx[0])* 2**(exp_v),"V")

## VOUT OV WARNING :
cmd = 0x42;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("set Vout OV FAULT = ",(xx[1]*256+xx[0])* 2**(exp_v),"V")

## IOUT OC Limit:
cmd = 0x46;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("set Iout OC LIMIT = ",linear_dat_to_dec(xx[1]*256+xx[0]) ,"A")

## IOUT OC resp:
cmd = 0x47;
xx = hd.pm_read_byte(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]));#,hex(xx[1]) )

## IOUT OC Warning:
cmd = 0x4A;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("set Iout OC Warning = ",linear_dat_to_dec(xx[1]*256+xx[0]) ,"A")

## temp OT limit:
cmd = 0x4F;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("get OT = ",linear_dat_to_dec(xx[1]*256+xx[0]) ,"。C")

## temp OT limit:
cmd = 0x50;
xx = hd.pm_read_byte(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]));#,hex(xx[1]) )

## temp OT Warning:
cmd = 0x51;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("get OT = ",linear_dat_to_dec(xx[1]*256+xx[0]) ,"。C")

## Vin OV fault :
cmd = 0x55;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("get Vin OV limit  = ",linear_dat_to_dec(xx[1]*256+xx[0]) ,"V")

## power good on
cmd = 0x5e;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("set good on  Vout = ",(xx[1]*256+xx[0])* 2**(exp_v),"V")

## power good off
cmd = 0x5f;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("set good off  Vout = ",(xx[1]*256+xx[0])* 2**(exp_v),"V")

## ton on delay
cmd = 0x60;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("get Ton delay = ",linear_dat_to_dec(xx[1]*256+xx[0]) ,"ms")

## ton on rise
cmd = 0x61;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("get Ton rise = ",linear_dat_to_dec(xx[1]*256+xx[0]) ,"ms")

## ton on rise
cmd = 0x79;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )

## Vin
cmd = 0x88;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("get Vin = ",linear_dat_to_dec(xx[1]*256+xx[0]) ,"V")

## Vout
cmd = 0x8B;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("get Vout = ",(xx[1]*256+xx[0])* 2**(exp_v),"V")

xx = hd.pm_write_byte(device_addr,0x2,0xd)

xx = hd.pm_read_byte(device_addr,0x2,0xd)
## Vin
cmd = 0x8D;
xx = hd.pm_read_byte2(device_addr,cmd)
print("input cmd",hex(cmd),"get_date",hex(xx[0]),hex(xx[1]) )
print("get TEmp = ",linear_dat_to_dec(xx[1]*256+xx[0]) ,"C")

xx = hd.pm_write_word(device_addr,cmd,0xc020)

def exp2dec(inword):
    inword = 0x3f14
    l11b = inword & 0x7ff;
    h6b  = ((0x1f << 11) & inword ) >> 11;
