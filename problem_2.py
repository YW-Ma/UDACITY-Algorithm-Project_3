def search_smallest(input_list):
    #  exceptional situation processing
    if len(input_list) == 0: # empty list
        return None
    if len(input_list) == 1: # only one item
        return 0
    # normal situation processing
    start = 0
    end = len(input_list)-1
    while start <= end:
        mid = (start+end)//2
        if input_list[mid] < input_list[mid - 1]:
            return mid
        # smallest value located on the right side
        elif input_list[mid] > input_list[end]:
            start = mid + 1
        # smallest value located on the left side
        elif input_list[mid] < input_list[end]:
            end = mid - 1
    return None

def search_number(input_list, number, start, end):
    #  exceptional situation processing
    if len(input_list) == 0:    # don't have any item
        return -1
    if input_list[0] == number: # only one item
        return 0
    # normal situation processing
    while start <= end:
        mid = (start+end)//2
        if input_list[mid] == number:
            return mid
        elif input_list[mid] > number:
            end = mid - 1
        elif input_list[mid] < number:
            start = mid + 1
    return -1 # cannot find
    
def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the number
    Returns:
       int: Index or -1
    """
    # Part 0: exceptional situation processing
    if len(input_list) == 0:    # don't have any item (like [])
        return -1
    if input_list[0] == number: # only one item (like [1])
        return 0
    if input_list[0] < input_list[-1]: # the list is not rotated (like [1,2,3])
        return search_number(input_list, number, 0, len(input_list)-1)
    
    # Part 1: finding out the smallest one's index
    smallest = search_smallest(input_list)
    if smallest is None:
        return -1
    # Part 2: search number in a sub-list
    if number > input_list[0]: # should search it in the first sub-list
        return search_number(input_list, number, 0, smallest-1)
    else:
        return search_number(input_list, number, smallest, len(input_list)-1)
        

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) #pass -- return 0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) #pass -- return 5
test_function([[6, 7, 8, 1, 2, 3, 4], 100]) #pass -- return -1
test_function([[], 8]) #pass -- return -1
test_function([[1], 8]) #pass -- return -1

