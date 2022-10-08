import random
import time as t
import matplotlib.pyplot as plt
import numpy as np
import time

#----------IMPORTANT----------
#To run this, you must have matplotlib and numpy installed
#As well as have Python 3.10 or greater
#
#
#Dakota Varnell, Jorge Chavez, Nick Adney
#CSCI 3330 Algorithms
#10/09/22

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

#BEGINNING VISUALIZATION FUNCTINONS
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
plt.show()
#------------BUBBLE SORT------------#

#------------INSERTION SORT------------

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

#------------Quick Sort------------

def partition(array,low,high):
    i = ( low - 1 )
    x = array[high]
 
    for j in range(low , high):
        if   array[j] <= x:
 
            i = i+1
            array[i],array[j] = array[j],array[i]
 
    array[i+1],array[high] = array[high],array[i+1]
    return (i+1)


# low  --> Starting index,
# high  --> Ending index
def quicksort_visualized(array,low,high):

    x = np.arange(0, len(array), 1)
    wait_time = .000001
 
    #  auxiliary stack
    size = high - low + 1
    stack = [0] * (size)
 
    top = -1
 
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
 
    # Keep popping from stack while is not empty
    while top >= 0:
        
        #showing visualization
        plt.bar(x, array, align="edge", width=0.8) #creates a bar for each element in myList
        plt.pause(wait_time) #pause to allow the bars to be seen
        plt.clf() #clear frame


        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
 
        # sorted array
        p = partition( array, low, high )
        
        # push left side to stack
        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        #  push right side to stack
        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high
    return array
#------------Quick Sort------------#
#ENDING VISUALIZATION FUNCTINONS
    
# def bubble_sort(myList):
#     for i in range(len(myList)-1):
#         for j in range(len(myList)-i-1):
#             if myList[j] > myList[j + 1]: #if the current value is greater than the next
#                 myList[j], myList[j+1] = \
#                     myList[j + 1], myList[j] #swap them
#     return myList

# def merge_sort(list):
#     #if list empty then return it 
#     if len(list) <= 1:
#         return list
#     #split the left and the right half further
#     left_half, right_half = split(list)
#     #sort the left half
#     left = merge_sort(left_half)
#     #sort the right half
#     right = merge_sort(right_half)
#     #return the merged lists
#     return merge(left, right)

# def split(list):
#     #get our midpoint
#     mid = len(list) // 2
#     #left list = everything left of midpoint
#     left = list[:mid]
#     #right list = everything right of midpoint
#     right = list[mid:]
#     #return our lists
#     return left, right

# def merge(left, right):
    
#     #empty list and indexes
#     l = []
#     i = 0
#     j = 0
#     #Sort our sublists 
#     #while index i not greater than the left list and vice versa with right list
#     while i < len(left) and j < len(right):
        
#         #if left value is less than right then append the value to our temp list l and increment i
#         if left[i] < right[j]:
#             l.append(left[i])
#             i += 1
        
#         #else then append our right value to our temp list value l
#         else:
#             l.append(right[j])
#             j += 1
#     #while i is less than the len of our left list append the value at index i to list l
#     while i < len(left):
#         l.append(left[i])
#         i += 1
#     #while j is less than the len of our right list append the value at index j to list l
#     while j < len(right):
#         l.append(right[j])
#         j += 1
#     #return our merged list
#     return l

# def partition(array,low,high):
#     i = ( low - 1 )
#     x = array[high]
 
#     for j in range(low , high):
#         if   array[j] <= x:
 
#             i = i+1
#             array[i],array[j] = array[j],array[i]
 
#     array[i+1],array[high] = array[high],array[i+1]
#     return (i+1)
 
# # low  --> Starting index,
# # high  --> Ending index
# def quicksort(array,low,high):
 
#     #  auxiliary stack
#     size = high - low + 1
#     stack = [0] * (size)
 
#     top = -1
 
#     top = top + 1
#     stack[top] = low
#     top = top + 1
#     stack[top] = high
 
#     # Keep popping from stack while is not empty
#     while top >= 0:
 
#         # Pop high and low
#         high = stack[top]
#         top = top - 1
#         low = stack[top]
#         top = top - 1
 
#         # sorted array
#         p = partition( array, low, high )

#         # push left side to stack
#         if p-1 > low:
#             top = top + 1
#             stack[top] = low
#             top = top + 1
#             stack[top] = p - 1

