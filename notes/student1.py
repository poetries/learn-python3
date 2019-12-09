'''
继承
'''

class Human(object):
  num =10
  def __init__(self,name,age):
    self.__name = name
    self.__age = age 
    
  def getName(self):
    return self.__name

# 继承父类Human
class Student(Human):
  def __init__(self,school,name,age):
    self.school = school
    # 子类调用父类构造函数 
    # 方式1
    # Human.__init__(self,name,age)
    # 方式2 推荐super
    super(Student,self).__init__(name,age)

  def getInfo(self): 
    return self.getName() + self.school

stu = Student('中山大学','poetry',22)
print(stu.getInfo())