def merge(lst1,lst2):
    lst_odd=[i for i in lst1 if i%2!=0]
    lst_even=[i for i in lst2 if i%2==0]
    m_lst=lst_odd+lst_even
    return m_lst
print("MERGE OF TWO LISTS")
num1=int(input("Enter number of elements in list 1:"))
lst1=[]
for i in range(num1):
    lst1.append(int(input("Enter element:")))
num2=int(input("Enter number of elements in list 2:"))
lst2=[]
for i in range(num2):
    lst2.append(int(input("Enter element:")))
merge_lst=merge(lst1,lst2)
print("The odd from list 1 and even from list 2 are ,")
print(merge_lst)
    
