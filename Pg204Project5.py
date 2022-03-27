def isSorted(lst):
  return all(lst[x] < lst[x + 1] for x in range(len(lst) - 1))
  return True
  return False
  
