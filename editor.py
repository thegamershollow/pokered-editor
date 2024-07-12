# character map
char_map = {'7F':' SPACE ','80':'A', '81':'B', '82':'C', '83':'D', '84':'E', '85':'F', '86':'G', '87':'H', '88':'I', '89':'J', '8A':'K', '8B':'L', '8C':'M', '8D':'N', '8E':'O', '8F':'P', '90':'Q', '91':'R', '92':'S', '93':'T', '94':'U', '95':'V', '96':'W', '97':'X', '98':'Y', '99':'Z', '9A':'(', '9B':')', '9C':':', '9D':';', '9E':'[', '9F':']', 'A0':'a', 'A1':'b', 'A2':'c', 'A3':'d', 'A4':'e', 'A5':'f', 'A6':'g', 'A7':'h', 'A8':'i', 'A9':'j', 'AA':'k', 'AB':'l', 'AC':'m', 'AD':'n', 'AE':'o', 'AF':'p', 'B0':'q', 'B1':'r', 'B2':'s', 'B3':'t', 'B4':'u', 'B5':'v', 'B6':'w', 'B7':'x', 'B8':'y', 'B9':'z', 'BA':'é', 'E0':"'", 'E1':'PK', 'E2':'MN', 'E3':'-', 'E6':'?', 'E7':'!', 'E8':'.', 'EF':'♂', 'E4':',', 'E5':'♀', 'E6':'0', 'E7':'1', 'E8':'2', 'E9':'3', 'EA':'4', 'EB':'5', 'EC':'6', 'ED':'7', 'EE':'8', 'EF':'9'}
hex_map = {' ':'7F','A': '80', 'B': '81', 'C': '82', 'D': '83', 'E': '84', 'F': '85', 'G': '86', 'H': '87', 'I': '88', 'J': '89','K': '8A', 'L': '8B', 'M': '8C', 'N': '8D', 'O': '8E', 'P': '8F', 'Q': '90', 'R': '91', 'S': '92', 'T': '93','U': '94', 'V': '95', 'W': '96', 'X': '97', 'Y': '98', 'Z': '99', '(': '9A', ')': '9B', ':': '9C', ';': '9D','[': '9E', ']': '9F', 'a': 'A0', 'b': 'A1', 'c': 'A2', 'd': 'A3', 'e': 'A4', 'f': 'A5', 'g': 'A6', 'h': 'A7','i': 'A8', 'j': 'A9', 'k': 'AA', 'l': 'AB', 'm': 'AC', 'n': 'AD', 'o': 'AE', 'p': 'AF', 'q': 'B0', 'r': 'B1','s': 'B2', 't': 'B3', 'u': 'B4', 'v': 'B5', 'w': 'B6', 'x': 'B7', 'y': 'B8', 'z': 'B9', 'é': 'BA', "'": 'E0','PK': 'E1', 'MN': 'E2', '-': 'E3', ',': 'E4', '♀': 'E5', '9': 'E6', '!': 'E7', '.': 'E8', '3': 'E9', '4': 'EA','5': 'EB', '6': 'EC', '7': 'ED', '8': 'EE', '♂': 'EF'}

# decodes the pokemon character map to readable text
def decode_text(hex_input):
    if isinstance(hex_input, bytes):
        hex_string = hex_input.hex().upper()
    else:
        hex_string = hex_input.upper()
    hex_pairs = []
    for i in range(0, len(hex_string), 2):
        hex_pairs.append(hex_string[i:i+2])
    decoded_chars = []
    for pair in hex_pairs:
        if pair in char_map:
            decoded_chars.append(char_map[pair])
        else:
            decoded_chars.append('?')
    decoded_string = ''.join(decoded_chars)
    return decoded_string

# encodes readable text to the pokemon character map
def encode_text(string):
    encoded_hex = []
    for char in string:
        if char in hex_map:
            encoded_hex.append(hex_map[char])
        else:
            encoded_hex.append('??')
    encoded_string = ''.join(encoded_hex)
    byte_string = bytes.fromhex(encoded_string)

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

#gets the players name
def getPlayerName(savefile):
	f = open(savefile, 'rb')
	f.seek(0x2598)
	x = f.read(7)
	d = decode_text(x)
	return d

file = 'main.sav'
f = open(file, 'rb+')
f.seek(0,0)
ram = f.read()
x = open(f"{file}.bak",'wb')
x.write(ram)
x.close()
f.close()

name = getPlayerName(file)
print(name)
