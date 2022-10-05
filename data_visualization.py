import random
from turtle import color
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import time

#------------IMPORTANT------------#
#matplotlib, numpy and scipy must be installed to successfully compile this program
#if you are using anaconda:
#conda install matplotlib
#conda install numpy

#if you are using pip:
#pip install matplotlib
#pip install numpy

#it is best practice to use a virtual environment rather than intall in the base environment

#-----------GENERATING LIST TO BE USED AS INPUTS-----------
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

#------------BUBBLE SORT------------
#bubble_sort is used for timing the algorithm
def bubble_sort(myList):
    for i in range(len(myList)-1):
        for j in range(len(myList)-i-1):
            if myList[j] > myList[j + 1]: #if the current value is greater than the next
                myList[j], myList[j+1] = \
                    myList[j + 1], myList[j] #swap them
    return myList

#bubble_sort_visualized shows the visualization of the sorting algorithm
def bubble_sort_visualized(myList):

    x = np.arange(0, len(myList), 1)
    wait_time = .000001

    for i in range(len(myList)-1):
        for j in range(len(myList)-i-1):

            plt.bar(x, myList, align="edge", width=0.8) #creates a bar for each element in myList
            plt.pause(wait_time) #pause to allow the bars to be seen
            plt.clf() #clear frame

            if myList[j] > myList[j + 1]: #if the current value is greater than the next
                myList[j], myList[j+1] = \
                    myList[j + 1], myList[j] #swap them
            
    time.sleep(1)
    return myList
#------------BUBBLE SORT------------


#------------MERGE SORT------------
def merge_sort_visualized(arr):

    x = np.arange(0, len(arr), 1)
    wait_time = .000001

    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    # plt.bar(x, arr, align="edge", width=0.8) #creates a bar for each element in myList
    # plt.pause(wait_time) #pause to allow the bars to be seen
    # plt.clf() #clear frame

    # Perform merge_sort recursively on both halves
    left, right = merge_sort_visualized(arr[:mid]), merge_sort_visualized(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())


def merge(left, right, merged):

    x = np.arange(0, len(merged), 1)
    wait_time = .000001

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
      
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    plt.bar(x, merged, align="edge", width=0.8) #creates a bar for each element in myList
    plt.pause(wait_time) #pause to allow the bars to be seen
    plt.clf() #clear frame

    return merged
plt.show()
#------------MERGE SORT------------

#------------INSERTION SORT------------
#Beginning instertion_sort_visualized
def insertion_sort_visualized(arr):

    x = np.arange(0, len(arr), 1)
    wait_time = .000001
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > cursor:

            #showing visualization
            plt.bar(x, arr, align="edge", width=0.8) #creates a bar for each element in myList
            plt.pause(wait_time) #pause to allow the bars to be seen
            plt.clf() #clear frame

            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor
    return arr
#------------INSERTION SORT------------

#------------QUICK SORT------------
def partition(array, begin, end):
    pivot_idx = begin
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    
    return quick_sort_recursion(array, begin, end)


def __main__ ():
    sorted, reverse, ran = generate_lists(30)

    #bubble_sort_visualized(ran)
    #insertion_sort_visualized(ran)
    #merge_sort_visualized(ran)
    #quick_sort_visualized(ran)
    
    

    return



__main__()



