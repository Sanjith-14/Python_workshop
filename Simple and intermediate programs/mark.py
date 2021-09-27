def simple_interest(P,N,R):
    si=(P*N*R)/100
    return round(si,2)
print("SIMPLE INTEREST")
P=int(input("Enter Principle amount:"))
N=int(input("Enter number of years:"))
R=float(input("Enter rate of interest:"))
print("The simple interset for {} is {}".format(P,simple_interest(P,N,R)))


    
