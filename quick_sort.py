from concurrent.futures import ProcessPoolExecutor
import numpy as np
from functools import partial

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def parallel_quicksort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    
    threshold = 10000
    
    if len(left) > threshold or len(right) > threshold:
        with ProcessPoolExecutor() as executor:
            future_left = executor.submit(parallel_quicksort, left)
            future_right = executor.submit(parallel_quicksort, right)
            
            left = future_left.result()
            right = future_right.result()
    else:
        left = parallel_quicksort(left)
        right = parallel_quicksort(right)
    
    return left + middle + right

def main():
    data = list(np.random.randint(10, 100000, 1000000))
    print(data)
    
    sorted_data = parallel_quicksort(data.copy())

    print('=============== sorted =================')
    
    print(sorted_data)
    

if __name__ == "__main__":
    main()