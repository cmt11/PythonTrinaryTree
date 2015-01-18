"""
This program implements a "trinary" search tree (where each node has up to 2 data values and 3 branches) and performs several operations on it.

Author: Chris Thomas
"""



def printTree(tree, indent=0):
    """
    Prints an indented representation of a trinary tree.  The second
    parameter determines how far the tree is to be indented from the
    left margin.  This representation looks like a drawing of a tree
    without the connecting lines if you tilt your head to the left.
    """
    if tree == None:
        return # don't print anything
    elif tree['data2'] == None: # one data element, no children
        print " "*indent + str(tree['data1'])
    else: # two data elements, may have up to three children
        printTree(tree['right'],indent+4)
        print " "*indent + str(tree['data2'])
        printTree(tree['middle'],indent+4)
        print " "*indent + str(tree['data1'])
        printTree(tree['left'],indent+4)
        


def add(tree, newValue):
    """
    Adds newValue to tree and returns a pointer to the root of the
    modified tree.  If newValue is already in the tree, doesn't change
    the tree (but this is not an error).
    """
    if search(tree, newValue) == True: # if newValue is already in the tree, do not change the tree
        return tree
    if tree == None: # if the tree is empty, create the first node
        newNode = {'data1': newValue, 'data2': None, 'left': None, 'middle': None, 'right': None}
        return newNode  # return the new tree
    if newValue < tree['data1']:  # newValue is less than the current value in data1
        if tree['data2'] == None: # there is no data2 value
            tree['data2'] = tree['data1']
            tree['data1'] = newValue
            return tree # return the modified tree
        else: # tree['data2'] != None
            tree['left'] = add(tree['left'], newValue) # add newValue to the left "branch" of the tree
            return tree # return the modified tree
    else: # newValue > tree['data1']
        if tree['data2'] == None: # there is no data2 value
            tree['data2'] = newValue
            return tree # return the modified tree
        elif newValue < tree['data2']: # newValue is greater than data1 but less than data2
            tree['middle'] = add(tree['middle'], newValue) # add newValue to the middle "branch" of the tree
            return tree # return the modified tree
        else: # newValue > tree['data2']
            tree['right'] = add(tree['right'], newValue) # add newValue to the right "branch" of the tree
            return tree # return the modified tree
            


def treeFromList(values):
    """
    Parameter must be a Python lists of values.  Returns a tree
    created by adding each value from the list to the tree, in order.
    """
    tree = None
    for v in values:
        tree = add(tree,v)
    return tree



import random
def randomTree(numNodes):
    """
    Creates a tree with the specified number of nodes using random numbers.
    A helper to generate trees for testing.  The tree may actually have fewer
    nodes than the requested number if randInt happens to come up with
    duplicates of the same number.
    """
    tree = None
    for i in range(numNodes):
        tree = add(tree, random.randint(1,100))
    return tree
    


def search(tree,value):
    """
    Searches a tree for a value.  Returns True if value occurs somewhere
    inside tree, False otherwise.
    """
    if tree == None: # if the tree is empty, return False
        return False
    if tree['data1'] == value or tree['data2'] == value: # if the target is one of the data values of the current node, return True
        return True
    if tree['data1'] > value: # the target is less than data1
        return search(tree['left'], value) # search the left "branch" of the tree
    else: # tree['data1'] < value
        if tree['data2'] > value: # the target is greater than data1, but less than data2
            return search(tree['middle'], value) # search the middle "branch" of the tree
        else: # tree['data2'] < value
            return search(tree['right'], value) # search the right "branch" of the tree
        


def total(tree):
    """
    Returns the total of all the numbers in a tree.  If the tree is empty,
    the total is zero.
    """
    if tree == None: # if the tree is empty, the total is zero
        return 0
    if tree['data1'] != None: # there is a data1 value
        if tree['data2'] != None: # there is a data2 value
            return tree['data1'] + tree['data2'] + total(tree['left']) + total(tree['middle']) + total(tree['right'])
        else: # data2 == None
            return tree['data1'] + total(tree['left']) + total(tree['middle']) + total(tree['right'])                                                         
    else: # data1 == None
        if tree['data2'] != None: # there is a data2 value
            return tree['data2'] + total(tree['left']) + total(tree['middle']) + total(tree['right'])
        else: # data2 == None
            return 0

            

