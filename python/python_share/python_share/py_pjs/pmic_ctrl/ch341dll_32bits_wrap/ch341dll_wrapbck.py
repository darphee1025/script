import ctypes

## only win32 version python can Load the CH341DLL.dll
class CH341DEV():
    def __init__(self, dev_index = 0):
        self.usb_id = dev_index
        self.open_status = 0;
        self.i2c_speed = 3;
        self.ch341_i2c_speed(self.i2c_speed);
        self.ch341dll = ctypes.windll.LoadLibrary(".//CH341DLL_31k.dll")
        print("Ch341dll_wrap is loaded!!! only work for python 32bits version !!!")
        self.ch341_open();

    def check_status (self):
        if (self.open_status == 0):
            print("Open USB CH341Dev Index=",self.usb_id," is not ready, pls try to open it firsit!!!!!!!")
            return -1;

        return 1;

    def ch341_open(self ):
        if ( self.ch341dll.CH341OpenDevice(self.usb_id) > 0):
            print("Open USB CH341Dev Index=",self.usb_id,"ok!!!!!!!")
            self.open_status = 1;
            return self.usb_id;
        else:
            print("Error!!! USB CH341 Open Failed!")
            self.open_status = 0;
            return -1

    def ch341_close(self):
        if (self.ch341dll.CH341CloseDevice(self.usb_id) > 0):
            print("Close USB CH341Dev Index=", self.usb_id, "ok!!!!!!!")
            self.open_status = 0;
            return 1;
        else:
            print("Error!!! USB CH341 Close Failed!")
            return -1

    def ch341_i2c_speed(self,speed=3):
        self.i2c_speed = speed;
        if(self.check_status() < 1):
            print ("set I2C speed to ", speed, "Fail ,please check your CH341 Device !!")
            return -1;
        if (self.ch341dll.CH341SetStream(self.usb_id,0x80+speed) > 0):
            print ("set I2C speed to ", speed, "(3=750Khz, 2=400k, 1=100k, 0=20k")
            return 1;
        else:
            self.open_status = 0;
            print ("set I2C speed to ", speed, "Fail ,please check your CH341 Device !!")
            return -1

    def ch341_swi2c (self,i2c_addr7b,reg_addr,wdata):
        if(self.check_status() < 1):
            return -1;
        return self.ch341dll.CH341WriteI2C(self.usb_id, i2c_addr7b & 0xff, reg_addr&0xff, wdata&0xff)

    def ch341_sri2c (self,i2c_addr7b,reg_addr):
        if(self.check_status() < 1):
            return -1;
        rdata = (ctypes.c_uint8 * 1)()
        if( self.ch341dll.CH341ReadI2C(self.usb_id, i2c_addr7b & 0xff, reg_addr&0xff,rdata ) > 0):
            return rdata[0]&0xff
        else:
            return -1;

    def ch341_stream_op (self,i2c_addr7b,wdat,Rd_num):
        '''i2c rw stream '''
        if(self.check_status() < 1):
            return -1;
        inlen = Rd_num;
        if inlen > 4000:
            print("should not greater than 4000");
            return -1;
        inlen += 1;
        wdata = (ctypes.c_uint8 * (inlen))()
        rdata = (ctypes.c_uint8 * (inlen))()
        wlen  = len(wdat) - 1;
        wdata[0] = (i2c_addr7b & 0xff) << 1 ;
        for ii in range(wlen)
            wdata[1+ii] = wdat[ii] & 0xff;
        if( self.ch341dll.CH341StreamI2C (self.usb_id, wlen + 1, wdata ,inlen, rdata ) > 0):
            rdout = [];
            for ii in range(inlen):
                rdout.append(int(rdata[ii]));
            return rdout;
        else:
            return -1;

    def ch341_stream_mri2c (self,i2c_addr7b,Rd_num=1):
        '''i2c rw stream '''
        if(self.check_status() < 1):
            return -1;
        inlen = Rd_num;
        if inlen > 4000:
            print("should not greater than 4000");
            return -1;
        inlen += 1;
        wdata = (ctypes.c_uint8 * (inlen))()
        rdata = (ctypes.c_uint8 * (inlen))()
        wdata[0] = (i2c_addr7b & 0xff) << 1 ;
        wdata[0] = wdata[0] + 1;
        for ii in range(1,inlen):
            wdata[ii] = 0xff;
        #print("debug: wlen=",inlen)
        #print("debug: wdata=",wdata[100:])
        if( self.ch341dll.CH341StreamI2C (self.usb_id, inlen, wdata ,inlen, rdata ) > 0):
            rdout = [];
            for ii in range(inlen):
                rdout.append(int(rdata[ii]));
            return rdout;
        else:
            return -1;


    def ch341_stream_wi2c (self,i2c_addr7b,din):
        '''i2c rw stream '''
        if(self.check_status() < 1):
            return -1;
        inlen = len(din);
        if inlen > 4000:
            print("should not greater than 4000");
            return -1;
        inlen += 1;
        wdata = (ctypes.c_uint8 * (inlen))()
        rdata = (ctypes.c_uint8 * (inlen))()
        wdata[0] = (i2c_addr7b & 0xff) << 1;
        for ii in range(1,inlen):
            wdata[ii] = din[ii-1] & 0xff;
        #print("debug: wlen=",inlen)
        #print("debug: wdata=",wdata[100:])
        if( self.ch341dll.CH341StreamI2C (self.usb_id, inlen, wdata ,0, rdata ) > 0):
            return 1;
        else:
            self.open_status = 0;
            return -1;
    ##### -- pm bus options
    def pm_calc_pec (self, to_calc):
        crc8 = 0;
        for ii in to_calc:
            #print("---------", hex(ii), "-----------------")
            for jj in range(8):
                #print("bit", 7 - jj, int((ii & (0x1 << (7 - jj))) > 0))
                bitv = int((ii & (0x1 << (7 - jj))) > 0);
                crcb7 = int((crc8 & 0x80) > 0);
                to_add = bitv ^ crcb7;
                crc8_x2 = 0xff & (crc8 << 1);
                comb_v = crc8_x2 ^ (7 * to_add);
                crc8 = comb_v & 0xff
        return crc8;

    def pm_send_byte(self,i2c_addr7b,cmd,pec=0):
        inlen = 2;
        if(pec > 0):
            inlen = inlen + 1;
        wdata = (ctypes.c_uint8 * (inlen))()
        rdata = (ctypes.c_uint8 * (inlen))()
        wdata[0] = (i2c_addr7b & 0xff) << 1;
        wdata[1] = (cmd & 0xff) ;
        ## todo calc pec
        pec_code = self.pm_calc_pec([wdata[0],wdata[1]])
        if(pec > 0):
            wdata[2] = (pec_code & 0xff) ; ##
        if( self.ch341dll.CH341StreamI2C (self.usb_id, inlen, wdata ,0, rdata ) > 0):
            return 1;
        else:
            self.open_status = 0;
            return -1;

    def pm_read_word (self,i2c_addr7b,cmd,pec=0):
        inlen = 2;
        if(pec > 0):
            inlen = inlen + 1;
        wdata = (ctypes.c_uint8 * (inlen))()
        rdata = (ctypes.c_uint8 * (inlen))()
        wdata[0] = (i2c_addr7b & 0xff) << 1;
        wdata[1] = (cmd & 0xff) ;
        if( self.ch341dll.CH341StreamI2C (self.usb_id, 2, wdata ,inlen-1, rdata ) > 0):
            ## check --- calc pec
            rdat_out = [];
            pec_code = 0x1f
            #            if (pec_code > 0):
            #                pm_calc_pec(rdata) ==
            for ii in range(inlen-1):
                rdat_out.append(int(rdata[ii]))
            return rdat_out;
        else:
            self.open_status = 0;
            return -1;

    def pm_read_byte(self,i2c_addr7b,cmd,pec=0):
        inlen = 2;
        if(pec > 0):
            inlen = inlen + 1;
        wdata = (ctypes.c_uint8 * (inlen))()
        rdata = (ctypes.c_uint8 * (inlen))()
        wdata[0] = (i2c_addr7b & 0xff) << 1;
        wdata[1] = (cmd & 0xff) ;
        if( self.ch341dll.CH341StreamI2C (self.usb_id, 2, wdata ,inlen-1, rdata ) > 0):
            ## check --- calc pec
            rdat_out = [];
            pec_code = 0x1f
            #            if (pec_code > 0):
            #                pm_calc_pec(rdata) ==
            for ii in range(inlen-1):
                rdat_out.append(int(rdata[ii]))
            return rdat_out;
        else:
            self.open_status = 0;
            return -1;

    def pm_write_byte (self,i2c_addr7b,cmd,dat,pec=0):
        inlen = 3;
        if(pec > 0):
            inlen = inlen + 1;
        wdata = (ctypes.c_uint8 * (inlen))()
        rdata = (ctypes.c_uint8 * (inlen))()
        wdata[0] = (i2c_addr7b & 0xff) << 1;
        wdata[1] = (cmd & 0xff) ;
        wdata[2] = (dat & 0xff) ;
        ## todo calc pec
        #pec_code = 0x1f
        pec_code = self.pm_calc_pec([wdata[0],wdata[1],wdata[2]])
        if(pec > 0):
            wdata[inlen-1] = (pec_code & 0xff) ; ##
        if( self.ch341dll.CH341StreamI2C (self.usb_id, inlen, wdata ,0, rdata ) > 0):
            return 1;
        else:
            self.open_status = 0;
            return -1;

    def pm_write_word (self, i2c_addr7b, cmd, dat,  pec=0):
        inlen = 4;
        if (pec > 0):
            inlen = inlen + 1;
        wdata = (ctypes.c_uint8 * (inlen))()
        rdata = (ctypes.c_uint8 * (inlen))()
        wdata[0] = (i2c_addr7b & 0xff) << 1;
        wdata[1] = (cmd & 0xff);
        wdata[2] = (dat & 0xff);
        wdata[3] = (dat >> 8) & 0xff;
        ## todo calc pec
        pec_code = self.pm_calc_pec([wdata[0],wdata[1],wdata[2],wdata[3]])
        if (pec > 0):
            wdata[inlen - 1] = (pec_code & 0xff);  ##
        if (self.ch341dll.CH341StreamI2C(self.usb_id, inlen, wdata, 0, rdata) > 0):
            return 1;
        else:
            self.open_status = 0;
            return -1;


    def pm_write_block (self, i2c_addr7b, cmd, dat,  pec=0):
        inlen = 3;
        lendata = len(dat);
        inlen += len(dat);
        if (pec > 0):
            inlen = inlen + 1;
        wdata = (ctypes.c_uint8 * (inlen))()
        rdata = (ctypes.c_uint8 * (inlen))()
        wdata[0] = (i2c_addr7b & 0xff) << 1;
        wdata[1] = (cmd & 0xff);
        wdata[2] = ( lendata & 0xff);
        for jj in range(len(dat)):
            wdata[3+jj] = (dat[jj] & 0xff);
        ## todo calc pec
        dat_list = [];
        for clccrc in range(inlen-1):
            dat_list.append(wdata[clccrc])
        pec_code = self.pm_calc_pec(dat_list);
        if (pec > 0):
            wdata[inlen - 1] = pec_code;
        if (self.ch341dll.CH341StreamI2C(self.usb_id, inlen, wdata, 0, rdata) > 0):
            return 1;
        else:
            self.open_status = 0;
            return -1;


    def pm_write_infine_reg(self, i2c_addr7b, reg_addr , wdat,  pec=0):
        inlen = 7;
        if (pec > 0):
            inlen = inlen + 1;
        wdata = (ctypes.c_uint8 * (inlen))()
        rdata = (ctypes.c_uint8 * (inlen))()
        wdata[0] = (i2c_addr7b & 0xff) << 1;
        wdata[1] = (0xD0 & 0xff);
        wdata[2] = (0x04 & 0xff);
        wdata[3] = (reg_addr & 0xff);
        wdata[4] = ((reg_addr>>8) & 0xff);
        wdata[5] = (wdat & 0xff);
        wdata[6] = ((wdat>>8) & 0xff);
        ## todo calc pec
        dat_list = [];
        for clccrc in range(inlen-1):
            dat_list.append(wdata[clccrc])
        pec_code = self.pm_calc_pec(dat_list);
        if (pec > 0):
            wdata[inlen - 1] = pec_code;
        if (self.ch341dll.CH341StreamI2C(self.usb_id, inlen, wdata, 0, rdata) > 0):
            return 1;
        else:
            self.open_status = 0;
            return -1;


    def pm_read_infine_reg(self, i2c_addr7b, reg_addr ,  pec=0):
        inlen = 7;
        if (pec > 0):
            inlen = inlen + 1;
        wdata = (ctypes.c_uint8 * (inlen))()
        rdata = (ctypes.c_uint8 * (inlen))()
        wdata[0] = (i2c_addr7b & 0xff) << 1;
        wdata[1] = (0xD0 & 0xff);
        wdata[2] = (reg_addr & 0xff);
        wdata[3] = ((reg_addr>>8) & 0xff);
        ## todo calc pec
        dat_list = [];
        for clccrc in range(inlen-1):
            dat_list.append(wdata[clccrc])
        pec_code = self.pm_calc_pec(dat_list);
        read_num = 2;
        if (pec > 0):
            read_num += 1;
        if (self.ch341dll.CH341StreamI2C(self.usb_id, 4 , wdata, read_num, rdata) > 0):
            return rdata;
        else:
            self.open_status = 0;
            return -1;

















    def spi_oled1306_3w(self, not_cmd, data):
        if (self.check_status() < 1):
            return -1;
        wdata = (ctypes.c_uint8 * 2)()
        wdata[0] = (( not_cmd & 0x1 ) << 7) + (data >> 1);
        wdata[1] = (data & 1)<<7;
        if (self.ch341dll.CH341StreamSPI4(self.usb_id, 0x80, 2, wdata)):
            return 1
        else:
            return -1;

    def ch341_spi4w_stream(self,din):
        if(self.check_status() < 1):
            return -1;
        inlen = len(din);
        if inlen > 4000:
            print("should not greater than 4000");
            return -1;
        wdata = (ctypes.c_byte* (inlen))()
        for ii in range(inlen):
            wdata[ii] = int(din[ii]) & 0xff;
        #print("debug: wlen=",inlen)
        #print("debug: wdata=",wdata[100:])
        #print("debug: get_inptus: ",din,"length = ",len(din), inlen);
        if (self.ch341dll.CH341StreamSPI4(self.usb_id, 0x80, inlen, wdata)):
            return wdata;
        else:
            return -1;

    def ch341_get_input(self):
        if(self.check_status() < 1):
            return -1;
        inlen = 4
        rdata = (ctypes.c_byte* (inlen))()
        for ii in range(inlen):
            rdata[ii] = 0;
        if (self.ch341dll.CH341GetInput(self.usb_id, rdata)):
            return (rdata[0] + rdata[1]*256 + rdata[3]*256);
        else:
            return -1;

    def ch341_set_output(self,set_range, set_dir, set_v):
        if(self.check_status() < 1):
            return -1;
        if (self.ch341dll.CH341SetOutput(self.usb_id, set_range,set_dir, set_v)):
            return 1;
        else:
            return -1;

    def ch341_oled306_3w_stream(self,din):
        if(self.check_status() < 1):
            return -1;
        inlen = len(din);
        if inlen > 4000:
            print("should not greater than 4000");
            return -1;
        wdata = (ctypes.c_byte* (inlen))()
        rdata = (ctypes.c_byte* (inlen))()
        for ii in range(inlen):
            wdata[ii] = int(din[ii]) & 0xff;
        #print("debug: wlen=",inlen)
        #print("debug: wdata=",wdata[100:])
        #print("debug: get_inptus: ",din,"length = ",len(din), inlen);
        if (self.ch341dll.CH341StreamSPI4(self.usb_id, 0x80, inlen, wdata)):
            return 1;
        else:
            return -1;

if __name__ == "__main__":
    hd = CH341DEV(0)
    #hd.ch341_close()
    xx = hd.ch341_get_input();
    yy = xx & 0xff
    print("get_input GPIO date D7:D0:", hex(yy))
    hd.ch341_close();
