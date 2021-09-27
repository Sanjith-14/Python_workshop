def min(a,b):
    min=a if a<b else b
    return min
print("Minimum of two numbers")
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
print("The minimum of {} and {} is {}".format(a,b,min(a,b)))
