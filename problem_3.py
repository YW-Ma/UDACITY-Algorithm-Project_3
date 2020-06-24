def quick_sort(data):
    if len(data) <= 1: # base case
        return data
    else:
        mid = data[(len(data))//2]
        left = []
        right = []
        data.remove(mid) # remove the base value from the list
        for i in data:
            if i >= mid:
                right.append(i)
            else:
                left.append(i)
        return quick_sort(left) + [mid] + quick_sort(right)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # 1. Sorting part:
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


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]