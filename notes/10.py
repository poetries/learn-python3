''' 
map函数
'''


arr = [1,2,3,4,5,6]
arr2 = [10,12,14,16,12,14]

# 列表推导式
a = [i*i for i in arr ]

# print(a)

# map函数
b = map(lambda x: x*x,arr)
print(list(b))

c = map(lambda x,y: x*x + y,arr,arr2) # 可以传多个list，个数要相同
print(list(c))