# f = open('test.txt',encoding='utf-8')

# data = f.readlines()
# for line in data:
#   print(line.strip('\n'))
  
# f.close()
from functools import reduce

with open('test.txt') as f:
  for line in f.readlines():
    print(line.strip('\n'))

def test(name,**kw):
  print(kw)

extra = {'auth': '112'}
test('poet',**extra)

arr = [1,2,3,4,5]
a = iter(arr)

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

print ( reduce(lambda x,y: x+y,[1,2,3,4,5,6],0) )

import  time

print(time.time())

import test

test.test()

import os

print(os.path.abspath('..'))
print(os.path.exists('test'))