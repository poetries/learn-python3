''' 
reduce函数
'''

from functools import reduce

arr = [1,2,3,4,5,6]

# 连续调用lambda
r = reduce(lambda x,y:x+y,arr)

print(r)