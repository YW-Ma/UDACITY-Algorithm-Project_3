def sqrt(number):
   """
   Calculate the floored square root of a number

   Args:
      number(int): Number to find the floored squared root
   Returns:
      int: Floored Square Root
   """
   lower = 0
   upper = number
   answer = 0
   # binary search -- require O(logn) time, n is the 
   while lower <= upper:
      mid = (lower + upper) // 2
      squre = mid*mid

      # first branch, search in the smaller part
      if squre > number:
         upper = mid - 1
      # second branch, search in the larger part
      if squre < number:
         lower = mid + 1
         answer = mid # update answer (since we want the floor of the sqrt)
      # third branch
      if squre == number:
         return mid
      
   return answer

# Test
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
