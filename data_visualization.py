import random
#import matplotlib.pyplot as plt
#import numpy as np

#------------IMPORTANT------------#
#matplotlib and numpy must be installed to successfully compile this program
#if you are using anaconda:
#conda install matplotlib
#conda install numpy

#if you are using pip:
#pip install matplotlib
#pip install numpy

#it is best practice to use an environment rather than intall in the base env

def generate_lists(n):
    
    sorted_list = []
    random_list = []
    for i in range(n):
        sorted_list.append(i + 1)
        random_list.append(i + 1)
    
    reversed_list = []
    for i in reversed(sorted_list):
        reversed_list.append(i) 

    random.shuffle(random_list)

    return sorted_list, reversed_list, random_list

#IT'S RECOMMENDED TO USE SMALL LISTS AS INPUT
def bubble_sort_visualized(myList):
    x = np.arange(0, len(myList), 1)
    wait_time = .000001
    for i in range(len(myList)-1):
        for j in range(len(myList)-i-1):
            plt.bar(x, myList) #creates a bar for each element in myList
            plt.pause(wait_time) #pause to allow the bars to be seen
            plt.clf() #clear frame
            if myList[j] > myList[j + 1]: #if the current value is greater than the next
                myList[j], myList[j+1] = \
                    myList[j + 1], myList[j] #swap them
    return myList
    plt.show()
    

def bubble_sort(myList):
    for i in range(len(myList)-1):
        for j in range(len(myList)-i-1):
            if myList[j] > myList[j + 1]: #if the current value is greater than the next
                myList[j], myList[j+1] = \
                    myList[j + 1], myList[j] #swap them
    return myList

def merge_sort(list):

    #if list empty then return it 
    if len(list) <= 1:
        return list

    #split the left and the right half further
    left_half, right_half = split(list)

    #sort the left half
    left = merge_sort(left_half)

    #sort the right half
    right = merge_sort(right_half)

    #return the merged lists
    return merge(left, right)

def split(list):

    #get our midpoint
    mid = len(list) // 2

    #left list = everything left of midpoint
    left = list[:mid]

    #right list = everything right of midpoint
    right = list[mid:]

    #return our lists
    return left, right

def merge(left, right):
    
    #empty list and indexes
    l = []
    i = 0
    j = 0

    #Sort our sublists 
    #while index i not greater than the left list and vice versa with right list
    while i < len(left) and j < len(right):
        
        #if left value is less than right then append the value to our temp list l and increment i
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        
        #else then append our right value to our temp list value l
        else:
            l.append(right[j])
            j += 1

    #while i is less than the len of our left list append the value at index i to list l
    while i < len(left):
        l.append(left[i])
        i += 1
    #while j is less than the len of our right list append the value at index j to list l
    while j < len(right):
        l.append(right[j])
        j += 1

    #return our merged list
    return l

def merge_sort_visualized():
    #implement visualization of merge sort
    return

def quicksort(values):
    
    #if the list is empty return it
    if len(values) <= 1:
        return values

    less_than_pivot = []
    greater_than_pivot = []

    # Next we need to choose the pivot value. For now, we just grab the first item from the list.
    pivot = values[0]

    # Then we loop through all the items in the list following the pivot.
    for value in values[1:]:
        # We check to see whether the current value is less than or equal to the pivot.
        if value <= pivot:
        # If it is, we copy it to the sub-list of values less than the pivot.
            less_than_pivot.append(value)
        # Otherwise, the current value must be greater than the pivot
        else:
        # So we copy it to the other list.
            greater_than_pivot.append(value)
    #We call quicksort recursively on the sub-list that's less than the pivot. 
    #We do the same for the sub-list that's greater than the pivot. 
    #Merge our lists and our pivot and return
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
def quick_sort_visualized():
    #implement visualization of quick sort
    return

def insertion_sort(list): 
   
    # Outer loop to traverse the list 
    for i in range(1, len(list)): 
        #value of a is the value at the current index
        a = list[i] 
        # Move elements of list1[0 to i-1] which are greater to one position ahead of their current position 
        j = i - 1 
        #while j is greater than 0 and a is less than the current value at index j swap the values and dec j
        while j >= 0 and a < list[j]: 
            list[j + 1] = list[j] 
            j -= 1 
        #the next index is equal to the value of a whichi is at index i
        list[j + 1] = a 
    #return our list
    return list

def insertion_sort_visualized():
    return

def __main__ ():

    #Produce our 3 lists for sorted list, reverse list, and random order list
    sorted, revers, ran = generate_lists(10)

    #visualize our bubble sort
    x = bubble_sort_visualized(ran)

    #Show that all of ours sorts are working properly
    print(bubble_sort(ran))
    print(merge_sort(ran))
    print(quicksort(ran))
    print(insertion_sort(ran))

#Call our main
__main__()
    



