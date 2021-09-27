def addtask():
    task=input("Enter the task :").lower()
    print("Smaller the number, Higher the priority") #priority is unique
    priority=int(input("Enter the priority :"))
    dic[priority]=task;
def deltask():
    del_task=input("Enter the task to be deleted :").lower()
    if del_task in dic.values():
        for key, value in dic.items():
            if value == del_task:
                del dic[key]
                break
    else:
        print("Enter correct task")
def updatetask():
    old_task=input("Enter the old task :").lower()
    upd_task=input("Enter the new task to be updated:").lower()
    if old_task in dic.values():
        for key, value in dic.items():
            if value == old_task:
                k=key
                dic[k]=upd_task
                break
    else:
        print("Enter correct task")
def changepriority():
    a=int(input("Enter the old priority :"))
    b=int(input("Enter the new priority:"))
    if a in dic:
        key=dic.get(a)
        del dic[a]
        dic[b]=key
    else:
        print("Enter correct priority")
def display():
    print("The tasks are")
    dic1=dic.items()
    sorted_dic=sorted(dic1)
    for i in sorted_dic:
        for j in i:
            print(j,end=" ")
        print()
        
dic={}
fns={1:addtask,2:deltask,3:updatetask,4:changepriority,5:display}
while(True):
    print("\nPress 1 for adding task \n 2 for deleting a task \n 3 for updating old task with new task \n 4 for changing the priority of a task \n 5 for display the tasks :\n 6 for exit:")
    choice=int(input())
    if choice in fns:
        fns[choice]()
        if(choice!=5):
            display()
    elif choice==6:
        exit(0)
    else:
        print("Enter correct input..") 


  
