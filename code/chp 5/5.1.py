largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        numb = int(num)
        smallest =numb
    except:
        print('Invalid input')
        continue
    else :
        
        if numb<smallest :
            smallest = numb
        elif numb>largest :
            largest = numb
        

print("Maximum is",largest)
print("Minimum is",smallest)