#Sistema decimal
print("Dime el número de bytes")
bytes=int(input())
bytesSD=bytes
gb = bytesSD // 1000000000
bytesSD = bytesSD % 1000000000
mb = bytesSD // 1000000
bytesSD = bytesSD % 1000000
kb = bytesSD // 1000
bytesSD = bytesSD % 1000
print(f"{bytes} bytes en sistema decimal (SI): {gb} GB, {mb} MB, {kb} KB, {bytesSD} bytes")
#Sistema binario
bytesSB=bytes
gbSB= bytesSB // (1024*1024*1024)
bytesSB = bytesSB % (1024*1024*1024)
mbSB = bytesSB // (1024*1024)
bytesSB = bytesSB % (1024*1024)
kbSB = bytesSB // 1024
bytesSB =bytesSB % 1024
print(f"{bytes} bytes en sistema binario (IEC): {gbSB} GiB, {mbSB} MiB, {kbSB} KiB, {bytesSB} bytes")
