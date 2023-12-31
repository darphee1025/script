class chip_hd:
    def __init__(self,i2c_addr, i2c_hd):
        self.i2c_addr = i2c_addr; ##addr in 8?7bits.
        self.i2c_hd   = i2c_hd;

    def wr_i2c (self,i2c_hd,wdat):
        rslt = i2c_hd.wr_i2c(self.i2c_addr,wdat);
        if(rslt < 1):
            print("Error Write I2C/Pmbus fail, may be NACK!!!!")
        return rslt;

    def rd_i2c (self,i2c_hd):
        rslt = i2c_hd.wr_i2c(self.i2c_addr,wdat);
        if(rslt < 1):
            print("Error Write I2C/Pmbus fail, may be NACK!!!!")
        return rslt;

class pmbus_cmd:
    def __init__(self,chip_hd, name="PAGE",code=0x88,bw=1,readable=1,value=0x0,dat_format=0x0):
        self.chip_hd = chip_hd ;
        self.name = name;
        self.code = code;
        self.bw   = bw;
        self.readable = readable ;
        self.dat_format = dat_format;
    def wr (self,w_v):
        wdat = [self.code]
        if (len(w_v) > 1):
            for ii in range(len(w_v)):
                wdat.append(w_v[ii])
        else:
            if(bw == 1):
                wdat = [self.code,w_v]
            else:
                if(w_v > 0xffff):
                    print("Error pmbus_cmd ",pmbus_cmd.name,"wdata=",w_v,"ERROR! > 0xffff");
                else:
                    wdat = [self.code,w_v & 0xff, (w_v & 0xff00) >> 8 ];
        return self.chip_hd.wr_i2c(wdat)

    def rd (self):
        wdat = [self.code]
        if (len(w_v) > 1):
            for ii in range(len(w_v)):
                wdat.append(w_v[ii])
        else:
            if(bw == 1):
                wdat = [self.code,w_v]
            else:
                if(w_v > 0xffff):
                    print("Error pmbus_cmd ",pmbus_cmd.name,"wdata=",w_v,"ERROR! > 0xffff");
                else:
                    wdat = [self.code,w_v & 0xff, (w_v & 0xff00) >> 8 ];
        return self.chip_hd.wr_i2c(wdat)



class pmbus13_command:
    def __init__(self):
        self.



    def is_valid_cmd(self):

