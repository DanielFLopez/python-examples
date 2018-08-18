from math import floor

def quicksort(arr):
  if not arr:
      return []
  pivot = arr[floor(len(arr)/2)]
  pivots = [x for x in arr if x == pivot]
  lesser = quicksort([x for x in arr if x < pivot])
  greater = quicksort([x for x in arr if x > pivot])
  return lesser + pivots + greater


print(quicksort([9,8,5,7,4,2,1,9,6,3,0]))
