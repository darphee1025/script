#xx = list(range(1,100))
def p_red(dat):
    print('\033[2;31m' + dat +  '\033[0;0m',end="")

def list_reg_print(inlist, start_addr=0, diff_ref = []):
    if (start_addr >  0):
        zeros_s = [];
        for jj in range(start_addr):
            zeros_s.append(0);
        xx = zeros_s  + inlist
    else:
        xx = inlist

    inlen = len(xx);
    print ("ADDR-> ",end="")
    if (len(diff_ref) == len(xx)):
        for ii in range(16):
            print("%02X " % ii,end="")
            if ii == 7:
                print("| ",end="")
        print("")
        ### first line:
        for ind in range(inlen):
            if (ind %16 == 0):
                print("  %02X:  " % ind, end="")
            if (xx[ind] == diff_ref[ind]):
                print("%02X " % xx[ind], end="");  # diff color --
            else:
                tp  = "{0:02X} ".format(xx[ind])
                p_red(tp);  # diff color --
            if (ind % 16 == 7):
                print("| ",end="")
            if (ind %16 == 15):
                print("")

    else:
        for ii in range(16):
            print("%02X " % ii,end="")
            if ii == 7:
                print("| ",end="")
        print("")
        ### first line:
        for ind in range(inlen):
            if (ind %16 == 0):
                print("  %02X:  " % ind, end="")
            print("%02X " % xx[ind],end="")
            if (ind % 16 == 7):
                print("| ",end="")
            if (ind %16 == 15):
                print("")

    print("")


#xx = [1,2,3,4,8,8,0]
#yy = [2,3,5,8,9,0]
#list_reg_print(yy,0,xx)