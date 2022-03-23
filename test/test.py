# Python implementation of Introsort algorithm

import math
import sys
from heapq import heappush, heappop


def heapsort(array):
    h = []
    for value in array:
        heappush(h, value)
    array = []
    array = array + [heappop(h) for i in range(len(h))]
    return array


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):

        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1, array


def introsort_util(array, begin, end, depthLimit):
    if depthLimit == 0:
        array = heapsort(array)
        return array

    pivot = len(array) // 2
    (array[pivot], array[end]) = (array[end], array[pivot])

    partition_point, array = partition(array, begin, end)

    array = introsort_util(array, begin, partition_point - 1, depthLimit - 1)
    array = introsort_util(array, partition_point + 1, end, depthLimit - 1)
    return array


def introsort(array):
    depthLimit = 2 * math.floor(math.log2(len(array)))
    return introsort_util(array, 0, len(array) - 1, depthLimit)


def main():
    arr = [
        2, 10, 24, 2, 10, 11, 27,
        4, 2, 4, 28, 16, 9, 8,
        28, 10, 13, 24, 22, 28,
        0, 13, 27, 13, 3, 23,
        18, 22, 8, 8]

    print(introsort(arr))


if __name__ == '__main__':
    main()