#         #  push right side to stack
#         if p+1 < high:
#             top = top + 1
#             stack[top] = p + 1
#             top = top + 1
#             stack[top] = high
#     return array
 

# def insertion_sort(list): 
   
#     # Outer loop to traverse the list 
#     for i in range(1, len(list)): 
#         #value of a is the value at the current index
#         a = list[i] 
#         # Move elements of list1[0 to i-1] which are greater to one position ahead of their current position 
#         j = i - 1 
#         #while j is greater than 0 and a is less than the current value at index j swap the values and dec j
#         while j >= 0 and a < list[j]: 
#             list[j + 1] = list[j] 
#             j -= 1 
#         #the next index is equal to the value of a whichi is at index i
#         list[j + 1] = a 
#     #return our list
#     return list

# def time_bubble(sorted_list, reverse_list, random_list):
    
#     length_measured = len(reverse_list)
    
#     #record worst time for bubble sort
#     t0 = t.perf_counter()
#     bubble_sort(reverse_list)
#     t1 = t.perf_counter()
#     worst = t1-t0

#     #record best time for bubble sort
#     t0 = t.perf_counter()
#     bubble_sort(sorted_list)
#     t1 = t.perf_counter()
#     best = t1-t0

#     #record average time for bubble sort
#     t0 = t.perf_counter()
#     bubble_sort(random_list)
#     t1 = t.perf_counter()
#     avg = t1-t0

#     return worst, best, avg, length_measured

# def writeToFile(name, best, worst, avg, length_measured):

#     best = round(best, 3)
#     worst = round(worst, 3)
#     avg = round(avg, 3)

#     f = open("Time Complexity Analysis.txt", "a") 
#     f.write("\n" + name)
#     f.write("\nLength of list: " + str(length_measured))
#     f.write("\nBest time: " + str(best))
#     f.write("\nWorst time: " + str(worst))
#     f.write("\nAverage time: " + str(avg) + "\n")
#     f.close()

# def addToFile(name, best, worst, avg, length_measured):
    
#     best = round(best, 3)
#     worst = round(worst, 3)
#     avg = round(avg, 3)
    
#     f = open("Time Complexity Analysis.txt", "a")
#     f.write("\n" + name)
#     f.write("\nLength of list: " + str(length_measured))
#     f.write("\nBest time: " + str(best))
#     f.write("\nWorst time: " + str(worst))
#     f.write("\nAverage time: " + str(avg) + "\n")
#     f.close()

# def time_merge(sorted_list, reverse_list, random_list):
#     length_measured = len(reverse_list)

#      #record worst time for merge sort
#     t0 = t.perf_counter()
#     merge_sort(reverse_list)
#     t1 = t.perf_counter()
#     worst = t1-t0

#     #record best time for merge sort
#     t0 = t.perf_counter()
#     merge_sort(sorted_list)
#     t1 = t.perf_counter()
#     best = t1-t0

#     #record average time for merge sort
#     t0 = t.perf_counter()
#     merge_sort(random_list)
#     t1 = t.perf_counter()
#     avg = t1-t0


#     return worst, best, avg, length_measured

# def time_quick(sorted_list, reverse_list, random_list):
#     length_measured = len(reverse_list)

#      #record worst time for quicksort
#     t0 = t.perf_counter()
#     quicksort(reverse_list, 0, length_measured - 1)
#     t1 = t.perf_counter()
#     worst = t1-t0

#     #record best time for quicksort
#     t0 = t.perf_counter()
#     quicksort(sorted_list, 0, length_measured - 1)
#     t1 = t.perf_counter()
#     best = t1-t0

#     #record average time for quicksort
#     t0 = t.perf_counter()
#     quicksort(random_list, 0, length_measured - 1)
#     t1 = t.perf_counter()
#     avg = t1-t0


#     return worst, best, avg, length_measured

# def time_insertion(sorted_list, reverse_list, random_list):
#     length_measured = len(reverse_list)

#      #record worst time for insertion sort
#     t0 = t.perf_counter()
#     insertion_sort(reverse_list)
#     t1 = t.perf_counter()
#     worst = t1-t0

#     #record best time for insertion sort
#     t0 = t.perf_counter()
#     insertion_sort(sorted_list)
#     t1 = t.perf_counter()
#     best = t1-t0

#     #record average time for insertion sort
#     t0 = t.perf_counter()
#     insertion_sort(random_list)
#     t1 = t.perf_counter()
#     avg = t1-t0


#     return worst, best, avg, length_measured

