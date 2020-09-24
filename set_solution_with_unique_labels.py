import os
import re
import sys
import io

def search_root_as_set(set_origin, set_destination):
    return set_origin.difference(set_destination)
    
def main():
    
    set_origin = set()
    set_destination = set()

    
    input_file = open('input_file.txt', 'r')
    sys.stdin = io.StringIO(input_file.read())
    for line in sys.stdin:
        row = line.rstrip().split(' ')
        children = list(map(int, row[2:]))
        parentId = int (row[0])

        set_origin |= set([parentId])
        set_origin |= set(children)
        set_destination |= set(children)
        
    
    print(search_root_as_set(set_origin, set_destination))
            



if __name__ == '__main__':
    main()

