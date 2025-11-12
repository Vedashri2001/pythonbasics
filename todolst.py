todo=[]
complete=[]
num=0
while True:
    for i in range(len(todo)):
        print(f"{i+1}.{todo[i]}")
    print("*" * 20)
    print("Enter a command,h for help")
    command=input(">")
    if command=="q":
        break
    elif command=="h":
        print("enter task to add")
        print("enter q to quit")
    elif command.isnumeric():
        idx = int(command)-1
        if idx >=len(todo):
            print("invalid")
        else:
            done=todo.pop(idx)
            complete.append(done)
    else:
        todo.append(command)
if complete:
    print(f"completed {len(complete)} task")
    for todos in complete:
        print(f"* {todos}")
    else:
        print("no work")