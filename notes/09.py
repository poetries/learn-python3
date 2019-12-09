''' 
函数式编程：匿名函数 lambda
'''

def add(x,y):
  return x + y 

add(1,2)

# 匿名函数定义
f = lambda x,y: x+y

print(f(1,2))

arr = [{'key': 'poetries','value': 100},{'key': 'jing','value': 10}]

# 处理键值对
res = map(lambda item: {'name': item['key'],'score': item['value']}, arr)

print(list(res))