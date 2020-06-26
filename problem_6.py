import sys
def get_min_max(ints):
   """
   Return a tuple(min, max) out of list of unsorted integers.

   Args:
      ints(list): list of integers containing one or more integers
   """
   if len(ints) == 0:
      return None
   max = -sys.maxsize
   min = sys.maxsize
   for i in ints:
      if i <= min:
         min = i
      if i >= max:
         max = i
   return (min, max)


## Test Cases
import random

l = [i for i in range(0, 20)]  # a list containing 0 - 20
random.shuffle(l)
print ("Pass" if ((0, 19) == get_min_max(l)) else "Fail")

l = [i for i in range(-1500, 1000)]  # a list containing -1500 - 999
random.shuffle(l)
print ("Pass" if ((-1500, 999) == get_min_max(l)) else "Fail")

l = [0]  # a list containing one element (0)
print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")

l = []  # a list containing nothing
print ("Pass" if (None == get_min_max(l)) else "Fail")