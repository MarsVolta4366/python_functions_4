# max_num
def max_num(num1, num2, num3):
    return max(num1, num2, num3)

print(max_num(90, 6, 2))

# mult_list
def mult_list(list):
    result = 1
    for num in list:
        result = result * num
    return result

print(mult_list([3, 5, 4, 9]))

# rev_string
def rev_string(inputString):
    return inputString[::-1]

print(rev_string("Hello, how are you?"))

# fib
def fib(n):
    if n == 0:
        return "Invalid Input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

print(fib(6))

# num_within
def num_within(num, range_start, range_end):
    if num in range(range_start, range_end + 1):
        return True
    else:
        return False 
print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))

# pascal
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate numbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(5)
