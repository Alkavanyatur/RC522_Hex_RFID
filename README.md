# RC522_Hex_RFID
This program changes the RC522 rfid result to another valid result for others readers.

# What this program do:


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
