# This assumes that priority order is;
# 1. most character count to least character count
# 2. reverse alphabetically.


def add_remove_list(original: list, add: list, remove: list):
    """
    Add, remove from original list then returns a sorted list in reverse (character count, alphabetic) order.
    :param original: a list.
    :param add: a list of elements to be added.
    :param remove: a list to of elements be removed.
    :return: a list.
    """

    # Adds add list to original then remove elements from remove.
    # Set is implemented as hash table.
    data = (set(original) | set(add)) - set(remove)

    temp = dict()
    for v in data:
        length = len(v)
        # Binary Search / Insert
        if length in temp:
            start = 0
            end = len(temp[length]) - 1
            # Searching for appropriate position
            while start <= end:
                mid = (start + end) // 2
                mid_value = temp[length][mid]
                if mid_value > v:
                    start = mid + 1
                elif mid_value < v:
                    end = mid - 1
            # Inserting to sorted list
            temp[length] = temp[length][:start] + [v] + temp[length][start:]
        else:
            temp[length] = [v]

    result = []
    # Populating returning result
    for key in sorted(temp.keys(), reverse=True):
        for element in temp[key]:
            result.append(element)
    return result


original = ['one', 'two', 'three']
add = ['one', 'two', 'five', 'six']
remove = ['two', 'five']

print(add_remove_list(original, add, remove))
