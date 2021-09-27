def oddrange(a,b):
    for i in range(a,b+1):
        if(i%2!=0):
            print(i,end='\t')
print("ODD NUMBERS BETWEEN A RANGE")
a=int(input("Enter starting range :"))
b=int(input("Enter ending range :"))
oddrange(a,b)



    
