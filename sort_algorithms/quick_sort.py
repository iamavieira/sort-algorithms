def quick_sort(array, order):
    if len(array) < 2:
        return array

    pivot = array[len(array)-1]
    lh, hh = [], []
    for i in range(len(array)-1):
        if(order == 'DESC'):
            if(array[i] >= pivot):
                lh.append(array[i])
            else:
                hh.append(array[i])
        else:
            if(array[i] <= pivot):
                lh.append(array[i])
            else:
                hh.append(array[i])


    lh = quick_sort(lh, order)
    hh = quick_sort(hh, order)
    lh.append(pivot)
    lh.extend(hh)
    return lh;


array = [123, 4928583, -5939492, 49, .248, .323, .1140, -21, -13, 306739]
if(__name__ == '__main__'):
    print('original: ' + str(array))
    print(quick_sort(array, 'DESC'))
    print(quick_sort(array, 'ASC'))
    
