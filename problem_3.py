def quick_sort(data):
    """
    Quick sort,
    in descending order.
    """
    if len(data) <= 1: # base case
        return data
    else:
        mid = data[(len(data))//2]
        left = []
        right = []
        data.remove(mid) # remove the base value from the list
        for i in data:
            if i >= mid:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left) + [mid] + quick_sort(right)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # 1. Sorting part: in descending order
    sorted_list = quick_sort(input_list)
    # 2. Digit filling part:
    n1 = 0
    n2 = 0
    for i in range(0, len(sorted_list), 2): # odd indices
        n1 = n1*10
        n1 += sorted_list[i]
    for i in range(1, len(sorted_list), 2): # even indices
        n2 = n2*10
        n2 += sorted_list[i]
    return [n1,n2]

# TEST

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_case_1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_case_2 = [[], [0, 0]]
test_case_3 = [[1], [1, 0]]
test_case_4 = [[4, 6, 2, 5, 9], [952, 64]]

test_function(test_case_1)
test_function(test_case_2)
test_function(test_case_3)
test_function(test_case_4)
