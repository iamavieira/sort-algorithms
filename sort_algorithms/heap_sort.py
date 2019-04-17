main = False
if(__name__ == '__main__'):
    main = True
import math
import sys
from collections import deque
from common import swap
array = [10, 2, 3, -727, 98375, 826, 2.458, .2434, -.32, -0]

def build_max_heap(array):
    if main:
        print("Buildiing max heap... ")
    for i in range(len(array)-1, -1, -1):
        parent = int(i/2)
        if(0 <= parent < len(array)):
           if main:
              print('Parent: ' + str(array[parent]) + ' position: ' + str(parent))
           try:
             if main:
                print('Children: ' + str(array[2*parent+1]) + ' ' + str(array[2*parent+2]))
           except IndexError:
             if main:
                print('One or both childs are out of range')

           array = heapify(array, parent)
           if main:
              print('Subtree heapified: ' + str(array))
    
    return array

def heapify(array, i):

    if(0 <= 2*i+1 < len(array) and 0 <= 2*i+2 < len(array)):
        if(array[i] <= array[2*i+1] and array[i] <= array[2*i+2]):
            if(array[2*i+1] > array[2*i+2]):
                heapify(swap(array, i, 2*i+1), 2*i+1)
            else: 
                heapify(swap(array, i, 2*i+2), 2*i+2)

        elif(array[i] <= array[2*i+1]):
            heapify(swap(array, i, 2*i+1), 2*i+1)
        elif(array[i] <= array[2*i+2]):
            heapify(swap(array, i, 2*i+2), 2*i+2)

    elif(0 <= 2*i+1 < len(array)):
        if(array[i] <= array[2*i+1]):
            heapify(swap(array, i, 2*i+1), 2*i+1)

    return array

def heap_sort(array):
    queue = deque()
    array_copy = list(array)
    array_copy = build_max_heap(array_copy)
    for i in range(len(array_copy)):
        array_copy = swap(array_copy, 0, len(array_copy)-1)
        queue.appendleft(array_copy[len(array_copy)-1])
        array_copy.pop()
        array_copy = heapify(array_copy, 0)
    return queue

if(main):
    print('Original: ' + str(array))
    print('Heap sort: ' + str(heap_sort(array)))
