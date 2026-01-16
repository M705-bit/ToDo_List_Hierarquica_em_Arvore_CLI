
from collections import deque
from enum import Enum

class Status(Enum):
    not_concluded = None
    in_progres = 1
    concluded = 2

class Node:
    def __init__(self, data, status=None):
        self.data = data
        self.status = Status(status).name
        self.children = []

    def add_child(self, child):
       self.children.append(child)

class Tree:
    def __init__(self, root_data,status=None):
        self.root=Node(root_data,status)

    def add_child(self, parent, child_data,status=None):
        child = Node(child_data,status)
        parent.children.append(child)
    def remove_child(self, parent,child_data):
        for child in parent.children:
            if child.data == child_data:
                for child1 in child.children:
                    child.children.remove(child1)
                parent.children.remove(child)
                return

    def levelOrder(self) -> list[list[int]]:
            levels_list = []
            if self.root is None:
                return levels_list 
            
            queue = deque([self.root])

            while queue:
                level_values = []

                for _ in range(len(queue)):
                    current_node = queue.popleft()
                    #node = self.search(current_node)
                    level_values.append(f"{current_node.data} -> {current_node.status}")
                    queue.extend(current_node.children)
                levels_list.append(level_values)
            
            return levels_list
    
    def search(self,data,current_node=None):
        if current_node is None:
            current_node = self.root
        if current_node.data == data:
            return current_node 
        
        for child in current_node.children:
            found_node = self.search(data, child)
            if found_node:
                return found_node 
        
    def return_percentage(self):
        
        def calculate_percentage (current_node):
                total=1
                concluded = 1 if current_node.status == 'concluded' else 0
                for child in current_node.children:
                    t,c = calculate_percentage(child)
                    concluded +=c
                    total+=t
                return total, concluded
        total,concluded= calculate_percentage(self.root)
        output = (concluded) / (total-1) * 100
        return output


