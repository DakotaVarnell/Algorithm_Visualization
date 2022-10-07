import random
import time as t

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

def time_bubble(sorted_list, reverse_list, random_list):
    
    length_measured = len(reverse_list)
    
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

    best = round(best, 3)
    worst = round(worst, 3)
    avg = round(avg, 3)

    f = open("Time Complexity Analysis.txt", "a") 
    f.write("\n" + name)
    f.write("\nLength of list: " + str(length_measured))
    f.write("\nBest time: " + str(best))
    f.write("\nWorst time: " + str(worst))
    f.write("\nAverage time: " + str(avg) + "\n")
    f.close()

def addToFile(name, best, worst, avg, length_measured):
    
    best = round(best, 3)
    worst = round(worst, 3)
    avg = round(avg, 3)
    
    f = open("Time Complexity Analysis.txt", "a")
    f.write("\n" + name)
    f.write("\nLength of list: " + str(length_measured))
    f.write("\nBest time: " + str(best))
    f.write("\nWorst time: " + str(worst))
    f.write("\nAverage time: " + str(avg) + "\n")
    f.close()

def time_merge(sorted_list, reverse_list, random_list):
    length_measured = len(reverse_list)

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
    length_measured = len(reverse_list)

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
    length_measured = len(reverse_list)

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

def __main__ ():

    #Clear our file everytime it is written to
    open("Time Complexity Analysis.txt", "w").close()

    #Lists starting at 1000
    sorted, revers, ran = generate_lists(1000)
    name = "Bubble Sort"
    worst, best, avg, length = time_bubble(sorted, revers, ran)
    writeToFile(name, best, worst, avg, length)

    name = "Merge Sort"
    worst, best, avg, length = time_merge(sorted, revers, ran)
    addToFile(name, best, worst, avg, length)

    name = "Quicksort"
    worst, best, avg, length = time_quick(sorted, revers, ran)
    addToFile(name, best, worst, avg, length)

    name = "Insertion Sort"
    worst, best, avg, length = time_insertion(sorted, revers, ran)
    addToFile(name, best, worst, avg, length)


    #Measured at 10000
    sorted, revers, ran = generate_lists(10000)
    name = "Bubble Sort"
    worst, best, avg, length = time_bubble(sorted, revers, ran)
    writeToFile(name, best, worst, avg, length)

    name = "Merge Sort"
    worst, best, avg, length = time_merge(sorted, revers, ran)
    addToFile(name, best, worst, avg, length)

    name = "Quicksort"
    worst, best, avg, length = time_quick(sorted, revers, ran)
    addToFile(name, best, worst, avg, length)

    name = "Insertion Sort"
    worst, best, avg, length = time_insertion(sorted, revers, ran)
    addToFile(name, best, worst, avg, length)


    #Measured at 100000
    sorted, revers, ran = generate_lists(100000)
    name = "Bubble Sort"
    worst, best, avg, length = time_bubble(sorted, revers, ran)
    writeToFile(name, best, worst, avg, length)

    name = "Merge Sort"
    worst, best, avg, length = time_merge(sorted, revers, ran)
    addToFile(name, best, worst, avg, length)

    name = "Quicksort"
    worst, best, avg, length = time_quick(sorted, revers, ran)
    addToFile(name, best, worst, avg, length)

    name = "Insertion Sort"
    worst, best, avg, length = time_insertion(sorted, revers, ran)
    addToFile(name, best, worst, avg, length)


#Call our main function
__main__()