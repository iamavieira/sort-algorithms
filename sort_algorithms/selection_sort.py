def ascending(array):
    for i in range(len(array)-1, -1, -1):
        key = array[i]
        j_position = i
        for j in range(i+1):
            if(key < array[j]):
                j_position = j
                key = array[j]
        array[j_position] = array[i]
        array[i] = key
    return array
        
def descending(array):
    for i in range(len(array)-1, -1, -1):
        key = array[i]
        j_position = i
        for j in range(i):
            if(key > array[j]):
                j_position = j
                key = array[j]
        array[j_position] = array[i]
        array[i] = key
    return array

validation_array = [19, .87, -48593, -399, -.38583, .213, 21]
if(__name__ == '__main__'):
    print("original: " + str(validation_array)) 
    print("ascending: "+ str(ascending(validation_array)))
    print("descending: " + str(descending(validation_array)))