# def __main__ ():

#     #Clear our file everytime it is written to
#     open("Time Complexity Analysis.txt", "w").close()

#     #Lists starting at 1000
#     sorted, revers, ran = generate_lists(1000)
#     name = "Bubble Sort"
#     worst, best, avg, length = time_bubble(sorted, revers, ran)
#     writeToFile(name, best, worst, avg, length)

#     name = "Merge Sort"
#     worst, best, avg, length = time_merge(sorted, revers, ran)
#     addToFile(name, best, worst, avg, length)

#     name = "Quicksort"
#     worst, best, avg, length = time_quick(sorted, revers, ran)
#     addToFile(name, best, worst, avg, length)

#     name = "Insertion Sort"
#     worst, best, avg, length = time_insertion(sorted, revers, ran)
#     addToFile(name, best, worst, avg, length)


#     # #Measured at 10000
#     sorted, revers, ran = generate_lists(10000)
#     name = "Bubble Sort"
#     worst, best, avg, length = time_bubble(sorted, revers, ran)
#     writeToFile(name, best, worst, avg, length)

#     name = "Merge Sort"
#     worst, best, avg, length = time_merge(sorted, revers, ran)
#     addToFile(name, best, worst, avg, length)

#     name = "Quicksort"
#     worst, best, avg, length = time_quick(sorted, revers, ran)
#     addToFile(name, best, worst, avg, length)

#     name = "Insertion Sort"
#     worst, best, avg, length = time_insertion(sorted, revers, ran)
#     addToFile(name, best, worst, avg, length)


#     #Measured at 100000
#     sorted, revers, ran = generate_lists(100000)
#     name = "Bubble Sort"
#     worst, best, avg, length = time_bubble(sorted, revers, ran)
#     writeToFile(name, best, worst, avg, length)

#     name = "Merge Sort"
#     worst, best, avg, length = time_merge(sorted, revers, ran)
#     addToFile(name, best, worst, avg, length)

#     name = "Quicksort"
#     worst, best, avg, length = time_quick(sorted, revers, ran)
#     addToFile(name, best, worst, avg, length)

#     name = "Insertion Sort"
#     worst, best, avg, length = time_insertion(sorted, revers, ran)
#     addToFile(name, best, worst, avg, length)


# #Call our main function
# #__main__()

#srtd, rvsd, rand = generate_lists(40)
#bubble_sort_visualized(rand)
#insertion_sort_visualized(rand)
#quicksort_visualized(rand, 0, len(rand) - 1)

def __main__():
    srtd, rvsd, rand = generate_lists(10)
    a = True

    while(a):

        #beginning CLI
        print("HELLO,\n", "PLEASE CHOOSE AN ALGORITHM TO VISUALIZE:")
        print("1. BUBBLE SORT")
        print("2. INSERTION SORT")
        print("3. QIUCK SORT")

        choice = int(input())

        match choice:

            case 1: 
                b = True

                print("-----BUBBLE SORT----")
                print("Would you like to see the:")
                print("1. Best case scenario")
                print("2. Worst case scenario")
                print("3. Average case scenario")

                case_1 = int(input())

                match case_1:

                    case 1:
                        #When b is false, return to the beginning CLI

                        bubble_sort_visualized(srtd)
                        b = False

                    case 2:
                        bubble_sort_visualized(rvsd)
                        b = False
                    case 3:
                        bubble_sort_visualized(rand)
                        b = False
            case 2:
                b = True

                print("-----INSERTION SORT----")
                print("Would you like to see the:")
                print("1. Best case scenario")
                print("2. Worst case scenario")
                print("3. Average case scenario")

                case_2 = int(input())
                match case_2:

                    case 1:
                        #When b is false, return to the beginning CLI

                        insertion_sort_visualized(srtd)
                        b = False

                    case 2:
                        insertion_sort_visualized(rvsd)
                        b = False
                    case 3:
                        insertion_sort_visualized(rand)
                        b = False

            case 3:
                b = True

                print("-----QUICK SORT----")
                print("Would you like to see the:")
                print("1. Best case scenario")
                print("2. Worst case scenario")
                print("3. Average case scenario")

                case_3 = int(input())

                match case_3:

                    case 1:
                        #When b is false, return to the beginning CLI

                        quicksort_visualized(srtd)
                        b = False

                    case 2:
                        quicksort_visualized(rvsd)
                        b = False
                    case 3:
                        quicksort_visualized(rand)
                        b = False


__main__()