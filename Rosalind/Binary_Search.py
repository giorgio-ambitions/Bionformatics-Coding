import sys
from bisect import bisect_left

def solve_bins():
  input_data = sys.stdin.read().split()
  if not input_data:
    return 
    
  n=int(input_data[0])
  m=int(input_data[1])

  # Read the sorted array A (1-based index implied in thought, 0-based in code)
  A = [int(x) for x in input_data[2 : 2 + n]]
  queries = [int(x) for x in input_data[2 + n :]]  # Fixed missing bracket here

  result = []
  for k in queries:
    #Find the intersection point using binary search 
    idx = bisect_left(A, k)
    #Check if the element exist at that index and matches the query 
    if idx<n and A[idx] == k:
      results.append(str(idx+1)) # Convert to 1-based index
  else:
      results.append(" ".join(results))

if __name__ == "__main__":
  solve_bins()


