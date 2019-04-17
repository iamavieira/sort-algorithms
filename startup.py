from sort_algorithms import (bubble_sort as bs,
                            improved_bubble_sort as ibs,
                            selection_sort as ss, 
                            insertion_sort as ins, 
                            merge_sort as ms, 
                            heap_sort as hs,
                            quick_sort as qs) 


from timeit import default_timer as timer

array = [10, 100, 72, -72, -.231, .1, -3885, -.84, -.4432]

print('original: ' + str(array))

print('bubble sort ascending: ')
start = timer()
result = bs.ascending(array);
end = timer()
print(f'result: {result} time: {end-start}')

print('bubble sort descending: ')
start = timer()
result = bs.descending(array);
end = timer()
print(f'result: {result} time: {end-start}')

print('improved bubble sort ascending: ')
start = timer()
result = ibs.ascending(array);
end = timer()
print(f'result: {result} time: {end-start}')

print('improved bubble sort descending: ')
start = timer()
result = ibs.descending(array);
end = timer()
print(f'result: {result} time: {end-start}')

print('selection sort ascending: ')
start = timer()
result = ss.ascending(array);
end = timer()
print(f'result: {result} time: {end-start}')

print('selection sort descending: ')
start = timer()
result = ss.descending(array);
end = timer()
print(f'result: {result} time: {end-start}')

print('insertion sort ascending: ')
start = timer()
result = ins.ascending(array);
end = timer()
print(f'result: {result} time: {end-start}')

print('insertion sort descending: ')
start = timer()
result = ins.descending(array);
end = timer()
print(f'result: {result} time: {end-start}')

print('merge sort ascending: ')
start = timer()
result = ms.merge_sort(array, 0, len(array), 'ASC')
end = timer()
print(f'result: {result} time: {end-start}')

print('merge sort descending: ')
start = timer()
result = ms.merge_sort(array, 0, len(array), 'DESC')
end = timer()
print(f'result: {result} time: {end-start}')

print('heap sort: ')
start = timer()
result = hs.heap_sort(array)
end = timer()
print(f'result: {result} time: {end-start}')

print('quick sort descending: ')
start = timer()
result = qs.quick_sort(array, 'DESC')
end = timer()
print(f'result: {result} time: {end-start}')

print('quick sort ascending: ')
start = timer()
result = qs.quick_sort(array, 'ASC')
end = timer()
print(f'result: {result} time: {end-start}')
