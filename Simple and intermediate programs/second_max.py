def maximum(lst):
    lst1=lst
    lst1.remove(max(lst1))
    return max(lst1)
print("SECOND LARGEST ELEMENT IN LIST")
num=int(input("Enter number of elements in list:"))
lst=[]
for i in range(num):
    lst.append(int(input("Enter element:")))
print("The list is")
print(lst)
print("The second largest element in the list is ",maximum(lst))
  
