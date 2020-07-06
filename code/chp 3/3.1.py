hrs = input("Enter Hours:")
h = float(hrs)
inte = input("Enter interest:")
i = float(inte)
if h>40 :
    pay=40*i+(h-40)*i*1.5
else :
    pay=h*i
print(pay)
        