import sys


def solve():
  # Read all tokens from standard input efficiently
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  n = int(input_data[0])
  m = int(input_data[1])

  # Initialize degree array with zeros (1-based index up to n)
  degrees = [0] * (n + 1)

  # Process each edge
  idx = 2
  for _ in range(m):
    u = int(input_data[idx])
    v = int(input_data[idx + 1])
    degrees[u] += 1
    degrees[v] += 1
    idx += 2

  # Output the degrees from vertex 1 to n, separated by a space
  print(*(degrees[1:]))


if __name__ == "__main__":
  solve()
