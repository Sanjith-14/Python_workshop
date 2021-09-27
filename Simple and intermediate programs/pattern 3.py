rows=int(input("Enter number of rows :"))
print("The pattern is ,\n")
for i in range(1,rows+1):
    for j in range(0,rows-i):
        print(" ",end='')
    for k in range(i):
        print("* ",end='')
    print()


  
