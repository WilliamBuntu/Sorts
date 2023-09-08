def merge_sort(list):
    """_summary_

    Sorts a list in ascending order
    returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort th sublists created in previous step
    Combine: Merge the sorted sublists created in previous step

    Takes O(kn log n) time
    """


    if len(list) <= 1:
        return list

    right_half, left_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):

    """_summary_

    Divides the sorted list at midpoint into sublists
    returns two sublists - left and right

    Takes overall O(k log n) time
    """

    mid = len(list) // 2
    left = list[: mid]
    right = list[mid : ]

    return left, right


def merge(left, right):

    """_summary_
    Merge two lists, sorting  them in the process

    Runs in overall O(n) time

    Returns:
        a New merged list
    """

    l = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1


    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True

    return list[0] < list[1] and verify_sorted(list[1:])




list = [23, 54, 16, 31, 20, 5, 1, 75, 13]
l = merge_sort(list)
# print(l)


print(verify_sorted(list))
print(list)
print( verify_sorted(l))
print(l)
