def computepay(h,r):
    if h>40 :
        pay=40*r+(h-40)*r*1.5
    else :
        pay=h*r
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
hr = float(hrs)    
ra = float(rate)
p = computepay(hr, ra)
print("Pay",p)