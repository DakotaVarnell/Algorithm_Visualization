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


def __main__():
    srtd, rvsd, rand = generate_lists(10)
    a = True

    while(a):

        #beginning CLI
        print("HELLO,\n", "PLEASE CHOOSE AN ALGORITHM TO VISUALIZE:")
        print("1. BUBBLE SORT")
        print("2. INSERTION SORT")
        print("3. QUICK SORT")

        choice = int(input())

        match choice:

            case 1: 
                b = True

                print("-----BUBBLE SORT----")
                print("Would you like to see the:")
                print("1. Worst case scenario")
                print("2. Average case scenario")
                print("3. Go back to choose a different algorithm")

                case_1 = int(input())

                match case_1:

                    case 1:
                        bubble_sort_visualized(rvsd)

                    case 2:
                        bubble_sort_visualized(rand)

                    case 3:
                        b = False
            case 2:
                b = True

                print("-----INSERTION SORT----")
                print("Would you like to see the:")
                print("1. Worst case scenario")
                print("2. Average case scenario")
                print("3. Go back to choose a different algorithm")

                case_2 = int(input())
                match case_2:

                    case 1:
                        insertion_sort_visualized(rvsd)

                    case 2:
                        insertion_sort_visualized(rand)

                    case 3:
                        #When b is false, return to the beginning CLI
                        b = False

            case 3:
                b = True

                print("-----QUICK SORT----")
                print("Would you like to see the:")
                print("1. Worst case scenario")
                print("2. Average case scenario")
                print("3. Go back to choose a different algorithm")

                case_3 = int(input())

                match case_3:

                    case 1:
                        quicksort_visualized(rvsd, 0, len(rand) - 1)
                
                    case 2:
                        quicksort_visualized(rand, 0, len(rand) - 1)

                    case 3: 
                        #When b is false, return to the beginning CLI
                        b = False


__main__()