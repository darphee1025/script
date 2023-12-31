#from Load_excel import *
def p_red(dat):
    print('\033[2;31m' + dat +  '\033[0;0m',end="")
#p_red('nihao')
#print("nida")
class pyt_reg():
    #this is class for a whole 8bits or 16 or 32bits, pyt_reg
    def __init__(self,name="RegName",bus_hd=None,bits_w=8,addr=0x0,desc=""):
        self.name = name;
        self.bits_w = bits_w;
        self.addr = addr ;
        self.default_v = 0x0;
        self.value = 0x0;
        #def get_mirrored_value(self):
        self.mirrored_value = 0x0;
        self.fl = []; # field list ,for short
        self.desc = desc ;
        self.bus_hd = bus_hd;

    def get_rw_mask(self):
        rw_mask = 0;
        for indf in range(len(self.fl)):
            cur_rf = self.fl[indf];
            if (self.fl[indf].rw == "RW"):
                rw_mask += ( 0xfffffff >> (31-cur_rf.get_rf_msb()))  &  ( 0xffffffff << cur_rf.start_b )
            return rw_mask

    def set(self,dat):
        value = dat ;
        reg_msk = 0xffffffff & (2 ** self.bits_w - 1);
        for indf in range(len(self.fl)):
            cur_rf = self.fl[indf];
            if (self.fl[indf].rw == "RW"):
                fl_msk = (2**cur_rf.bits_w - 1) << cur_rf.start_b;
                setv = (fl_msk & dat) >> cur_rf.start_b;
                cur_rf.set(setv)
                self.value = value
        return value

    def sync(self,dat):
        self.set(dat);
        for indf in range(len(self.fl)):
            cur_rf = self.fl[indf];
            cur_rf.mirrored_value = cur_rf.value;

    def show_desc(self,dat):
        value = dat ;
        reg_msk = 0xffffffff & (2 ** self.bits_w - 1);
        tmp_str = "[INFO] -show_desc->";print(tmp_str)
        tmp_str = "    "
        tmp_str += (self.name).ljust(20)
        tmp_str += "="
        print(tmp_str, end="");
        p_red(hex(dat));
        tmp_str = "  "
        tmp_str = tmp_str.ljust(28)
        tmp_str += " default=" + hex(self.get_reg_default_v())
        print(tmp_str)
        for indf in range(len(self.fl)):
            tmp_str = ""
            cur_rf = self.fl[indf];
            tmp_str = "  " + cur_rf.name + " "
            tmp_str = tmp_str.ljust(20)
            tmp_str += "[" + cur_rf.get_rf_msb().__str__() + ":" + cur_rf.start_b.__str__() + "] "
            tmp_str = tmp_str.ljust(26);
            fl_msk = (2**cur_rf.bits_w - 1) << cur_rf.start_b;
            setv = (fl_msk & dat) >> cur_rf.start_b;
            tmp_str += " " + cur_rf.rw
            tmp_str = tmp_str.ljust(30)
            tmp_str += "=" ;
            print(tmp_str,end="");
            p_red(hex(setv));
            tmp_str = "   "
            tmp_str += cur_rf.desc;
            print(tmp_str)
        return value

    def get(self):
        value = 0;
        for indf in range(len(self.fl)):
            cur_rf = self.fl[indf];
            if (self.fl[indf].rw == "RW"):
                value += cur_rf.value << cur_rf.start_b;
            if (self.fl[indf].rw == "RO"):
                value += cur_rf.value << cur_rf.start_b;
            #print("debug32： reg_name",self.name,"fd_name:",cur_rf.name,"fd_v",cur_rf.value,"value sum=",value,"indf:",indf)
            self.value = value
        return value

    def need_update(self):
        value = 0;
        for indf in range(len(self.fl)):
            cur_rf = self.fl[indf];
            if (cur_rf.need_update()):
                return 1
        return 0

    def update(self):
        rslt = self.bus_hd.write(self.addr, self.get())
        if(rslt):
            self.sync(self.get())
        return rslt ;

    def write(self,wdata):
        wdata = (2**self.bits_w - 1) & wdata;
        rslt = self.bus_hd.write(self.addr, wdata)
        if (rslt):
            self.sync(wdata)
        return rslt;

    def read(self,to_pr=0):
        rdata = self.bus_hd.read(self.addr)
        self.sync(rdata);
        if(to_pr):
            print('[INFO]  ' + self.name + " Call read @addr=" + hex(self.addr) + ", get rdata=",hex(rdata))
        return rdata;

    def reads(self):
        rdata = self.bus_hd.read(self.addr)
        self.sync(rdata);
        self.show_desc(rdata)
        return rdata;

    def get_reg_default_v (self):
        default_v = 0;
        for indf in range(len(self.fl)):
            cur_rf = self.fl[indf];
            if (self.fl[indf].rw == "RW"):
                default_v += cur_rf.default_v << cur_rf.start_b;
            if (self.fl[indf].rw == "RO"):
                default_v += cur_rf.default_v << cur_rf.start_b;
            #print("debug32： reg_name",self.name,"fd_name:",cur_rf.name,"fd_v",cur_rf.default_v,"default_v sum=",default_v,"indf:",indf)
            self.default_v = default_v
        return default_v

    def get_fl_bits(self):
        bits_sum = 0;
        for indf in range(len(self.fl)):
            cur_rf = self.fl[indf];
            bits_sum += cur_rf.bits_w ;
        return bits_sum

    def check_fl_bits_index(self):
        error_cnt = 0;
        last_start_b = self.bits_w;
        for indf in range(len(self.fl)):
            cur_rf = self.fl[indf];
            if(cur_rf.get_rf_msb() +1 != last_start_b):
                print("Error bits index check fail Reg:",self.name,"fiedl:",cur_rf.name);
                error_cnt += 1;
            last_start_b = cur_rf.start_b;
        if(last_start_b > 0):
            print("Error bits index last not 0 check fail Reg: ", self.name, "fiedl:", cur_rf.name);
            error_cnt += 1;
        return error_cnt

    def check_fl_bits_index_mono(self):
        error_cnt = 0;
        last_start_b = self.bits_w;
        for indf in range(len(self.fl)):
            cur_rf = self.fl[indf];
            if(cur_rf.get_rf_msb() +1 > last_start_b):
                print("Error bits index must Monotonically increase; check fail Reg:",self.name,"fiedl:",cur_rf.name);
                error_cnt += 1;
            last_start_b = cur_rf.start_b;
        if(last_start_b > 0):
            print("Error bits index last not 0 check fail Reg: ", self.name, "fiedl:", cur_rf.name);
            error_cnt += 1;
        return error_cnt

    def gets(self):
        rdata = self.get()
        self.show_desc(rdata)

    def check_fl_default_v(self):
        error_cnt = 0;
        for indf in range(len(self.fl)):
            cur_rf = self.fl[indf];
            if (cur_rf.rw == "RW"):
                limit_v =  2**(cur_rf.bits_w)-1
                if (limit_v < cur_rf.default_v):
                    print("Error Field Default Value is too big!! @reg:",self.name,"field@",cur_rf.name,"V=",hex(cur_rf.default_v),"limit=",hex(limit_v))
                    error_cnt += 1
        return error_cnt

    #    def reg_check(self):


