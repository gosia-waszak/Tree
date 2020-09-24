import os
import re
import sys
import io

""" example input (with leafs also provided):
2 -> 7 5
7 -> 10
5 ->
10 -> 
"""

def main():
    with open('xor_input_file_with_leafs.txt', 'r') as input_file:
        sys.stdin = io.StringIO(input_file.read())
        total = 0
        for line in sys.stdin:
            row = line.rstrip().split(' ')
            children = list(map(int, row[2:]))
            parentId = int (row[0])
            total ^= parentId
            for item in children:
                total ^= item
    
    print(total)

if __name__ == '__main__':
    main()


