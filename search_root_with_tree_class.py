import os
import re
import sys
import io

class TreeNode:
    def __init__(self, value):
        self.parent = None
        self.val = value

    def set_parent(self, node):
        self.parent = node

    def search_root(self):
        current = self
        # the root is a node with no parents
        while current.parent != None:
            current = current.parent
        return current
    
    def print_node_val(self):
        print(self.val)
        

def main(filename):
    nodes_dict = {}

    ## comment out below to read specific string as file
    #string ='1 -> 1'
    #with io.StringIO(string) as input_file:

    with open(filename, 'r') as input_file:
        sys.stdin = io.StringIO(input_file.read())
        """1 ->1"""
        node = None
        for line in sys.stdin:
            # parse input format 'parent -> child1 child2 child3 ...'
            row = line.rstrip().split(' ')
            children = list(map(int, row[2:]))
            try: 
                parentId = int(row[0])
            except:
                raise Exception('The file input format {} is incorrect'.format(filename))
            if parentId in nodes_dict.keys():
                node = nodes_dict[parentId]
            else:
                node = TreeNode(parentId)
                nodes_dict[parentId] = node

            for childId in children:
                if childId in nodes_dict.keys():
                    child = nodes_dict[childId]
                else:
                    child = TreeNode(childId)
                    nodes_dict[childId] = child
                child.set_parent(node)


    if node:
        answer = node.search_root()
        answer.print_node_val()
        return answer.val
    else:
        raise Exception('The file {} was empty'.format(filename))


if __name__ == '__main__':
    input_filename = 'input_file.txt'
    main(input_filename)