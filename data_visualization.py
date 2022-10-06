#@@ -1,194 +1,194 @@
import random
<<<<<<< HEAD
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
=======
import time as t
>>>>>>> 708adb373a6cc5b942f4aae733cac19518ee0c56

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


def time_bubble(sorted_list, reverse_list, random_list):
    length_measured = len(reverse_list, random_list, sorted_list)
    

    #record worst time for bubble sort
    t0 = t.perf_counter()
    bubble_sort(reverse_list)
    t1 = t.perf_counter()
    worst = t1-t0

    #record best time for bubble sort
    t0 = t.perf_counter()
    bubble_sort(sorted_list)
    t1 = t.perf_counter()
    best = t1-t0

    #record average time for bubble sort
    t0 = t.perf_counter()
    bubble_sort(random_list)
    t1 = t.perf_counter()
    avg = t1-t0

    return worst, best, avg, length_measured

def writeToFile(name, best, worst, avg, length_measured):
    f = open("Time Complexity Analysis.txt", "w") 
    f.write(name)
    f.write("\n\nLength of list: " + length_measured)
    f.write("\nBest time: " + best)
    f.write("\nWorst time: " + worst)
    f.write("\nAverage time: " + avg)
    f.close()

def addToFile(name, best, worst, avg, length_measured):
    f = open("Time Complexity Analysis.txt", "a")
    f.write(name)
    f.write("\n\nLength of list: " + length_measured)
    f.write("\nBest time: " + best)
    f.write("\nWorst time: " + worst)
    f.write("\nAverage time: " + avg)
    f.close()

def time_merge(sorted_list, reverse_list, random_list):
    length_measured = len(reverse_list, random_list, sorted_list)

     #record worst time for merge sort
    t0 = t.perf_counter()
    merge_sort(reverse_list)
    t1 = t.perf_counter()
    worst = t1-t0

    #record best time for merge sort
    t0 = t.perf_counter()
    merge_sort(sorted_list)
    t1 = t.perf_counter()
    best = t1-t0

    #record average time for merge sort
    t0 = t.perf_counter()
    merge_sort(random_list)
    t1 = t.perf_counter()
    avg = t1-t0


    return worst, best, avg, length_measured

def time_quick(sorted_list, reverse_list, random_list):
    length_measured = len(reverse_list, random_list, sorted_list)

<<<<<<< HEAD
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
=======
     #record worst time for quicksort
    t0 = t.perf_counter()
    quicksort(reverse_list)
    t1 = t.perf_counter()
    worst = t1-t0

    #record best time for quicksort
    t0 = t.perf_counter()
    quicksort(sorted_list)
    t1 = t.perf_counter()
    best = t1-t0

    #record average time for quicksort
    t0 = t.perf_counter()
    quicksort(random_list)
    t1 = t.perf_counter()
    avg = t1-t0


    return worst, best, avg, length_measured

def time_insertion(sorted_list, reverse_list, random_list):
    length_measured = len(reverse_list, random_list, sorted_list)

     #record worst time for insertion sort
    t0 = t.perf_counter()
    insertion_sort(reverse_list)
    t1 = t.perf_counter()
    worst = t1-t0

    #record best time for insertion sort
    t0 = t.perf_counter()
    insertion_sort(sorted_list)
    t1 = t.perf_counter()
    best = t1-t0

    #record average time for insertion sort
    t0 = t.perf_counter()
    insertion_sort(random_list)
    t1 = t.perf_counter()
    avg = t1-t0


    return worst, best, avg, length_measured

def __main__ (worst, best, avg, length_measured):

    #Produce our 3 lists for sorted list, reverse list, and random order list
    sorted, revers, ran = generate_lists(10)
    name = "Bubble Sort"
    writeToFile(name, length_measured(time_bubble), worst(time_bubble), best(time_bubble), avg(time_bubble))
    
    name = "Merge Sort"
    addToFile(name, length_measured(time_merge), worst(time_merge), best(time_merge),avg(time_merge))

    name = "Quicksort"
    addToFile(name, length_measured(time_quick), worst(time_quick), best(time_quick),avg(time_quick))

    name = "Insertion Sort"
    addToFile(name, length_measured(time_insertion), worst(time_insertion), best(time_insertion),avg(time_insertion))
>>>>>>> 708adb373a6cc5b942f4aae733cac19518ee0c56

    #visualize our bubble sort
    x = bubble_sort_visualized(ran)

    #Show that all of ours sorts are working properly
    print(bubble_sort(ran))
    print(merge_sort(ran))
    print(quicksort(ran))
    print(insertion_sort(ran))

<<<<<<< HEAD
#Call our main
__main__()
    


=======
    

    
#Call our main
#Call our main function
__main__()
    
>>>>>>> 708adb373a6cc5b942f4aae733cac19518ee0c56

