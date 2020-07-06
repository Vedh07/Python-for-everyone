# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
x=0
rh=0
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
        r=line[19:]
        rh=rh + float(r)
        x=x+1
ra=rh/x    
print("Average spam confidence:",ra)
