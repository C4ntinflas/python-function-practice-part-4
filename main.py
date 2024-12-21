def max_num(a, b, c):
  """Finds the maximum of three numbers.

  Args:
    a: The first number.
    b: The second number.
    c: The third number.

  Returns:
    The maximum of the three numbers.
  """
  return max(a, b, c)

def mult_list(numbers):
  """Multiplies all the numbers in a list.

  Args:
    numbers: A list of numbers.

  Returns:
    The product of all numbers in the list.
  """
  result = 1
  for num in numbers:
    result *= num
  return result

def rev_string(s):
  """Reverses a string.

  Args:
    s: The string to reverse.

  Returns:
    The reversed string.
  """
  return s[::-1]

def num_within(x, a, b):
  """Checks if a number falls within a given range (inclusive).

  Args:
    x: The number to check.
    a: The beginning of the range.
    b: The end of the range.

  Returns:
    True if x is within the range [a, b], False otherwise.
  """
  return a <= x <= b

def pascal(n):
  """Prints the first n rows of Pascal's triangle.

  Args:
    n: The number of rows to print.
  """
  row = [1]
  for x in range(n):
    print(row)
    row = [1] + [row[y] + row[y+1] for y in range(len(row)-1)] + [1]

# Example usage:
print(max_num(1, 2, 3))  # Output: 3
print(mult_list([1, 2, 3]))  # Output: 6
print(rev_string("hello"))  # Output: olleh
print(num_within(3, 2, 4))  # Output: True
print(num_within(3, 1, 3))  # Output: True
print(num_within(10, 2, 5))  # Output: False
pascal(5) 