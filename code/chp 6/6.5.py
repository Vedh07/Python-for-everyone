str = "X-DSPAM-Confidence:    0.8475";
pt=str.find('.')
piece=str[pt-1:]
ptr=float(piece)
print(ptr)