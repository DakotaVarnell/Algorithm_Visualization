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


sorted, revers, ran = generate_lists(10)
print(sorted)
print(revers)
print(ran)

def time_bubble(sorted_list, reverse_list, random_list):

    

    #record worst time for bubble sort
    t0 = t.perf_counter()
    bubble_sort(reverse_list)
    t1 = t.perf_counter()
    bubble_worst = t1-t0

    #record best time for bubble sort
    t0 = t.perf_counter()
    bubble_sort(sorted_list)
    t1 = t.perf_counter()
    bubble_best = t1-t0

    #record average time for bubble sort
    t0 = t.perf_counter()
    bubble_sort(random_list)
    t1 = t.perf_counter()
    bubble_avg = t1-t0

    return bubble_worst, bubble_best, bubble_avg

def time_merge(sorted_list, reverse_list, random_list):

     #record worst time for merge sort
    t0 = t.perf_counter()
    merge_sort(reverse_list)
    t1 = t.perf_counter()
    merge_worst = t1-t0

    #record best time for merge sort
    t0 = t.perf_counter()
    merge_sort(sorted_list)
    t1 = t.perf_counter()
    merge_best = t1-t0

    #record average time for merge sort
    t0 = t.perf_counter()
    merge_sort(random_list)
    t1 = t.perf_counter()
    merge_avg = t1-t0


    return merge_worst, merge_best, merge_avg

def time_quick(sorted_list, reverse_list, random_list):

     #record worst time for quicksort
    t0 = t.perf_counter()
    quicksort(reverse_list)
    t1 = t.perf_counter()
    quick_worst = t1-t0

    #record best time for quicksort
    t0 = t.perf_counter()
    quicksort(sorted_list)
    t1 = t.perf_counter()
    quick_best = t1-t0

    #record average time for quicksort
    t0 = t.perf_counter()
    quicksort(random_list)
    t1 = t.perf_counter()
    quick_avg = t1-t0


    return quick_worst, quick_best, quick_avg

def writeToFile(name, best, worse, average):
    name = bubble_sort
    with open("Time Compexity Analysis", 'w') as f:
        
#hefowefef

def time_insertion(sorted_list, reverse_list, random_list):
    
    length = len(reverse_list)
    length = len(sorted_list)
    length = len(random_list)

    #record worst time for insertion sort
    t0 = t.perf_counter()
    insertion_sort(reverse_list)
    t1 = t.perf_counter()
    insertion_worst = t1-t0

    #record best time for insertion sort
    t0 = t.perf_counter()
    insertion_sort(sorted_list)
    t1 = t.perf_counter()
    insertion_best = t1-t0

    #record average time for insertion sort
    t0 = t.perf_counter()
    insertion_sort(random_list)
    t1 = t.perf_counter()
    insertion_avg = t1-t0


    return insertion_worst, insertion_best, insertion_avg

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
#Call our main function
__main__()
    