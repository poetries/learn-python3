#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

print('hello, world')

students = ['小明','小红']

print(len(students))

age = 20
if age>10:
  print('123')

for name in students:
  print(name)


def sum(n):
  num = 1
  for x in range(n):
    num +=x 
  return x

print('sum',sum(100))

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

tu = move(100, 100, 60, math.pi / 6)

print(tu) 

def personInfo(name,age,**kw): 
  print(name,age,kw)

info = {
  'name': 'poetry',
  'age': 22,
}
extra = {
'bithday': '1992-12-12',
'addr': '广东省深圳市'
}
personInfo(info['name'],info['age'],**extra)

dd = {'a': 1, 'b': 2, 'c': 3}

for key,v in dd.items():
  print(key,v)



def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

class Stu(object):
  def __init__(self,name,age):
    self.__name = name
    self.__age = age 
  
  # 把一个方法变成属性调用 如stu.age
  @property
  def age(self):
    return self.__age

  @age.setter
  def age(self,age):
    self.__age = age

stu = Stu('poetry',22)

print(stu.age)