expense=[]
while True:
    print("\n--- Expense Tracker ---\n")
    print("1.Add Expense.")
    print("2.View Expense.")
    print("3.View total spent.")
    print("4.Remove an expense.")
    print("5.Exit.")

    c=int(input("Enter your choice:-"))

    if c==1:
        amount=float(input("Enter Amount:-"))
        desc=input("Enter description: ")
        expense.append((amount,desc))
        print("Expense added!")

    elif c==2:
        if not expense:
                print("No expenses yet.")
        else:
            for i,(amount,desc) in enumerate(expense,start=1):
                print(f"{i}. {desc}->₹{amount}")
    elif c == 3:
        total = sum(amount for amount, _ in expense)
        print(f"Total expense: ₹{total}")

    elif c == 4: 
        num = int(input("Enter expense number to remove: "))
        if 1 <= num <= len(expense):
            removed = expense.pop(num - 1)
            print(f"Removed: {removed[1]} - ₹{removed[0]}")
        else:
            print("Invalid number.")

    elif c == 5:
        print("Exiting...")
        break
    
    else:
        print("Invalid choice.")
