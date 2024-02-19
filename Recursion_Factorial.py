def fc(n):
 res = 1
 while n > 0:
    res = res * n
    n = n - 1
    return res
print(fc(4)) # 24
print("==========")
# Recursion
def fc(n):
    # base case
    if n == 1:
        return 1
    # recursion case
    else:
        return n * fc(n-1)
print(fc(1))