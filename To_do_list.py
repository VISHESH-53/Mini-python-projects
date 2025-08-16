l=[]
while True:
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Remove Task")
    print("4.Exit")

    c=int(input("\nEnter your choice:-\n"))

    if c==1:
        task=input("Enter Task:-\n")
        l.append(task)
    elif c == 2:
        if not l:
            print("No tasks yet.")
        else:
            for i, task in enumerate(l, start=1):
                print(f"{i}. {task}\n")

    elif c == 3:
        if not l:
            print("No tasks to remove.")
        else:
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(l):
                removed = l.pop(num - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")

    elif c==4:
        print("\nExiting.....")
        break
    else:
        print("\nInvalid input.")
    
