
'''

What this program do:


RC522 reads rfid tags giving a decimal number than is in fact a Hex number. The tag on other readers give
different results.

This program allow to transform the RC522 result to another reader tag result.

It can change depending of the number of bytes of the tag.



As example:

RC522 reads 421021516083 as rfid result

421021516083 in hex 6206D68133

We remove the fifth control byte

62 06 D6 81 (33)

We rotate the number.

81 D6 06 62

Then, we transform to decimal

2178287202

'''


# 4 bytes
def Read_Tag_4(uid):
    # Print UID 4 bytes
    print("tag UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3]))
    tag_endian = (uid[3], uid[2], uid[1], uid[0])
    print('tag endian:', tag_endian)
    tag_hex = hex(uid[3]), hex(uid[2]), hex(uid[1]), hex(uid[0])
    print ('tag hex:', tag_hex)
    tag_str = str(hex(uid[3])[2:]), str(hex(uid[2])[2:]), str(hex(uid[1])[2:]), str(hex(uid[0])[2:])
    print('tag string:', tag_str)
    tag_str = str(hex(uid[3])[2:]) + str(hex(uid[2])[2:]) + str(hex(uid[1])[2:]) + str(hex(uid[0])[2:])
    print('tag hex string concat:', tag_str)
    tag = int(tag_str, 16)
    print('tag dec:', tag)


# 5 bytes
def Read_Tag_5(uid):
    # Print UID 5 bytes
    print("tag UID: %s,%s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3], uid[4]))
    tag_endian = (uid[4],uid[3], uid[2], uid[1], uid[0])
    print('tag endian:', tag_endian)
    tag_hex = hex(uid[4]),hex(uid[3]), hex(uid[2]), hex(uid[1]), hex(uid[0])
    print('tag hex:', tag_hex)
    tag_str = str(hex(uid[4])[2:]),str(hex(uid[3])[2:]), str(hex(uid[2])[2:]), str(hex(uid[1])[2:]), str(hex(uid[0])[2:])
    print('tag string:', tag_str)
    tag_str = str(hex(uid[4])[2:]) + str(hex(uid[3])[2:]) + str(hex(uid[2])[2:]) + str(hex(uid[1])[2:]) + str(hex(uid[0])[2:])
    print('tag hex string concat:', tag_str)
    tag = int(tag_str, 16)
    print('tag dec:', tag)


# 7 bytes
def Read_Tag_7(uid):
    # Print UID 7 bytes
    print("tag UID: %s,%s,%s,%s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3], uid[4], uid[5], uid[6]))
    tag_endian = (uid[6],uid[5],uid[4],uid[3], uid[2], uid[1], uid[0])
    print('tag endian:', tag_endian)
    tag_hex = hex(uid[6]), hex(uid[5]),hex(uid[4]),hex(uid[3]),hex(uid[2]), hex(uid[1]), hex(uid[0])
    print('tag hex:', tag_hex)
    tag_str = str(hex(uid[6])[2:]), str(hex(uid[5])[2:]), str(hex(uid[4])[2:]),  str(hex(uid[3])[2:]), str(hex(uid[2])[2:]), str(hex(uid[1])[2:]), str(hex(uid[0])[2:])
    print('tag string:', tag_str)
    tag_str = str(hex(uid[6])[2:]) +str(hex(uid[5])[2:]) +str(hex(uid[4])[2:]) +str(hex(uid[3])[2:]) + str(hex(uid[2])[2:]) + str(hex(uid[1])[2:]) + str(hex(uid[0])[2:])
    print('tag hex string concat:', tag_str)
    tag = int(tag_str, 16)
    print('tag dec:', tag)



# Code to test
# Test Array with one result. Add several if your need
array_qr = [421021516083]

def returnHexStr(valor):
    return str(hex(valor)).replace("0x", "").zfill(2)


def rc522_to_rfidDec(value):
    numberDec = value
    numberHex = hex(numberDec)
    hexString = str(numberHex).replace("0x", "").zfill(10)
    byte_array = bytearray.fromhex(hexString)
    hexString = "0x"+returnHexStr(byte_array[3])+returnHexStr(byte_array[2])+returnHexStr(byte_array[1])+returnHexStr(byte_array[0])
    an_integer = int(hexString, 16)
    print(value, "-",an_integer)


for x in array_qr:
    rc522_to_rfidDec(x)