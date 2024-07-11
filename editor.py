def checksumCalc (savefile):
	with open(savefile, 'rb+') as f:
		ram = bytearray(f.read())
		checksum = 0xff
		for c in ram[0x2598:0x3523]:
			checksum -= c
		ram[0x3523]=checksum&0xff
		f.seek(0,0)
		f.write(ram)

file = 'aaaaa.sav'