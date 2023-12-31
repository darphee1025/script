to_calc0 = [0x22, 0x00, 0x23, 0x00]
to_calc1 = [0x22, 0x21, 0x04, 0x00]


def calc_crc8 (to_calc):
    crc8 = 0;
    for ii in to_calc:
        print("---------", hex(ii), "-----------------")
        for jj in range(8):
            print("bit",7-jj,int((ii & (0x1 << (7-jj))) > 0))
            bitv = int((ii & (0x1 << (7-jj))) > 0);
            crcb7 = int((crc8 &  0x80)>0);
            to_add = bitv ^ crcb7;
            crc8_x2 = 0xff & (crc8 << 1);
            comb_v   = crc8_x2 ^ (7*to_add);
            crc8 = comb_v & 0xff
    return crc8;
#print(hex(crc8))
print(hex(calc_crc8(to_calc0)))
print(hex(calc_crc8(to_calc1)))


