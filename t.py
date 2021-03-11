
import sys

def string_to_bytes(s):
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c != '\\':
            out.append(ord(c))
            i = i + 1
        else:
            hex_str = s[i+2:i+4]
            i = i + 4
            out.append(int(hex_str, 16))
    b = bytearray(out)
    return b
###
s = "abc ∑" # utf-8 string with ascii and unicode characters
se = s.encode('utf-8') # encode it to bytes 
print(s, se) # print them both out
####
s = "abc \\xe2\\x88\\x91" # ascii string with bytes encoded as ascii characters
by = string_to_bytes(s) # convert string to bytes
print(by, by.decode("utf-8")) # decode bytes back into utf-8 string

