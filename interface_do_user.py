from ToDo import Status,Node,Tree

tree=Tree(input("Add the name of the project: "))
sub_tasks = []

def add_task():
    print("Add tasks and substasks")
    found_node = None
    while found_node is None:
        parent_task = input("Add the name of the task to which the subtasks will be part of: ")
        found_node = tree.search(parent_task)
        if found_node is None:
            print(f"Could not find '{parent_task}'. Try again.")

    sub_tasks= list(input("Add the subtasks separated by comma: ").split(","))
    i=0
    for sub in sub_tasks:
        tree.add_child(found_node, sub)

while True:
    
    output=input("\n What do you want to do? \n Type '1' to add tasks; \n Type '2' to change the status of the task; \n Type '3' to end loop; \n Type here:  ")
    match output:
        case '1': 
            add_task()
        case '2': 
            try:
                node = tree.search(input("\n Specify the task: "))
                if node is None:
                    raise AttributeError
            except AttributeError:
    
                #avisa o erro
                print("Task not found. Please try again.")
                continue
            node.status=Status((int(input("\n Type \n '1' to have status equal to 'in progress' \n Type '2' to have status equal to 'concluded' \n Type here: ")))).name
        case '3': 
            break
    
print("\n To do list:")
list_of_tasks = []
list_of_tasks = tree.levelOrder()
for level in list_of_tasks:
    print(level)
print(f" The progress of the project is in {tree.return_percentage()}%")