"""
Create a function named sumSquareCube that takes integer n as input and prints the sum of square and cube of n. Use this function to print sum for 2, 9, 11
"""
def sum_square_cube(n):
  sq = n*n
  cu = n*n*n
  sm = sq + cu
  return sm

num = int(input("Enter Number: "))
print(sum_square_cube(num))
