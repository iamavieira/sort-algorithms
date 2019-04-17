import sys
#divide-and-conquer
def find_q(r):
    return int(r/2)#round towards 0

def merge(array, p, q, r, order):
    lowHalf, highHalf = array[p:q], array[q:r]
    lh = len(lowHalf) - 1
    hh = len(highHalf) - 1
    for i in range(len(array)-1,-1,-1):
        if(lh < 0):
            array[i] = highHalf[hh]
            hh -= 1
        elif(hh < 0):
            array[i] = lowHalf[lh]
            lh -= 1
        else:
            if(order == 'ASC'):
                if(lowHalf[lh] > highHalf[hh]):
                    array[i] = lowHalf[lh]
                    lh -= 1
                else:
                    array[i] = highHalf[hh]
                    hh -= 1
            else: 
                if(lowHalf[lh] < highHalf[hh]):
                    array[i] = lowHalf[lh]
                    lh -= 1
                else:
                    array[i] = highHalf[hh]
                    hh -= 1
    return array

def merge_sort(array, p, r, order):
    if(r >= 2):
        q = find_q(r)
        array[p:q] = merge_sort(array[p:q], p, len(array[p:q]), order)
        array[q:r] = merge_sort(array[q:r], p, len(array[q:r]), order)
        array = merge(array, p, q, r, order)
    return array

array = [-7, 8, -.23, 45, -12, 35, 90, -111] #p=0;r=6;first subarray is the full array
just_to_be_sure = [.938747, -284, 938,93029, 858, -.24234, 7, 837757, 109493, 395, -24, -114.32, -.2321]
if(__name__ == '__main__'):
    print('original: ' + str(just_to_be_sure))
    #print('recursion limit: ' + str(sys.setrecursionlimit(15000)) + str(sys.getrecursionlimit()))
    print('ascending: ' + str(merge_sort(just_to_be_sure, 0, len(just_to_be_sure), 'ASC')))
    print('descending: ' + str(merge_sort(just_to_be_sure, 0, len(just_to_be_sure), 'DESC')))
