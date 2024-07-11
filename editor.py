



# character map
char_map = {'80':'A', '81':'B', '82':'C', '83':'D', '84':'E', '85':'F', '86':'G', '87':'H', '88':'I', '89':'J', '8A':'K', '8B':'L', '8C':'M', '8D':'N', '8E':'O', '8F':'P', '90':'Q', '91':'R', '92':'S', '93':'T', '94':'U', '95':'V', '96':'W', '97':'X', '98':'Y', '99':'Z', '9A':'(', '9B':')', '9C':':', '9D':';', '9E':'[', '9F':']', 'A0':'a', 'A1':'b', 'A2':'c', 'A3':'d', 'A4':'e', 'A5':'f', 'A6':'g', 'A7':'h', 'A8':'i', 'A9':'j', 'AA':'k', 'AB':'l', 'AC':'m', 'AD':'n', 'AE':'o', 'AF':'p', 'B0':'q', 'B1':'r', 'B2':'s', 'B3':'t', 'B4':'u', 'B5':'v', 'B6':'w', 'B7':'x', 'B8':'y', 'B9':'z', 'BA':'é', 'E0':"'", 'E1':'PK', 'E2':'MN', 'E3':'-', 'E6':'?', 'E7':'!', 'E8':'.', 'EF':'♂', 'E4':',', 'E5':'♀', 'E6':'0', 'E7':'1', 'E8':'2', 'E9':'3', 'EA':'4', 'EB':'5', 'EC':'6', 'ED':'7', 'EE':'8', 'EF':'9'}

def decode_text(var):
    decoder = str(var)[2:-1]
    decoder = decoder.replace("\\", " ")
    decoder = decoder.replace('x', '')
    for k, v in char_map.items():
        decoder = decoder.replace(k, v)
    decoder = decoder.replace(' ', '')
    return decoder

# checksum calculator
def checksumCalc(savefile):
	with open(savefile, 'rb+') as f:
		ram = bytearray(f.read())
		checksum = 0xff
		for c in ram[0x2598:0x3523]:
			checksum -= c
		ram[0x3523]=checksum&0xff
		f.seek(0,0)
		f.write(ram)
def getPlayerName(savefile):
	with open(savefile, 'rb+') as f:
		ram = bytearray(f.read())
		f.seek(0x2598)
		name = decode_text(f.read(7))
		return name
file = '100.sav'

print(getPlayerName(file))