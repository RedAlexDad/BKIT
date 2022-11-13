def bubble_sort(array):
    changed = True
    while changed:
        changed = False
        for i in range(0, len(array) -1):
            if(array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1],  array[i]
                changed = True
    return array




