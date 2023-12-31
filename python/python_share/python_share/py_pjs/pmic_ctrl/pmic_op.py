from ch341dll_32bits_wrap.ch341dll_wrap  import *
class pmic_i2c_options(CH341DEV):
    def __init__(self,ch341_index):
        super(pmic_i2c_options,self).__init__(ch341_index);
#        self.i2c_addr7b = i2c_addr; ##addr in 8?7bits.
        self.valid_reg_addr_list = [*range(0,255,1)];
##### -- pm bus options
    def i2c_calc_pec (self, to_calc):
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

    def i2c_write (self,i2c_addr7b,addr,ldata,pec=0):
        #print("debug: call i2c_write ---")
        lenl = len(ldata);
        if lenl < 1:
            print("Error at less one wdata needed!!", reg_addr)
            return -1;
        inlen = 2+lenl;
        if(pec > 0):
            inlen = inlen + 1;
        wdata = (ctypes.c_uint8 * (inlen))()
        rdata = (ctypes.c_uint8 * (inlen))()
        wdata[0] = (i2c_addr7b & 0xff) << 1;
        wdata[1] = (addr & 0xff) ;
        for ii in range(lenl):
            wdata[2+ii] = (ldata[ii] & 0xff) ;
        
        ## todo calc pec
        pec_code = self.i2c_calc_pec(wdata)
        if(pec > 0):
            wdata[inlen] = (pec_code & 0xff) ; ##
        if( self.ch341dll.CH341StreamI2C (self.usb_id, inlen, wdata ,0, rdata ) > 0):
            return 1;
        else:
            return -1;

    def i2c_read (self,i2c_addr7b,reg_addr,read_num=1,pec=0):
        inlen = read_num;
        if(pec > 0):
            inlen = inlen + 1;
        wdata = (ctypes.c_uint8 * (2))()
        rdata = (ctypes.c_uint8 * (inlen))()
        wdata[0] = (i2c_addr7b & 0xff) << 1;
        wdata[1] = (reg_addr & 0xff) ;
        if( self.ch341dll.CH341StreamI2C (self.usb_id, 2, wdata ,inlen, rdata ) > 0):
            ## check --- calc pec
            rdat_out = [];
            pec_code = 0x1f
#            if (pec_code > 0):
#                i2c_calc_pec(rdata) ==
            for ii in range(inlen):
                rdat_out.append(int(rdata[ii]))
#            rdat_out = int( rdata[0] );
            return rdat_out;
        else:
            return -1;

