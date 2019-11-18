with open("3d1106a4-5c2a-4909-8d3a-1088b1ecc7db_ts_avc_hd_1571294026137.ts", "rb") as f:
    data = f.read(188)  # just read the first 188 bytes
    first_byte = data[0]
    if first_byte == 0x47:
        print("Found sync byte")
    else:
        print("Could not find sync byte. Not a valid transport stream file")
