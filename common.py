def swap(array, old_i, new_i):
    tmp = array[old_i]
    array[old_i] = array[new_i]
    array[new_i] = tmp
    return array


