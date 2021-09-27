from collections import OrderedDict
def addtask():
    name=input("Enter the Name :")
    num=int(input("Enter the number :"))
    dic[name]=num;
def deltask():
    del_task=input("Enter the Name to be deleted :")
    if del_task in dic:
        del dic[del_task]
    else:
        print("Enter correct Name")
def updatetask():
    old_name=input("Enter the old Name :")
    new_name=input("Enter the new Name :")
    new_num=input("Enter the new number :")
    if old_name in dic:
        del dic[old_name]
        dic[new_name]=new_num
    else:
        print("Enter correct Name")

def display():
    print()
    print("-"*50)
    print()
    print("CONTACT LIST.\n")
    dic1=OrderedDict(sorted(dic.items()))
    for i,j in dic1.items():
        print(i," number is ",j)
        print()
    print("-"*50)
        
dic={}
fns={1:addtask,2:deltask,3:updatetask,4:display}
while(True):
    s="\nPress 1 for adding contact \n 2 for deleting a contact \n 3 for updating old contact with new contact \n 4 for display the contacts :\n 5 for exit:"
    choice=int(input(s))
    if choice in fns:
        fns[choice]()
        if(choice!=4):
            display()
    elif choice==5:
        exit()
    else:
        print("Enter correct input..") 