def height(tree):
    """
    Returns the height of the tree -- the length of the longest path from
    the root to a leaf.
    """
    if tree == None: # if the tree is empty, the height is zero
        return 0
    else:
        leftHeight = height(tree['left'])     # the height of the left "branch" of the tree
        middleHeight = height(tree['middle']) # the height of the middle "branch" of the tree
        rightHeight = height(tree['right'])   # the height of the right "branch" of the tree
        return max(leftHeight, middleHeight, rightHeight) + 1 # return the longest "branch" (which is the height of the tree)



def findMin(tree):
    """
    Returns the smallest value in the tree, or None if the tree is empty.
    """
    if tree == None: # if the tree is empty, return None
        return None
    elif tree['left'] == None: # there is no left "branch"
        return tree['data1']   # return data1, the lowest value in the tree
    else: # tree['left'] != None
        return findMin(tree['left']) # find the lowest value in the left "branch" of the tree
    


def deleteMin(tree):
    """
    Deletes the smallest value in the tree and returns the modified tree.
    No effect if the tree is empty.
    """
    if tree == None: # if the tree is empty, return None
        return None
    if tree['left'] == None: # the tree has no left "branch"
        if tree['data2'] == None: # if there is no data2 value, return None
            return None
        if tree['middle'] != None: # the tree has a middle "branch"
            tree['data1'] = findMin(tree['middle'])
            tree['middle'] = deleteMin(tree['middle'])
        elif tree['right'] != None: # the tree has no middle "branch", but does have a right "branch"
            tree['data1'] = tree['data2']
            tree['data2'] = findMin(tree['right'])
            tree['right'] = deleteMin(tree['right'])
        else: # the tree has no middle "branch" or right "branch"
            tree['data1'] = tree['data2']
            tree['data2'] = None
        return tree # return the modified tree
    else: # tree['left'] != None
        tree['left'] = deleteMin(tree['left'])
        return tree # return the modified tree



def treeToList(tree):
    """
    Returns a list of all the values in the tree, in ascending order.
    Empty list if the tree is empty.
    """
    nums = []
    if tree == None: # if the tree is empty, return an empty list
        return []
    temp = treeToList(tree['left']) # create a temporary list of values in the left "branch"
    if temp != None: # the list is not None
        for number in temp: # add the values in temp to the list
            nums.append(number)
    if tree['data1'] != None: # if data1 is not None, add it to the list
        nums.append(tree['data1'])
    temp = treeToList(tree['middle']) # create a temporary list of values in the middle "branch"
    if temp != None: # the list is not None
        for number in temp: # add the values in temp to the list
            nums.append(number)
    if tree['data2'] != None: # if data2 is not None, add it to the list
        nums.append(tree['data2'])
    temp = treeToList(tree['right']) # create a temporary list of values in the right "branch"
    if temp != None: # the list is not None
        for number in temp: # add the values in temp to the list
            nums.append(number)
    return nums # return the list of numbers in the tree



def delete(tree, value):
    """
    Deletes a given value in the tree and returns the modified tree.
    No effect if the tree is empty.
    NOTE: The structure of the tree may be slightly altered by this function, as I couldn't quite perfect it by hand-in time.
    """
    nums = treeToListUnsorted(tree) # create a list of numbers in the tree
    nums.remove(value) # remove the desired value from the list
    tree = treeFromList(nums) # re-create the tree from the modified list of numbers
    return tree # return the modified tree



def treeToListUnsorted(tree):
    """
    Returns a list of all the values in the tree, in an order so as to preserve the structure of the original tree even if the list is modified.
    """
    nums = []
    temp = tree
    if temp == None: # if the tree is empty, return an empty list
        return []
    if temp['data1'] != None: # if data1 is not None, add it to the list
        nums.append(temp['data1'])
    if temp['data2'] != None:  # if data2 is not None, add it to the list
        nums.append(temp['data2'])
    if temp['left'] != None: # the tree has a left "branch"
        tempList = treeToListUnsorted(temp['left']) # create a temporary list of values in the left "branch"
        for value in tempList: # add the values in tempList to the list
            nums.append(value)
    if temp['middle'] != None: # the tree has a middle "branch"
        tempList = treeToListUnsorted(temp['middle']) # create a temporary list of values in the middle "branch"
        for value in tempList: # add the values in tempList to the list
            nums.append(value)
    if temp['right'] != None: # the tree has a right "branch"
        tempList = treeToListUnsorted(temp['right']) # create a temporary list of values in the right "branch"
        for value in tempList: # add the values in tempList to the list
            nums.append(value)
    return nums # return the list of numbers in the tree
        
    
