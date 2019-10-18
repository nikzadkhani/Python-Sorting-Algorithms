import random

def selection_sort(ls):
    """ Implementation of the Selection Sort Algorithm:
        Linear Move Time: O(n) Quadratic Comparison Time: O(n^2),
        Overall Time: O(n) + O(n^2) = O(n^2)
    """
    for i in range(len(ls) - 1):
        swap(ls, i, i + find_index_min(ls[(i):]))

def bubble_sort(ls):
    """ Implementation of the Bubble Sort Algorithm:
        Quadratic Move Time: O(n^2), Quadratic Comparison Time: O(n^2)
        Overall Time: O(n^2) + O(n^2) = O(n^2)
    """
    for i in range(len(ls) - 1, 0, -1):
        for j in range(0, i):
            if ls[j] > ls[j + 1]:
                swap(ls, j, j + 1)

def swap(ls, first_index, second_index):
    """ Helper function that swaps the elements at the given indices
        within the list ls
    """
    temp = ls[first_index]
    ls[first_index] = ls[second_index]
    ls[second_index] = temp

def find_index_min(ls):
    """ Finds the index of the minimum value according to the '<' operator
        returns the index as an integer
    """
    min_index = 0
    for i in range(1, len(ls)):
        if ls[i] < ls[min_index]:
            min_index = i
    return min_index

def merge_sort(ls):
    """ Implementation of the Merge Sort Algorithm:
        Logarithmic Move Time: O(nlog(n) Logarithmic Comparison Time: O(nlog(n)
        Overall Time: O(nlog(n)) + O(nlog(n)) = O(nlog(n))
    """
    temp = [0] * len(ls)
    m_sort(ls, temp, 0, len(ls) - 1)

def m_sort(ls, temp, start, end):
    """ Recursion of the Merge Sort Algorithm
        Helper function that handles the recursion, so the wrapper doesn't
        have to.
    """
    if (start >= end):
        return

    middle = (start + end) // 2

    m_sort(ls, temp, start, middle)
    m_sort(ls, temp, middle + 1, end)

    i = start
    j = middle + 1
    k = start

    left_start = start
    left_end = middle
    right_start = middle + 1
    right_end = end

    while i <= left_end and j <= right_end:
        if ls[i] < ls[j]:
            temp[k] = ls[i]
            i += 1
            k += 1
        else:
            temp[k] = ls[j]
            j += 1
            k += 1

    while i <= left_end:
        temp[k] = ls[i]
        i += 1
        k += 1

    while j <= right_end:
        temp[k] = ls[j]
        j += 1
        k += 1

    for i in range(left_start, right_end + 1):
        ls[i] = temp[i]

def insertion_sort(ls):
    """ Implementation of the Insertion Sort Algorithm
        Quadratic Move Time: O(n^2), Quadratic Comparison Time: O(n^2)
        Overall Time: O(n^2) + O(n^2) = O(n^2)
    """
    for i in range(1, len(ls)):
        if ls[i] < ls[i - 1]:
            to_insert = ls[i]

            j = i
            while True:
                ls[j] = ls[j - 1]
                j += -1

                if j <= 0 or to_insert >= ls[j - 1]:
                    break

            ls[j] = to_insert

def quick_sort(ls):
    """ Implementation of the Quick Sort Algorithm
        Move Time: O(n^2), Comparison Time: O(n)
        Overall Time: O(n^2) + O(n^2) = O(n^2)
    """
    q_sort(ls, 0 , len(ls) - 1)

def q_sort(ls, first, last):
    pivot = ls[(first + last) // 2]
    i = first
    j = last

    while True:
        while ls[i] < pivot:
            i += 1
        while ls[j] > pivot:
            j += -1

        if i < j:
            swap(ls, i, j)
            i += 1
            j += -1
        else:
            break

    if first < j:
        q_sort(ls, first, j)
    if last > j + 1:
        q_sort(ls, j + 1, last)

def count_sort(ls):
    """ An implementation of one version of the count sort Algorithm
        k is the range of values from the max to the min
        Additional Memory: O(k), Overall Time: O(n + k)
    """
    min_val = min(ls)
    max_val = max(ls)
    counts = [0] * (max_val - min_val + 1)

    for i in ls:
        counts[i - min_val] += 1

    j = 0
    for i in range(len(counts)):
        while counts[i] != 0:
            ls[j] = i + min_val
            j += 1
            counts[i] += -1