class pyt_reg_field():
    #this is class for a regfield
    def __init__(self,name="regf",bits_w=1,start_b=0,default_v=0,rw="RW",desc=""):
        self.name = name
        self.bits_w = bits_w;
        self.start_b = start_b;
        self.default_v = default_v;
        self.value     = default_v ;
        self.mirrored_value = default_v ;
        self.rw = rw; #'rw', 'ro' suppert only for Version 0.1
        self.desc = desc;

    def get_rf_msb(self):
        return (self.start_b + self.bits_w - 1);

    def get_mirrored_value(self):
        return self.mirrored_value

    def need_update(self):
        return (self.mirrored_value != self.value);

    def fl_update(self,v):
        self.mirrored_value = v;
        self.value          = v;

    def get(self):
        return  self.value

    def set(self,dat):
        self.value = dat & (2**self.bits_w - 1);
        return  self.value ;

#
#class REGA (pyt_reg):
#    #def __init__(self):
#    def __init__(self, name="RegName",bus_hd=None,bits_w=8, addr=0x1, desc=""):
#        super(REGA, self).__init__(name,bus_hd, bits_w,addr,desc)
#        self.fld1     = pyt_reg_field("fld1",4,0,0xa,'RW',"diyige field")
#        self.curr_set = pyt_reg_field("curr_set",4,4,0xb,'RW',"curr set , 0=4ma, 1=8ma")
#        self.fl       = [self.fld1,self.curr_set]
#
#class REGB (pyt_reg):
#    #def __init__(self):
#    def __init__(self, name="RegName",bus_hd=None, bits_w=8, addr=0xB, desc=""):
#        super(REGB, self).__init__(name,bus_hd, bits_w,addr,desc)
#        self.bf1     = pyt_reg_field("fld1",2,0,0xa,'RW',"diyf bf1 2bits")
#        self.bf2     = pyt_reg_field("curr_set",6,3,0xb,'RW',"curr set 6bs , 0=4ma, 1=8ma")
#        self.fl       = [self.bf1,self.bf2]
#
#class CHIP_REG():
#    def __init__(self,hdin):
#        self.U_RAGA = REGA("U_REGA",hdin)
#        self.U_RAGB = REGB("U_REGB",hdin)
#        self.bus_hd = hdin;
#
#class bus_opt():
#    def __init__(self,name="abcd"):
#        self.name = name
#
#    def bus_rd (self,addr):
#        return 0x1f;
#    def bus_wr (self,addr,wdata):
#        return 0x1;
#
#hd = bus_opt("BUS_I2C")
#CHIP_ABCD = CHIP_REG(hd);
#hex(CHIP_ABCD.U_RAGA.fld1.get())
#hex(CHIP_ABCD.U_RAGA.curr_set.get())
#hex(CHIP_ABCD.U_RAGA.get())
#
#hex(CHIP_ABCD.U_RAGA.curr_set.set(0x4))
#hex(CHIP_ABCD.U_RAGA.fld1.set(0x3))
#hex(CHIP_ABCD.U_RAGA.get())
#
#hex(CHIP_ABCD.U_RAGA.curr_set.set(0x4))
#hex(CHIP_ABCD.U_RAGA.fld1.set(0x3))
#hex(CHIP_ABCD.U_RAGA.set(0x58))

######### -- need to update

# xx.fld1.value = 3
# print(xx.fld1.value )

#class pyt_reg_field():
#    #this is class for a regfield
#    def __init__(self,name="regf",bits_w=1,start_b=0,default_v=0,rw="rw",desc=""):
#        self.name = name
#        self.bits_w = bits_w;
#        self.start_b = start_b;
#        self.default_v = default_v;
#        self.value     = default_v ;
#        self.rw = rw; #'rw', 'ro' suppert only for Version 0.1
#        self.desc = desc;
#    def get_rf_msb(self):
#        return (self.start_b + self.bits_w - 1);
