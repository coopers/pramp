import heapq

def find_grants_cap(a, budget):
  heapq.heapify(a)
  while a:
    average = float(budget) / len(a)
    n = heapq.heappop(a)
    if n < average:
      budget -= n
    else:
      return average

assert find_grants_cap([2, 100, 50, 120, 1000], 190) == 47.0
