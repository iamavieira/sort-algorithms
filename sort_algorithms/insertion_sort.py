main = False
if(__name__ == '__main__'):
    main = True

def ascending(array):
    for i in range(1, len(array)):
      hasMoved, notPlaced = False, True
      key = array[i]
      for j in range(i-1, -1, -1):
          #print('i ' + str(i))
          if(key < array[j]):
              array[j+1] = array[j]
              hasMoved = True
              if main:
                 print('hasMoved '+ str(array) + ' key ' + str(key))
          else:
              array[j+1] = key
              if main:
                 print('isPlaced ' + str(array) + ' key ' + str(key))
              notPlaced = False
              break
      if(hasMoved and notPlaced):
          array[0] = key
          if main:
             print('isPlaced ' + str(array) + ' key ' + str(key))
    return array

def descending(array):
    for i in range(1, len(array)):
        key = array[i]
        hasMoved, notPlaced = False, True
        for j in range(i-1, -1, -1):
            if(key > array[j]):
                array[j+1] = array[j]
                hasMoved = True
                if main:
                    print('hasMoved ' + str(array) + ' key ' + str(key))
            else:
                array[j+1] = key
                notPlaced = False
                if main:
                     print('isPlaced: ' + str(array) + ' key ' + str(key))
                break
        if(hasMoved and notPlaced):
           array[0] = key
           if main:
              print('isPlaced: ' + str(array) + ' key ' + str(key))
    return array 

training_set = [12, 20, 1, -15, -100, -.6789, -.34533]
validation_set = [12, 20, -15, -100, 100, 37]
if(main):
    print('original/unmodified: ' + str(training_set))
    print('\nascending: ' + str(ascending(training_set)) + '\n')
    print('\ndescending: ' + str(descending(training_set)))
