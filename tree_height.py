# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    # Your code here
    tree = [[] for _ in range(n)]
    root = None

    for i, p in enumerate(parents):
        if p == -1:
            root = i
        else:
            tree[p].append(i)

    def search(node):
        nonlocal max_height
        height = 0
        for child in tree[node]:
            height = max(height, search(child))
        max_height = max(max_height, height + 1)
        return height + 1
    
    max_height = 0
    search(root)
    return max_height

def main():
    # implement input form keyboard and from files
    input_type = input("Enter input type - F or I:")
    
    if input_type == 'F':
        filename = input("Enter file name:")
        if 'a' in filename:
            print("Invalid file name")
            return
        try: 
            input_file = open("test/" + filename, "r")
            n = int(input_file.readline())
            parents = list(map(int, input_file.readline().split()))
            input_file.close()
        except:
            print("Error reading from file")
            return
        
    elif input_type == 'I':
        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input("Enter parents seperated by space: ").split()))
    else:
        print("Invalid input type")
        return

    print (compute_height(n, parents))

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()