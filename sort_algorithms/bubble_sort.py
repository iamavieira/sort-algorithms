from common import swap

def ascending(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if(array[j]>array[j+1]):
                swap(array, j, j+1)
    return array

def descending(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if(array[j]<array[j+1]):
                swap(array, j, j+1)
    return array

array = [100, 1.5, 28.3, -17, -219, 1]
if(__name__ == '__main__'):
    print('original: ' + str(array))
    print('ascending: ' + str(ascending(array)))
    print('descending: ' + str(descending(array)))
