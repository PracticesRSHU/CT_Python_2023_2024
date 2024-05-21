#Working byte
import struct 
valid_gif_header = b'GIF89a' 
# f = open('animation.gif', 'rb') 
f = open('E:\\Tetiana\\CT_Python_2023_2024\\semestr_IV\\working_data\\animation.gif', 'rb') 
data = f.read(10) 
print(data[:10])
print(data[6:8]) #6,7 width
print(data[8:10])# 8,9 height
# L,l, I, i => 4 байт H, h (коротке ціле число) 2байт
print("width=", struct.pack('<H',500))
print("height=",struct.pack('<H',427))
if data[:6] == valid_gif_header:
    width = struct.unpack('<H', data[6:8])[0] 
    height = struct.unpack('<H', data[8:10])[0]  
    # width, height = struct.unpack('>HH', data[6:10])  #big-endian  L -> unsigned lon  g
    print('Valid GIF, width', width, 'height', height)
else:
    print('Not a valid GIF')
f.close()