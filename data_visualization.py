import random
import matplotlib.pyplot as plt
import numpy as np

#------------IMPORTANT------------#
#matplotlib and numpy must be installed to successfully compile this program
#if you are using anaconda:
#conda install matplotlib
#conda install numpy

#if you are using pip:
#pip install matplotlib
#pip install numpy

#it is best practice to use an environment rather than intall in the base env


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
            plt.bar(x, myList) #creates a bar for each element in myList
            plt.pause(wait_time) #pause to allow the bars to be seen
            plt.clf() #clear frame
            if myList[j] > myList[j + 1]: #if the current value is greater than the next
                myList[j], myList[j+1] = \
                    myList[j + 1], myList[j] #swap them
    return myList
plt.show() #what does this do?
    
#merge is used for timing the algorithm
def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result
    
#merge_sort is used for timing the algorihtm
def merge_sort(m):
    if len(m) <= 1:
        return m
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

#merge_visualized shows the visualization of the sorting algorithm
def merge_visualized(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result

#merge_sort_visualization shows the visualization of the sorting algorithm
def merge_sort_visualized(m):
    if len(m) <= 1:
        return m
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


def quick_sort():
    return
    
def quick_sort_visualized():
    #implement visualization of quick sort
    return





def __main__ ():
    sorted, revers, ran = generate_lists(10)

    x = bubble_sort_visualized(ran)
    print(x)

    return



__main__()



