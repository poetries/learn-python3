''' 
filter函数
'''

arr = [1,2,3,4,5,6,7,0,0,False,'']

# 过滤空字符串
res = filter(lambda x: not not x,arr)

print(list(res)) # [1,2,3,4,5,6,7]