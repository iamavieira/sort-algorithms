from timeit import default_timer as timer
from common import swap

def ascending(array):
    sorted = True;
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if(array[j]>array[j+1]):
              swap(array, j, j+1) 
              sorted = False;
        if(sorted): 
            break;
    return array;

def descending(array):
    sorted = True
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if(array[j] < array[j+1]):
                swap(array, j, j+1) 
                sorted = False;
        if(sorted):
            break;
    return array;

array = [100, 1.5, 28.3, -17, -219, 1];
ascending_array = [0, 1, 2, 3, 4, 5, 6]
if(__name__ == '__main__'):
    print('original: ' + str(array)); 
    print('ascending: ' + str(ascending(array)));
    print('descending: ' + str(descending(array)));
