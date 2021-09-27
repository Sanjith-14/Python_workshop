rows=int(input("Enter number of rows :"))
print("The pattern is ,\n")
for i in range(0,rows):
    if(i%5==0):
        for j in range(0,rows):
            if(j%5==0):
                print('+',end=' ')
            else:
                print("-",end=' ')
        print()
    else:
        for j in range(0,rows):
            if(j%5==0):
                print('|',end=' ')
            else:
                print(" ",end=' ')
        print()
  
