''' 
装饰器:特性、注解
'''

import time 

def decorator1(func):
  def wrapper(name):
    print(time.time())
    func(name)
  return wrapper

@decorator1 
def f1(name):
  print('this is a func',name)

# f1('poetries')

def decorator2(func):
  def wrapper(*args,**kw):
    print(time.time())
    print(args,'args')
    print(kw,'kw')
    func(*args,**kw)
  return wrapper

@decorator2
def f2(p1,p2):
  print('this is a func',p1,p2)

f2('静观流叶','1')