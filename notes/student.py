'''
面向对象
类=面向对象

行为、特征

类最基本的作用封装代码
'''

__author__ = 'poetries'

class Student(Human):
  # 类变量 静态属性
  author = 'poetry' 
  SUM = 10
  num = 999
  score = 98
  text = '小明今年'


  def __init__(self,name,age):
    # 构造函数 初始化对象属性
    # 成员可见性 __外部不能访问
    self.__name = name 
    self.__age = age 

  # 实例方法 第一个参数默认是self
  def getAge(self):
    # 实例中可调用类变量
    # print(self.author)
    return self.__getText() + str(self.__age)
  def getName(self):
    return self.__name
  def setName(self,name):
    self.__name = name
  
  # 私有方法，外部不可以访问
  def __getText(self):
    return self.text

  # 静态方法
  # 没有self
  # 实例和类都可以调用
  @staticmethod
  def test():
    # 内部可以访问类变量
    print('静态方法',Student.SUM)
  
  # 类方法 操作和类相关的
  # cls代表student这个类
  # 使用方式 student.testd()
  # 实例和类都可以调用，不要使用实例调用
  # 推荐使用类方法代替静态方法
  @classmethod
  def testd(cls):
    print('classMethod')
  
stu = Student('poetries',22)

print(stu.getAge())

# 修改内部变量值，通过内部定义一个方法，可以在内部进行判断，起到保护作用
stu.setName('静观流叶')

print(stu.getName())

# print(Student.author)
# print(Student.__dict__)
# print(Student.test())