A = [2,4,1,5]
n = len(A)
def sum_arr(A, n):
  sum = 0
  for i in range(n):
    sum = sum + A[i]
  return sum
print(sum_arr(A,n))
