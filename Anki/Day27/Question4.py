def solve(arr, queries):
  # Initialize the function find() with the array arr
  def find(x, y):
    # If x is greater than y, return 1
    if x > y:
      return 1

    # Calculate the value of pow(A[x], find(x+1, y)) and assign it to ans
    ans = pow(arr[x], find(x+1, y))

    # Return the value of ans
    return ans

  # Iterate over the queries
  for query in queries:
    # Get the values of x and y from the query
    x, y = query

    # Check if the value of find(x, y) is even or odd and print the result
    if find(x, y) % 2 == 0:
      print("Even")
    else:
      print("Odd")
