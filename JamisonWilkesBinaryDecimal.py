#Jamison Wilkes
#AssignmentLab02
#CS2705-Spring

#192.168.16.13
octet01 = 192
octet02 = 168
octet03 = 16
octet04 = 13

binOctet01 = bin(octet01)[2:].zfill(8)
binOctet02 = bin(octet02)[2:].zfill(8)
binOctet03 = bin(octet03)[2:].zfill(8)
binOctet04 = bin(octet04)[2:].zfill(8)

BinaryNumber = "#1. The binary format of the IP address is: {0}.{1}.{2}.{3}"
print(BinaryNumber.format(binOctet01,binOctet02,binOctet03,binOctet04))

#164.10.241.2 
octet01 = 164
octet02 = 10
octet03 = 241
octet04 = 2

binOctet01 = bin(octet01)[2:].zfill(8)
binOctet02 = bin(octet02)[2:].zfill(8)
binOctet03 = bin(octet03)[2:].zfill(8)
binOctet04 = bin(octet04)[2:].zfill(8)

BinaryNumber = "#2. The binary format of the IP address is: {0}.{1}.{2}.{3}"
print(BinaryNumber.format(binOctet01,binOctet02,binOctet03,binOctet04))

#10.244.116.15
octet01 = 10
octet02 = 244
octet03 = 116
octet04 = 15

binOctet01 = bin(octet01)[2:].zfill(8)
binOctet02 = bin(octet02)[2:].zfill(8)
binOctet03 = bin(octet03)[2:].zfill(8)
binOctet04 = bin(octet04)[2:].zfill(8)

BinaryNumber = "#3. The binary format of the IP address is: {0}.{1}.{2}.{3}"
print(BinaryNumber.format(binOctet01,binOctet02,binOctet03,binOctet04))

#15.255.200.153 
octet01 = 15
octet02 = 255
octet03 = 200
octet04 = 153

binOctet01 = bin(octet01)[2:].zfill(8)
binOctet02 = bin(octet02)[2:].zfill(8)
binOctet03 = bin(octet03)[2:].zfill(8)
binOctet04 = bin(octet04)[2:].zfill(8)

BinaryNumber = "#4. The binary format of the IP address is: {0}.{1}.{2}.{3}"
print(BinaryNumber.format(binOctet01,binOctet02,binOctet03,binOctet04))

#172.99.62.9 
octet01 = 172
octet02 = 99
octet03 = 62
octet04 = 9

binOctet01 = bin(octet01)[2:].zfill(8)
binOctet02 = bin(octet02)[2:].zfill(8)
binOctet03 = bin(octet03)[2:].zfill(8)
binOctet04 = bin(octet04)[2:].zfill(8)

BinaryNumber = "#5. The binary format of the IP address is: {0}.{1}.{2}.{3}"
print(BinaryNumber.format(binOctet01,binOctet02,binOctet03,binOctet04))

#IP Addresses
#10110100.11101011.00001000.10010001 
octet01 = '10110100'
decOctet01 = int(octet01, 2)
octet02 = '11101011'
decOctet02 = int(octet02, 2)
octet03 = '00001000'
decOctet03 = int(octet03, 2)
octet04 = '10010001'
decOctet04 = int(octet04, 2)

IPAddress = "#6. The decimal IP address is: {0}.{1}.{2}.{3}"
print(IPAddress.format(decOctet01,decOctet02,decOctet03,decOctet04))

#10001100.11111111.11000000.00000001
octet01 = '10001100'
decOctet01 = int(octet01, 2)
octet02 = '11111111'
decOctet02 = int(octet02, 2)
octet03 = '11000000'
decOctet03 = int(octet03, 2)
octet04 = '00000001'
decOctet04 = int(octet04, 2)

IPAddress = "#7. The decimal IP address is: {0}.{1}.{2}.{3}"
print(IPAddress.format(decOctet01,decOctet02,decOctet03,decOctet04))

#00010001.11001100.00000001.00010010 
octet01 = '00010001'
decOctet01 = int(octet01, 2)
octet02 = '11001100'
decOctet02 = int(octet02, 2)
octet03 = '00000001'
decOctet03 = int(octet03, 2)
octet04 = '00010010'
decOctet04 = int(octet04, 2)

IPAddress = "#8. The decimal IP address is: {0}.{1}.{2}.{3}"
print(IPAddress.format(decOctet01,decOctet02,decOctet03,decOctet04))

#11100111.00110011.10101010.11111110 
octet01 = '11100111'
decOctet01 = int(octet01, 2)
octet02 = '00110011'
decOctet02 = int(octet02, 2)
octet03 = '10101010'
decOctet03 = int(octet03, 2)
octet04 = '11111110'
decOctet04 = int(octet04, 2)

IPAddress = "#9. The decimal IP address is: {0}.{1}.{2}.{3}"
print(IPAddress.format(decOctet01,decOctet02,decOctet03,decOctet04))

#00010111.11101110.01010101.10000000 
octet01 = '00010111'
decOctet01 = int(octet01, 2)
octet02 = '11101110'
decOctet02 = int(octet02, 2)
octet03 = '01010101'
decOctet03 = int(octet03, 2)
octet04 = '10000000'
decOctet04 = int(octet04, 2)

IPAddress = "#10. The decimal IP address is: {0}.{1}.{2}.{3}"
print(IPAddress.format(decOctet01,decOctet02,decOctet03,decOctet04))