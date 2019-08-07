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
    if (start <= end):
        return

    middle = (start + end) // 2

    m_sort(ls, temp, start, middle)
    print("poop")
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
            j += 1
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


ls = [random.randint(0,50) for i in range(20)]
print(ls)

print('\nSelection Sort:')
selection_sort(ls)
print(ls)

print('\nShuffled Again:')
random.shuffle(ls)
print(ls)

print('\nBubble Sort:')
bubble_sort(ls)
print(ls)

print('\nShuffled Again:')
random.shuffle(ls)
print(ls)

print('\nMerge Sort:')
merge_sort(ls)
print(ls)
