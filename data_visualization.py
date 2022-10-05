import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import scipy as sp

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
        
    return myList
plt.show() 
#------------BUBBLE SORT------------


#------------MERGE SORT------------
def merge_sort_visualized(list):

    x = np.arange(0, len(list), 1)
    wait_time = .000001

    plt.bar(x, list, align="edge", width=0.8) #creates a bar for each element in myList
    plt.pause(wait_time) #pause to allow the bars to be seen
    plt.clf() #clear frame

    #if list empty then return it 
    if len(list) <= 1:
        return list

    #split the left and the right half further
    left_half, right_half = split(list)

    #sort the left half
    left = merge_sort_visualized(left_half)

    #sort the right half
    right = merge_sort_visualized(right_half)

    #return the merged lists
    return merge(left, right, list)

def split(list):

    #get our midpoint
    mid = len(list) // 2

    #left list = everything left of midpoint
    left = list[:mid]

    #right list = everything right of midpoint
    right = list[mid:]

    #return our lists
    return left, right

def merge(left, right, list):
    
    #empty list and indexes
    l = []
    i = 0
    j = 0

    x = np.arange(0, len(list), 1)
    wait_time = .000001

    #Sort our sublists 
    #while index i not greater than the left list and vice versa with right list
    while i < len(left) and j < len(right):

        plt.bar(x, list, align="edge", width=0.8) #creates a bar for each element in myList
        plt.pause(wait_time) #pause to allow the bars to be seen
        plt.clf() #clear frame

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

        plt.bar(x, list, align="edge", width=0.8) #creates a bar for each element in myList
        plt.pause(wait_time) #pause to allow the bars to be seen
        plt.clf() #clear frame

        l.append(left[i])
        i += 1
    #while j is less than the len of our right list append the value at index j to list l
    while j < len(right):

        plt.bar(x, list, align="edge", width=0.8) #creates a bar for each element in myList
        plt.pause(wait_time) #pause to allow the bars to be seen
        plt.clf() #clear frame

        l.append(right[j])
        j += 1

    #return our merged list
    return l
#------------MERGE SORT------------

#------------INSERTION SORT------------
#Beginning instertion_sort_visualized
def insertion_sort_visualized(myList):

    x = np.arange(0, len(myList), 1)
    wait_time = .000001

    i = 1
    while(i < len(myList)):
        j = i
        while((j > 0) and (myList[j - 1] > myList[j])):
            #showing visualization
            plt.bar(x, myList, align="edge", width=0.8) #creates a bar for each element in myList
            plt.pause(wait_time) #pause to allow the bars to be seen
            plt.clf() #clear frame

            temp = myList[j - 1]
            myList[j - 1] = myList[j]
            myList[j] = temp
            j -= 1
        i += 1
    return myList
plt.show()
#------------INSERTION SORT------------

#------------QUICK SORT------------
def quick_sort_visualized(values):

    x = np.arange(0, len(values), 1)
    wait_time = .000001

    plt.bar(x, values, align="edge", width=0.8) #creates a bar for each element in myList
    plt.pause(wait_time) #pause to allow the bars to be seen
    #plt.clf() #clear frame
    #plt.show()
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
    plt.clf() #clear frame
    plt.show()
    return quick_sort_visualized(less_than_pivot) + [pivot] + quick_sort_visualized(greater_than_pivot)


def __main__ ():
    sorted, reverse, ran = generate_lists(10)

    #bubble_sort_visualized(ran)
    #insertion_sort_visualized(ran)
    merge_sort_visualized(ran)
    #quick_sort_visualized(ran)
    
    

    return



__main__()



