import sys

with open(sys.argv[1], "rb") as f:
    data = f.read(188)  # just read the first 188 bytes
    first_byte = ord(data[0])
    if first_byte != 0x47:
        print("Could not find sync byte. Not a valid transport stream file")
    else:
        print("Found sync byte")
